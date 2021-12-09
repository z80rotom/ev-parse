import os
from argparse import ArgumentParser

import UnityPy

from ev_cmd import EvCmdType

ROOT_DIR = r"C:\Users\mhenderson\AppData\Roaming\yuzu\dump\0100000011D90000\romfs\StreamingAssets\AssetAssistant"
EV_SCRIPT = r"Dpr\ev_script"

def parse_ev_script(tree, name=None):
    if "Scripts" not in tree:
        # Not actually an ev_script
        return
    
    compiledScripts = {}
    scripts = tree["Scripts"]
    for script in scripts:
        label = script["Label"]
        compiledCommands = []
        commands = script["Commands"]
        for argDict in commands:
            args = argDict["Arg"]
            if len(args) == 0:
                continue
            arg = args[0]
            evCmd = EvCmdType(arg["data"])
            
            compiledCommands.append("{}({})".format(
                evCmd.name,
                ", ".join([str(arg["data"]) for arg in args[1:]])
            ))
        compiledScripts[label] = compiledCommands
    return compiledScripts

def write_ev_script(ofdir, name, compiledScripts):
    if not compiledScripts:
        return
    ofpath = os.path.join(ofdir, "{}.ev".format(name))
    if not os.path.exists(ofdir):
        os.mkdir(ofdir)
    with open(ofpath, "w") as ofobj:
        lines = []
        for label, script in compiledScripts.items():
            lines.append("{}:\n{}".format(
                label,
                "\n".join(["\t{}".format(cmd) for cmd in script])
            ))
        data = "\n".join(lines)
        ofobj.write(data)

def parse_ev_scripts(ifdir, ofdir):
    with open(ifdir, "rb") as ifobj:
        bundle = UnityPy.load(ifdir)

        for obj in bundle.objects:
            if obj.type.name == "MonoBehaviour":
                data = obj.read()
                if obj.serialized_type.nodes:
                        tree = obj.read_typetree()
                        compiledScripts = parse_ev_script(tree, name=data.name)
                        write_ev_script(ofdir, data.name, compiledScripts)

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", dest='ifpath', action='store', required=True)
    parser.add_argument("-o", "--output", dest='ofdir', action='store', default="parsed")
    
    vargs = parser.parse_args()
    parse_ev_scripts(vargs.ifpath, vargs.ofdir)

if __name__ == "__main__":
    main()