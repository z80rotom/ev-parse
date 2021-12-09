import os
import struct
from argparse import ArgumentParser

import UnityPy

from ev_cmd import EvCmdType

def decode_int(var):
    # Thanks Aldo796
    var = int(var)
    data = float(struct.unpack('!f', struct.pack('!I', var & 0xFFFFFFFF))[0])
    return data

def add_tamago(args):
    monsNo = int(decode_int(args[0]["data"]))
    placeNo = int(decode_int(args[1]["data"]))
    args[0]["data"] = monsNo
    args[1]["data"] = placeNo
    return args

EV_CMD_TYPE_MAP = {
    EvCmdType._ADD_TAMAGO: add_tamago
}

def parse_ev_script(tree, name=None):
    if "Scripts" not in tree:
        # Not actually an ev_script
        return
    
    compiledScripts = {}
    strList = tree["StrList"]
    strList = [it.encode("ascii", "ignore").decode() for it in strList]
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
            
            if evCmd in EV_CMD_TYPE_MAP:
                args = EV_CMD_TYPE_MAP[evCmd](args[1:])
            else:
                args = args[1:]

            argData = []
            for arg in args:
                if arg["argType"] == 2:
                    # Work
                    argData.append("@{}".format(arg["data"]))
                    continue
                if arg["argType"] == 3:
                    # Flag
                    argData.append("#{}".format(arg["data"]))
                    continue
                if arg["argType"] == 4:
                    # Sys Flag
                    argData.append("${}".format(arg["data"]))
                    continue                
                if arg["argType"] == 5:
                    strIdx = arg["data"]
                    strVal = strList[strIdx]
                    argData.append('"{}"'.format(strVal))
                if arg["argType"] not in range(0, 6):
                    print(arg["argType"])
                argData.append(arg["data"])
            compiledCommands.append("{}({})".format(
                evCmd.name,
                ", ".join([str(arg) for arg in argData])
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