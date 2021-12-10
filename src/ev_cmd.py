from enum import IntEnum, auto

class EvCmdType(IntEnum):
    _NONE_USE_NUMBER = -1
    _NOP = 1
    _DUMMY = auto()
    _END = auto()
    _TIME_WAIT = auto()
    _LD_REG_VAL = auto()
    _LD_REG_WDATA = auto()
    _LD_REG_ADR = auto()
    _LD_ADR_VAL = auto()
    _LD_ADR_REG = auto()
    _LD_REG_REG = auto()
    _LD_ADR_ADR = auto()
    _CP_REG_REG = auto()
    _CP_REG_VAL = auto()
    _CP_REG_ADR = auto()
    _CP_ADR_REG = auto()
    _CP_ADR_VAL = auto()
    _CP_ADR_ADR = auto()
    _CMPVAL = auto()
    _CMPWK = auto()
    _DEBUG_WATCH_WORK = auto()
    _VM_ADD = auto()
    _CHG_COMMON_SCR = auto()
    _CHG_LOCAL_SCR = auto()
    _JUMP = auto()
    _OBJ_ID_JUMP = auto()
    _BG_ID_JUMP = auto()
    _PLAYER_DIR_JUMP = auto()
    _CALL = auto()
    _RET = auto()
    _IF_JUMP = auto()
    _IF_CALL = auto()
    _IFVAL_JUMP = auto()
    _IFVAL_CALL = auto()
    _IFWK_JUMP = auto()
    _IFWK_CALL = auto()
    _SWITCH = auto()
    _CASE_JUMP = auto()
    _CASE_CANCEL = auto()
    _ADD_WAITICON = auto()
    _DEL_WAITICON = auto()
    _FLAG_SET = auto()
    _ARRIVE_FLAG_SET = auto()
    _FLAG_RESET = auto()
    _FLAG_CHECK = auto()
    _IF_FLAGON_JUMP = auto()
    _IF_FLAGOFF_JUMP = auto()
    _IF_FLAGON_CALL = auto()
    _IF_FLAGOFF_CALL = auto()
    _FLAG_CHECK_WK = auto()
    _FLAG_SET_WK = auto()
    _TRAINER_FLAG_SET = auto()
    _TRAINER_FLAG_RESET = auto()
    _TRAINER_FLAG_CHECK = auto()
    _IF_TR_FLAGON_JUMP = auto()
    _IF_TR_FLAGOFF_JUMP = auto()
    _IF_TR_FLAGON_CALL = auto()
    _IF_TR_FLAGOFF_CALL = auto()
    _ADD_WK = auto()
    _SUB_WK = auto()
    _LDVAL = auto()
    _LDWK = auto()
    _LDWKVAL = auto()
    _TALKMSG_ALLPUT = auto()
    _TALKMSG_ALLPUT_ARC = auto()
    _TALKMSG_ARC = auto()
    _TALKMSG_ALLPUT_PMS = auto()
    _TALKMSG_PMS = auto()
    _TALKMSG_BTOWER_APPEAR = auto()
    _TALKMSG_NG_POKE_NAME = auto()
    _TALKMSG = auto()
    _TALKMSG_SP = auto()
    _TALKMSG_SP_AUTO = auto()
    _TALKMSG_NOSKIP = auto()
    _TALKMSG_CON_SIO = auto()
    _TALKMSG_AUTOGET = auto()
    _AB_KEYWAIT = auto()
    _AB_KEY_TIME_WAIT = auto()
    _LAST_KEYWAIT = auto()
    _NEXT_ANM_LAST_KEYWAIT = auto()
    _TALK_OPEN = auto()
    _TALK_CLOSE = auto()
    _TALK_CLOSE_NO_CLEAR = auto()
    _TALK_KEYWAIT = auto()
    _EASY_OBJ_MSG = auto()
    _EASY_MSG = auto()
    _BOARD_MAKE = auto()
    _INFOBOARD_MAKE = auto()
    _BOARD_REQ = auto()
    _BOARD_REQ_WAIT = auto()
    _BOARD_MSG = auto()
    _BOARD_END_WAIT = auto()
    _EASY_BOARD_MSG = auto()
    _EASY_INFOBOARD_MSG = auto()
    _MENU_REQ = auto()
    _BG_SCROLL = auto()
    _YES_NO_WIN = auto()
    _GUINNESS_WIN = auto()
    _BMPMENU_INIT = auto()
    _BMPMENU_INIT_EX = auto()
    _BMPMENU_MAKE_LIST = auto()
    _BMPMENU_MAKE_LIST16 = auto()
    _BMPMENU_START = auto()
    _SEL_WIN_JUMP = auto()
    _BMPLIST_INIT = auto()
    _BMPLIST_INIT_EX = auto()
    _BMPLIST_MAKE_LIST = auto()
    _BMPLIST_START = auto()
    _BMPMENU_HV_START = auto()
    _SE_PLAY = auto()
    _SE_STOP = auto()
    _SE_WAIT = auto()
    _VOICE_PLAY = auto()
    _VOICE_WAIT = auto()
    _EASY_VOICE_MSG = auto()
    _ME_PLAY = auto()
    _ME_WAIT = auto()
    _SND_INITIAL_VOL_SET = auto()
    _BGM_PLAY = auto()
    _BGM_PLAY_CHECK = auto()
    _BGM_STOP = auto()
    _BGM_NOW_MAP_PLAY = auto()
    _BGM_SPECIAL_SET = auto()
    _BGM_SPECIAL_CLR = auto()
    _BGM_FADEOUT = auto()
    _BGM_FADEOUT_PLAY = auto()
    _BGM_FADEIN = auto()
    _BGM_PLAYER_PAUSE = auto()
    _PLAYER_FIELD_DEMO_BGM_PLAY = auto()
    _CTRL_BGM_FLAG_SET = auto()
    _CTRL_BGM_FLAG_RESET = auto()
    _PERAP_DATA_CHECK = auto()
    _PERAP_REC_START = auto()
    _PERAP_REC_STOP = auto()
    _PERAP_SAVE = auto()
    _SND_CLIMAX_DATA_LOAD = auto()
    _OBJ_ANIME = auto()
    _OBJ_ANIME_POS = auto()
    _ANIME_LABEL = auto()
    _ANIME_DATA = auto()
    _OBJ_ANIME_WAIT = auto()
    _TALK_OBJ_PAUSE_ALL = auto()
    _OBJ_PAUSE_ALL = auto()
    _OBJ_PAUSE_CLEAR_ALL = auto()
    _OBJ_PAUSE = auto()
    _OBJ_PAUSE_CLEAR = auto()
    _OBJ_ADD = auto()
    _OBJ_DEL = auto()
    _VANISH_DUMMY_OBJ_ADD = auto()
    _VANISH_DUMMY_OBJ_DEL = auto()
    _TURN_HERO_SITE = auto()
    _TALK_OBJ_START = auto()
    _TALK_OBJ_START_TURN_NOT = auto()
    _TALK_OBJ_END = auto()
    _TALK_START = auto()
    _EVENT_START = auto()
    _TALK_END = auto()
    _EVENT_END = auto()
    _PLAYER_POS_GET = auto()
    _OBJ_POS_GET = auto()
    _PLAYER_POS_OFFSET_SET = auto()
    _PLAYER_DIR_GET = auto()
    _NOT_ZONE_DEL_SET = auto()
    _MOVE_CODE_CHANGE = auto()
    _MOVE_CODE_GET = auto()
    _PAIR_OBJID_SET = auto()
    _EVENT_DATA = auto()
    _EVENT_DATA_END = auto()
    _SP_EVENT_DATA_END = auto()
    _SCENE_CHANGE_LABEL = auto()
    _SCENE_CHANGE_DATA = auto()
    _SCENE_CHANGE_END = auto()
    _FLAG_CHANGE_LABEL = auto()
    _OBJ_CHANGE_LABEL = auto()
    _INIT_CHANGE_LABEL = auto()
    _ADD_GOLD = auto()
    _SUB_GOLD = auto()
    _COMP_GOLD = auto()
    _GOLD_WIN_WRITE = auto()
    _GOLD_WIN_DEL = auto()
    _GOLD_WRITE = auto()
    _COIN_WIN_WRITE = auto()
    _COIN_WIN_DEL = auto()
    _COIN_WRITE = auto()
    _GET_COIN_NUM = auto()
    _ADD_COIN = auto()
    _SUB_COIN = auto()
    _FLD_ITEM_EVENT = auto()
    _HIDE_ITEM_EVENT = auto()
    _ADD_ITEM = auto()
    _SUB_ITEM = auto()
    _ADD_ITEM_CHK = auto()
    _ITEM_CHK = auto()
    _WAZA_ITEM_CHK = auto()
    _GET_POCKET_NO = auto()
    _CHECK_POCKET = auto()
    _ADD_BOX_ITEM = auto()
    _CHK_BOX_ITEM = auto()
    _ADD_GOODS = auto()
    _SUB_GOODS = auto()
    _ADD_GOODS_CHK = auto()
    _GOODS_CHK = auto()
    _ADD_TRAP = auto()
    _SUB_TRAP = auto()
    _ADD_TRAP_CHK = auto()
    _TRAP_CHK = auto()
    _ADD_TREASURE = auto()
    _SUB_TREASURE = auto()
    _ADD_TREASURE_CHK = auto()
    _TREASURE_CHK = auto()
    _ADD_TAMA = auto()
    _SUB_TAMA = auto()
    _ADD_TAMA_CHK = auto()
    _TAMA_CHK = auto()
    _CB_SEAL_KIND_NUM_GET = auto()
    _CB_ITEM_NUM_GET = auto()
    _CB_ITEM_NUM_ADD = auto()
    _UNKNOWN_FORM_GET = auto()
    _ADD_POKEMON = auto()
    _ADD_TAMAGO = auto()
    _CHG_POKE_WAZA = auto()
    _CHK_POKE_WAZA = auto()
    _CHK_POKE_WAZA_GROUP = auto()
    _APPROVE_POISON_DEAD = auto()
    _REVENGE_TRAINER_SEARCH = auto()
    _INIT_WEATHER = auto()
    _SET_WEATHER = auto()
    _UPDATE_WEATHER = auto()
    _GET_MAP_POS = auto()
    _GET_TEMOTI_POKE_NUM = auto()
    _SET_MAP_PROC = auto()
    _FINISH_MAP_PROC = auto()
    _WIFI_AUTO_REG = auto()
    _WIFI_P2P_MATCH_EVENT_CALL = auto()
    _WIFI_P2P_MATCH_SET_DEL = auto()
    _COMM_GET_CURRENT_ID = auto()
    _DENDOU_NUM_GET = auto()
    _POKE_WINDOW_PUT = auto()
    _POKE_WINDOW_PUT_PP = auto()
    _POKE_WINDOW_DEL = auto()
    _POKE_WINDOW_ANM = auto()
    _POKE_WINDOW_ANM_WAIT = auto()
    _BTL_SEARCHER_EVENT_CALL = auto()
    _BTL_SEARCHER_DIR_MV_SET = auto()
    _MSG_BOY_EVENT = auto()
    _IMAGE_CLIP_SET_PROC = auto()
    _IMAGE_CLIP_VIEW_TV_SET_PROC = auto()
    _IMAGE_CLIP_VIEW_CON_SET_PROC = auto()
    _CUSTOM_BALL_EVENT_CALL = auto()
    _TMAP_BG_SET_PROC = auto()
    _BOX_SET_PROC = auto()
    _OEKAKI_BOARD_SET_PROC = auto()
    _TR_CARD_SET_PROC = auto()
    _TRADE_LIST_SET_PROC = auto()
    _RECORD_CORNER_SET_PROC = auto()
    _DENDOU_SET_PROC = auto()
    _PC_DENDOU_SET_PROC = auto()
    _WORLDTRADE_SET_PROC = auto()
    _DPW_INIT_PROC = auto()
    _FIRST_POKE_SELECT_PROC = auto()
    _FIRST_POKE_SELECT_SET_AND_DEL = auto()
    _BAG_SET_PROC_NORMAL = auto()
    _BAG_SET_PROC_KINOMI = auto()
    _BAG_GET_RESULT = auto()
    _POKELIST_SET_PROC = auto()
    _NPC_TRADE_POKELIST_SET_PROC = auto()
    _UNION_POKELIST_SET_PROC = auto()
    _POKELIST_GET_RESULT = auto()
    _CON_POKELIST_SET_PROC = auto()
    _CON_POKELIST_GET_RESULT = auto()
    _CON_POKESTATUS_SET_PROC = auto()
    _POKESTATUS_GET_RESULT = auto()
    _WIFI_EARTH_SET_PROC = auto()
    _EYE_TRAINER_MOVE_SET = auto()
    _EYE_TRAINER_MOVE_CHECK = auto()
    _EYE_TRAINER_TYPE_GET = auto()
    _EYE_TRAINER_ID_GET = auto()
    _NAMEIN = auto()
    _NAMEIN_POKE = auto()
    _WIPE_FADE_START = auto()
    _WIPE_FADE_END_CHECK = auto()
    _WHITE_OUT = auto()
    _WHITE_IN = auto()
    _BLACK_OUT = auto()
    _BLACK_IN = auto()
    _MAP_CHANGE = auto()
    _MAP_CHANGE_NONE_FADE = auto()
    _COLOSSEUM_MAP_CHANGE_IN = auto()
    _COLOSSEUM_MAP_CHANGE_OUT = auto()
    _GET_BEFORE_ZONE_ID = auto()
    _GET_NOW_ZONE_ID = auto()
    _KABENOBORI = auto()
    _NAMINORI = auto()
    _BICYCLE_CHECK = auto()
    _BICYCLE_REQ = auto()
    _BICYCLE_REQ_NON_BGM = auto()
    _CYCLING_ROAD_SET = auto()
    _PLAYER_FORM_GET = auto()
    _PLAYER_REQ_BIT_ON = auto()
    _PLAYER_REQ_START = auto()
    _TAKINOBORI = auto()
    _SORAWOTOBU = auto()
    _HIDEN_FLASH = auto()
    _HIDEN_KIRIBARAI = auto()
    _CUTIN = auto()
    _CON_HERO_CHANGE = auto()
    _PLAYER_NAME = auto()
    _RIVAL_NAME = auto()
    _SUPPORT_NAME = auto()
    _POKEMON_NAME = auto()
    _ITEM_NAME = auto()
    _POCKET_NAME = auto()
    _ITEM_WAZA_NAME = auto()
    _WAZA_NAME = auto()
    _NUMBER_NAME = auto()
    _NUMBER_NAME_EX = auto()
    _BIRTH_DAY_CHECK = auto()
    _ANOON_SEE_NUM = auto()
    _NICK_NAME = auto()
    _POKETCH_NAME = auto()
    _TR_TYPE_NAME = auto()
    _MY_TR_TYPE_NAME = auto()
    _POKEMON_NAME_EXTRA = auto()
    _FIRST_POKEMON_NAME = auto()
    _RIVAL_POKEMON_NAME = auto()
    _SUPPORT_POKEMON_NAME = auto()
    _FIRST_POKE_NO_GET = auto()
    _NUTS_NAME = auto()
    _SEIKAKU_NAME = auto()
    _GOODS_NAME = auto()
    _TRAP_NAME = auto()
    _TAMA_NAME = auto()
    _ZONE_NAME = auto()
    _GENERATE_INFO_GET = auto()
    _TRAINER_ID_GET = auto()
    _TRAINER_BTL_SET = auto()
    _TRAINER_MULTI_BTL_SET = auto()
    _TRAINER_MSG_SET = auto()
    _TRAINER_TALK_TYPE_GET = auto()
    _REVENGE_TRAINER_TALK_TYPE_GET = auto()
    _TRAINER_TYPE_GET = auto()
    _TRAINER_BGM_SET = auto()
    _TRAINER_LOSE = auto()
    _TRAINER_LOSE_CHECK = auto()
    _NORMAL_LOSE = auto()
    _LOSE_CHECK = auto()
    _SEACRET_POKE_RETRY_CHECK = auto()
    _HAIFU_POKE_RETRY_CHECK = auto()
    _2VS2_BATTLE_CHECK = auto()
    _DEBUG_BTL_SET = auto()
    _DEBUG_TRAINER_FLAG_SET = auto()
    _DEBUG_TRAINER_FLAG_ON_JUMP = auto()
    _DEBUG_TR_TALK_BTL = auto()
    _SEL_PARENT_WIN = auto()
    _SEL_CHILD_WIN = auto()
    _DEBUG_PARENT_WIN = auto()
    _DEBUG_CHILD_WIN = auto()
    _DEBUG_SIO_ENCOUNT = auto()
    _DEBUG_SIO_CONTEST = auto()
    _CONSIO_TIMING_SEND = auto()
    _CONSIO_TIMING_CHECK = auto()
    _CON_SYSTEM_CREATE = auto()
    _CON_SYSTEM_EXIT = auto()
    _CON_JUDGE_NAME_GET = auto()
    _CON_BREEDER_NAME_GET = auto()
    _CON_NICK_NAME_GET = auto()
    _CON_NUM_TAG_SET = auto()
    _CON_SIO_PARAM_INIT_SET = auto()
    _CONTEST_PROC = auto()
    _CON_RANK_NAME_GET = auto()
    _CON_TYPE_NAME_GET = auto()
    _CON_VICTORY_BREEDER_NAME_GET = auto()
    _CON_VICTORY_ITEM_NO_GET = auto()
    _CON_VICTORY_NICK_NAME_GET = auto()
    _CON_RANKING_CHECK = auto()
    _CON_VICTORY_ENTRY_NO_GET = auto()
    _CON_MY_ENTRY_NO_GET = auto()
    _CON_OBJ_CODE_GET = auto()
    _CON_POPULARITY_GET = auto()
    _CON_DESK_MODE_GET = auto()
    _CON_HAVE_RIBBON_CHECK = auto()
    _CON_RIBBON_NAME_GET = auto()
    _CON_ACCE_NO_GET = auto()
    _CON_ENTRY_PARAM_GET = auto()
    _CON_CAMERA_FLASH_SET = auto()
    _CON_CAMERA_FLASH_CHECK = auto()
    _CON_HBLANK_STOP = auto()
    _CON_HBLANK_START = auto()
    _CON_ENDING_SKIP_CHECK = auto()
    _CON_RECORD_DISP = auto()
    _CON_MSGPRINT_FLAG_SET = auto()
    _CON_MSGPRINT_FLAG_RESET = auto()
    _SP_LOCATION_SET = auto()
    _ELEVATOR_FLOOR_GET = auto()
    _ELEVATOR_FLOOR_WRITE = auto()
    _SHINOU_ZUKAN_SEE_NUM = auto()
    _SHINOU_ZUKAN_GET_NUM = auto()
    _ZENKOKU_ZUKAN_SEE_NUM = auto()
    _ZENKOKU_ZUKAN_GET_NUM = auto()
    _CHK_ZENKOKU_ZUKAN = auto()
    _GET_HYOUKA_MSGID = auto()
    _WILD_BTL_SET = auto()
    _SP_WILD_BTL_SET = auto()
    _FIRST_BTL_SET = auto()
    _CAPTURE_BTL_SET = auto()
    _HONEY_TREE = auto()
    _GET_HONEY_TREE_STATE = auto()
    _HONEY_TREE_BTL_SET = auto()
    _HONEY_TREE_AFTER_SET = auto()
    _TSIGN_SET_PROC = auto()
    _REPORT_SAVE_CHECK = auto()
    _REPORT_SAVE = auto()
    _REPORT_WIN_OPEN = auto()
    _REPORT_WIN_CLOSE = auto()
    _CLIP_TVSAVEDATA_CHECK = auto()
    _CLIP_CONSAVEDATA_CHECK = auto()
    _CLIP_TV_TITLE_SAVE = auto()
    _GET_POKETCH = auto()
    _GET_POKETCH_FLAG = auto()
    _POKETCH_ADD = auto()
    _POKETCH_CHECK = auto()
    _COMM_SYNCHRONIZE = auto()
    _COMM_RESET = auto()
    _UNION_PARENT_CARD_TALK_NO = auto()
    _UNION_GET_INFO_TALK_NO = auto()
    _UNION_BEACON_CHANGE = auto()
    _UNION_CONNECT_TALK_DENIED = auto()
    _UNION_CONNECT_TALK_OK = auto()
    _UNION_TRAINER_NAME_REGIST = auto()
    _UNION_RETURN_SETUP = auto()
    _UNION_CONNECT_CUT_RESTART = auto()
    _UNION_GET_TALK_NUMBER = auto()
    _UNION_ID_SET = auto()
    _UNION_RESULT_GET = auto()
    _UNION_OBJ_ALL_VANISH = auto()
    _UNION_SCRIPT_RESULT_SET = auto()
    _UNION_PARENT_START_COMMAND_SET = auto()
    _UNION_CHILD_SELECT_COMMAND_SET = auto()
    _UNION_CONNECT_START = auto()
    _UNION_MAP_CHANGE = auto()
    _UNION_VIEW_TR_SEL_SET = auto()
    _UNION_VIEW_TR_TYPE_MSG_GET = auto()
    _UNION_VIEW_TR_TYPE_NO_GET = auto()
    _UNION_VIEW_MY_STATUS_SET = auto()
    _SYS_FLAG_ZUKAN_GET = auto()
    _SYS_FLAG_ZUKAN_SET = auto()
    _SYS_FLAG_SHOES_GET = auto()
    _SYS_FLAG_SHOES_SET = auto()
    _SYS_FLAG_BADGE_GET = auto()
    _SYS_FLAG_BADGE_SET = auto()
    _SYS_FLAG_BADGE_COUNT = auto()
    _SYS_FLAG_BAG_GET = auto()
    _SYS_FLAG_BAG_SET = auto()
    _SYS_FLAG_PAIR_GET = auto()
    _SYS_FLAG_PAIR_SET = auto()
    _SYS_FLAG_PAIR_RESET = auto()
    _SYS_FLAG_ONE_STEP_GET = auto()
    _SYS_FLAG_ONE_STEP_SET = auto()
    _SYS_FLAG_ONE_STEP_RESET = auto()
    _SYS_FLAG_GAME_CLEAR_GET = auto()
    _SYS_FLAG_GAME_CLEAR_SET = auto()
    _SYS_FLAG_KAIRIKI_SET = auto()
    _SYS_FLAG_KAIRIKI_RESET = auto()
    _SYS_FLAG_KAIRIKI_GET = auto()
    _SYS_FLAG_FLASH_SET = auto()
    _SYS_FLAG_FLASH_RESET = auto()
    _SYS_FLAG_FLASH_GET = auto()
    _SYS_FLAG_KIRIBARAI_SET = auto()
    _SYS_FLAG_KIRIBARAI_RESET = auto()
    _SYS_FLAG_KIRIBARAI_GET = auto()
    _SHOP_CALL = auto()
    _FIX_SHOP_CALL = auto()
    _FIX_GOODS_CALL = auto()
    _FIX_SEAL_CALL = auto()
    _ACCE_SHOP_CALL = auto()
    _PLAYER_REPORT_DRAW_SET = auto()
    _PLAYER_REPORT_DRAW_DEL = auto()
    _GAME_OVER_CALL = auto()
    _SET_WARP_ID = auto()
    _GET_MY_SEX = auto()
    _PC_KAIFUKU = auto()
    _UG_MAN_SHOP_NPC_RAND_PLACE = auto()
    _COMM_DIRECT_END = auto()
    _COMM_DIRECT_END_TIMING = auto()
    _COMM_DIRECT_ENTER_BTL_ROOM = auto()
    _COMM_PLAYER_SET_DIR = auto()
    _SET_UP_DOOR_ANIME = auto()
    _WAIT_3D_ANIME = auto()
    _FREE_3D_ANIME = auto()
    _SEQ_OPEN_DOOR = auto()
    _SEQ_CLOSE_DOOR = auto()
    _PMS_INPUT_SINGLE = auto()
    _PMS_INPUT_DOUBLE = auto()
    _PMS_BUF = auto()
    _GET_SEED_STATUS = auto()
    _GET_SEED_TYPE = auto()
    _GET_SEED_COMPOST = auto()
    _GET_SEED_GROUND = auto()
    _GET_SEED_COUNT = auto()
    _SET_SEED_COMPOST = auto()
    _SET_SEED_NUTS = auto()
    _SET_SEED_WATER = auto()
    _TAKE_SEED = auto()
    _SXY_POS_CHANGE = auto()
    _OBJ_POS_CHANGE = auto()
    _SXY_MV_CHANGE = auto()
    _SXY_DIR_CHANGE = auto()
    _SXY_EXIT_POS_CHANGE = auto()
    _SXY_BG_POS_CHANGE = auto()
    _OBJ_DIR_CHANGE = auto()
    _RETURN_SCRIPT_WK_SET = auto()
    _MSGEXPANDBUF = auto()
    _GET_SODATE_NAME = auto()
    _GET_SODATEYA_ZIISAN = auto()
    _INIT_WATER_GYM = auto()
    _PUSH_WATER_GYM_BUTTON = auto()
    _INIT_GHOST_GYM = auto()
    _MOVE_GHOST_GYM_LIFT = auto()
    _INIT_STEEL_GYM = auto()
    _INIT_COMBAT_GYM = auto()
    _INIT_ELEC_GYM = auto()
    _ROTATE_ELEC_GYM_GEAR = auto()
    _GET_POKE_COUNT = auto()
    _GET_POKE_COUNT2 = auto()
    _GET_POKE_COUNT3 = auto()
    _GET_POKE_COUNT4 = auto()
    _GET_TAMAGO_COUNT = auto()
    _UG_SHOP_MENU_INIT = auto()
    _UG_SHOP_TALK_START = auto()
    _UG_SHOP_TALK_END = auto()
    _UG_SHOP_ITEM_NAME = auto()
    _UG_SHOP_TRAP_NAME = auto()
    _DEL_SODATEYA_EGG = auto()
    _GET_SODATEYA_EGG = auto()
    _MSG_SODATEYA_AISHOU = auto()
    _MSG_AZUKE_SET = auto()
    _SET_SODATEYA_POKE = auto()
    _SODATEYA_POKELIST = auto()
    _HIKITORI_LIST = auto()
    _SODATE_POKE_LEVEL_STR = auto()
    _HIKITORI_RYOUKIN = auto()
    _HIKITORI_POKE = auto()
    _TAMAGO_DEMO = auto()
    _TEMOTI_MONSNO = auto()
    _MONS_OWN_CHK = auto()
    _CHK_TEMOTI_POKERUS = auto()
    _TEMOTI_POKE_SEX_GET = auto()
    _SUB_MY_GOLD = auto()
    _COMP_MY_GOLD = auto()
    _OBJ_VISIBLE = auto()
    _OBJ_INVISIBLE = auto()
    _MAILBOX = auto()
    _GET_MAILBOX_DATANUM = auto()
    _RANKING_VIEW = auto()
    _GET_TIME_ZONE = auto()
    _GET_RND = auto()
    _GET_RND_NEXT = auto()
    _GET_NATSUKI = auto()
    _ADD_NATSUKI = auto()
    _SUB_NATSUKI = auto()
    _HIKITORI_LIST_NAME_SET = auto()
    _GET_SODATEYA_AISHOU = auto()
    _SODATEYA_TAMAGO_CHK = auto()
    _TEMOTI_POKE_CHK = auto()
    _OOKISA_RECORD_CHK = auto()
    _OOKISA_RECORD_SET = auto()
    _OOKISA_TEMOTI_SET_BUF = auto()
    _OOKISA_KIROKU_SET_BUF = auto()
    _OOKISA_KURABE_INIT = auto()
    _WAZALIST_SET_PROC = auto()
    _WAZALIST_GET_RESULT = auto()
    _WAZA_COUNT = auto()
    _WAZA_DEL = auto()
    _TEMOTI_WAZANO = auto()
    _TEMOTI_WAZA_NAME = auto()
    _FNOTE_START_SET = auto()
    _FNOTE_DATA_MAKE = auto()
    _FNOTE_DATA_SAVE = auto()
    _IMC_ACCE_ADD_ITEM = auto()
    _IMC_ACCE_ADD_ITEM_CHK = auto()
    _IMC_ACCE_ITEM_CHK = auto()
    _IMC_BG_ADD_ITEM = auto()
    _IMC_BG_ITEM_CHK = auto()
    _NUTMIXER_CALL = auto()
    _NUTMIXER_PLAY_CHECK = auto()
    _ZUKAN_CHK_SHINOU = auto()
    _ZUKAN_CHK_NATIONAL = auto()
    _ZUKAN_RECONGNIZE_SHINOU = auto()
    _ZUKAN_RECONGNIZE_NATIONAL = auto()
    _URAYAMA_ENCOUNT_SET = auto()
    _URAYAMA_ENCOUNT_NO_CHK = auto()
    _POKE_MAIL_CHK = auto()
    _PAPERPLANE_SET = auto()
    _POKE_MAIL_DEL = auto()
    _KASEKI_COUNT = auto()
    _ITEMLIST_SET_PROC = auto()
    _ITEMLIST_GET_RESULT = auto()
    _ITEMNO_TO_MONSNO = auto()
    _KASEKI_ITEMNO = auto()
    _POKE_LEVEL_CHK = auto()
    _BTOWER_APP_CALL = auto()
    _BTOWER_WORK_CLEAR = auto()
    _BTOWER_WORK_INIT = auto()
    _BTOWER_WORK_RELEASE = auto()
    _BTOWER_TOOLS = auto()
    _BTOWER_SEVEN_POKE_GET = auto()
    _BTOWER_PRIZE_GET = auto()
    _BTOWER_PRIZEMAN_SET = auto()
    _BTOWER_SEND_BUF = auto()
    _BTOWER_RECV_BUF = auto()
    _BTOWER_GET_LEADER_ROOMID = auto()
    _BTOWER_IS_LEADER_EXIST = auto()
    _RECORD_INC = auto()
    _RECORD_GET = auto()
    _RECORD_ADD = auto()
    _RECORD_SET = auto()
    _RECORD_SETIFLARGE = auto()
    _SAFARI_START = auto()
    _SAFARI_END = auto()
    _CALL_SAFARI_SCOPE = auto()
    _CLIMAX_DEMO = auto()
    _INIT_SAFARI_TRAIN = auto()
    _MOVE_SAFARI_TRAIN = auto()
    _CHECK_SAFARI_TRAIN = auto()
    _PLAYER_HEGIHT_VALID = auto()
    _GET_POKE_SEIKAKU = auto()
    _CHK_POKE_SEIKAKU_ALL = auto()
    _UNDERGROUND_TALK_COUNT = auto()
    _NATURAL_PARK_WALK_COUNT_CLEAR = auto()
    _NATURAL_PARK_WALK_COUNT_GET = auto()
    _NATURAL_PARK_ACCESSORY_NO_GET = auto()
    _GET_NEWS_POKE_NO = auto()
    _NEWS_COUNT_SET = auto()
    _NEWS_COUNT_CHK = auto()
    _START_GENERATE = auto()
    _ADD_MOVE_POKE = auto()
    _OSHIE_WAZA_COUNT = auto()
    _REMAIND_WAZA_COUNT = auto()
    _OSHIE_WAZALIST_SET_PROC = auto()
    _REMAIND_WAZALIST_SET_PROC = auto()
    _OSHIE_WAZALIST_GET_RESULT = auto()
    _REMAIND_WAZALIST_GET_RESULT = auto()
    _NORMAL_WAZALIST_SET_PROC = auto()
    _NORMAL_WAZALIST_GET_RESULT = auto()
    _FLD_TRADE_ALLOC = auto()
    _FLD_TRADE_MONSNO = auto()
    _FLD_TRADE_CHG_MONSNO = auto()
    _FLD_TRADE_EVENT = auto()
    _FLD_TRADE_DEL = auto()
    _ZUKAN_TEXT_VER_UP = auto()
    _ZUKAN_SEX_VER_UP = auto()
    _ZENKOKU_ZUKAN_FLAG = auto()
    _CHK_RIBBON_COUNT = auto()
    _CHK_RIBBON_COUNT_ALL = auto()
    _CHK_RIBBON = auto()
    _SET_RIBBON = auto()
    _RIBBON_NAME = auto()
    _CHK_PRMEXP = auto()
    _CHK_WEEK = auto()
    _TV_ENTRY_WATCH_HIDE_ITEM = auto()
    _TV_ENTRY_WATCH_CHANGE_NAME = auto()
    _REGULATION_LIST_CALL = auto()
    _ASHIATO_CHK = auto()
    _PC_RECOVER_ANM = auto()
    _ELEVATOR_ANM = auto()
    _CALL_SHIP_DEMO = auto()
    _DEBUG_PRINT_WORK = auto()
    _DEBUG_PRINT_FLAG = auto()
    _DEBUG_PRINT_WORK_STATIONED = auto()
    _DEBUG_PRINT_FLAG_STATIONED = auto()
    _PM_VERSION_GET = auto()
    _FRONT_POKEMON = auto()
    _TEMOTI_POKE_TYPE = auto()
    _AIKOTOBA_KABEGAMI_SET = auto()
    _GET_UG_HATA_NUM = auto()
    _SETUP_PASO_ANM = auto()
    _START_PASO_ON_ANM = auto()
    _START_PASO_OFF_ANM = auto()
    _GET_KUJI_ATARI_NUM = auto()
    _KUJI_ATARI_CHK = auto()
    _KUJI_ATARI_INIT = auto()
    _NICK_NAME_PC = auto()
    _TV_INTERVIEWER_CHECK = auto()
    _COUNT_MONSBOX_SPACE = auto()
    _POKEPARK_CONTROL = auto()
    _POKEPARK_DEPOSIT_COUNT = auto()
    _POKEPARK_TRANS_MONS = auto()
    _POKEPARK_GET_SCORE = auto()
    _DENDOU_BALL_ANM = auto()
    _INIT_FLD_LIFT = auto()
    _MOVE_FLD_LIFT = auto()
    _CHECK_FLD_LIFT = auto()
    _SETUP_RAH_CYL = auto()
    _START_RAH_CYL = auto()
    _ADD_SCORE = auto()
    _ACCE_NAME = auto()
    _PARTY_MONSNO_CHECK = auto()
    _PARTY_DEOKISISUFORM_CHANGE = auto()
    _CHECKMINOMUCHICOMP = auto()
    _POKETCH_HOOK_SET = auto()
    _POKETCH_HOOK_RESET = auto()
    _SLOT_MACHINE = auto()
    _GET_NOW_HOUR = auto()
    _FLDOBJ_SHAKE_ANM = auto()
    _FLDOBJ_BLINK_ANM = auto()
    _D20R0106_LEGEND_IS_UNSEAL = auto()
    _DRESSING_IMC_ACCE_CHECK = auto()
    _AGB_CARTRIDGE_VER_GET = auto()
    _UNDERGROUND_TALK_COUNT_CLEAR = auto()
    _HIDEMAP_STATE_CHG = auto()
    _NAMEIN_MONUMENT = auto()
    _MONUMENT_NAME = auto()
    _IMC_BG_NAME = auto()
    _COMP_COIN = auto()
    _SLOT_RENTYAN_CHK = auto()
    _ADD_COIN_CHK = auto()
    _LEVEL_JIJII_NO = auto()
    _POKE_LEVEL_GET = auto()
    _IMC_ACCE_SUB_ITEM = auto()
    _C08R0801SCOPECAMERASET = auto()
    _LEVEL_JIJII_INIT = auto()
    _NEW_NANKAI_WORD_SET = auto()
    _REGULAR_CHECK = auto()
    _NEW_NANKAI_WORD_COMPLETE_CHECK = auto()
    _TEMOTI_POKE_CONTEST_STATUS_GET = auto()
    _D17SYSTEM_MAP_SELECT = auto()
    _UNDERGROUND_TOOL_GIVE_COUNT = auto()
    _UNDERGROUND_KASEKI_DIG_COUNT = auto()
    _UNDERGROUND_TRAP_HIT_COUNT = auto()
    _POFIN_ADD = auto()
    _POFIN_ADD_CHK = auto()
    _IS_HAIHU_EVENT_ENABLE = auto()
    _SODATEYA_POKELIST_SET_PROC = auto()
    _SODATEYA_POKELIST_GET_RESULT = auto()
    _GET_RANDOM_HIT = auto()
    _UNDERGROUND_TALK_COUNT2 = auto()
    _HIDENEFF_START = auto()
    _ZISHIN = auto()
    _BTL_POINT_WIN_WRITE = auto()
    _BTL_POINT_WIN_DEL = auto()
    _BTL_POINT_WRITE = auto()
    _GET_BTL_POINT = auto()
    _BTL_POINT_ADD = auto()
    _BTL_POINT_SUB = auto()
    _COMP_BTL_POINT = auto()
    _GET_BP_GIFT = auto()
    _UG_BALLITEM_CHECK = auto()
    _AUSU_ITEM_CHECK = auto()
    _CHECK_MY_GSID = auto()
    _FRIEND_DATA_NUM = auto()
    _GET_COIN_GIFT = auto()
    _SUB_WK_COIN = auto()
    _COMP_WK_COIN = auto()
    _AIKOTOBA_OKURIMONO_CHK = auto()
    _WIFI_HUSIGINAOKURIMONO_OPEN_FLAG_SET = auto()
    _UNION_GET_CARD_TALK_NO = auto()
    _WIRELESS_ICON_EASY = auto()
    _WIRELESS_ICON_EASY_END = auto()
    _SAVE_FIELD_OBJ = auto()
    _SEAL_NAME = auto()
    _SET_ESCAPE_LOCATION = auto()
    _FIELDOBJ_BITSET_FELLOWHIT = auto()
    _DAME_TAMAGO_CHK_ALL = auto()
    _UNION_BMPMENU_START = auto()
    _UNION_BATTLE_START_CHECK = auto()
    _GET_TRCARD_RANK = auto()
    _FLD_SCOPE_MODE_ON = auto()
    _FLD_SCOPE_MODE_OFF = auto()
    _AC_UP = auto()
    _AC_DOWN = auto()
    _AC_LEFT = auto()
    _AC_RIGHT = auto()
    _AC_LOOP = auto()
    _AC_DIR_U = auto()
    _AC_DIR_R = auto()
    _AC_DIR_D = auto()
    _AC_DIR_L = auto()
    _ACMD_END = auto()
    _AC_DIR_VAL = auto()
    _AC_WAIT = auto()
    _SET_TURN_HERO_FRAME = auto()
    _SET_TURN_OBJ_FRAME = auto()
    _DEBUG_PRINT = auto()
    _AC_MARK_GYOE = auto()
    _FADE_WAIT = auto()
    _HERO_MOVE_GRID_CENTER = auto()
    _AC_WORLD_X = auto()
    _AC_WORLD_Z = auto()
    _AC_HERO_MATCH_X = auto()
    _AC_HERO_MATCH_Z = auto()
    _SET_POS_HERO_MATCH_X = auto()
    _SET_POS_HERO_MATCH_Z = auto()
    _AC_UP_CENTER = auto()
    _AC_DOWN_CENTER = auto()
    _AC_LEFT_CENTER = auto()
    _AC_RIGHT_CENTER = auto()
    _AC_DIR_UP_CENTER = auto()
    _AC_DIR_DOWN_CENTER = auto()
    _AC_DIR_LEFT_CENTER = auto()
    _AC_DIR_RIGHT_CENTER = auto()
    _AC_VANISH_ON = auto()
    _AC_VANISH_OFF = auto()
    _AC_DIR_PAUSE_ON = auto()
    _AC_DIR_PAUSE_OFF = auto()
    _AC_ANM_PAUSE_ON = auto()
    _AC_ANM_PAUSE_OFF = auto()
    _AC_PC_BOW = auto()
    _AC_HIDE_PULLOFF = auto()
    _AC_HERO_BANZAI = auto()
    _AC_MARK_SAISEN = auto()
    _AC_HERO_BANZAI_UKE = auto()
    _ACMD_NOT = auto()
    _GET_LANGUAGE = auto()
    _GET_REL_POS_HERO = auto()
    _CAMERA_TARGET_HERO = auto()
    _CAMERA_TARGET_DUMMY = auto()
    _DUMMY_ANIME = auto()
    _DUMMY_ANIME_WAIT = auto()
    _DUMMY_SET_POS = auto()
    _DUMMY_SET_POS_HERO = auto()
    _SET_CUSTUM_WIN_MSBT = auto()
    _ADD_CUSTUM_WIN_LABEL = auto()
    _OPEN_CUSTUM_WIN = auto()
    _VISIBLE_OBJ_PROP = auto()
    _INVISIBLE_OBJ_PROP = auto()
    _EVENT_CAMERA_MODE = auto()
    _SET_EVENT_CAMERA_PARAM = auto()
    _EVENT_CAMERA_WAIT = auto()
    _EVENT_CAMERA_FRAME = auto()
    _HIT_DOOR_ANIME = auto()
    _HIT_DOOR_ANIME_WAIT = auto()
    _SET_DOOR_OBJ = auto()
    _ROTOMU_FORM_CHECK = auto()
    _TEMOTI_ROTOMU_FORM_WAZA_CHG = auto()
    _EVENT_GET_TEMOTI_POKE_CHK_GET_POS = auto()
    _TURN_HERO_TALK_OBJ = auto()
    _FADE_SPEED = auto()
    _FADE_BALL = auto()
    _FADE_DEFAULT = auto()
    _DOOR_FORCE_ANIME_END = auto()
    _LDVAL_VERSION = auto()
    _LDVAL_SEX = auto()
    _TV_ENTRY_PARKINFO_INIT = auto()
    _TV_ENTRY_PARKINFO_ITEM = auto()
    _TV_ENTRY_PARKINFO_ACCE = auto()
    _GROUP_EXIST_CHECK = auto()
    _GROUP_ENTRY_CHECK = auto()
    _GROUP_NAME = auto()
    _GROUP_LEADER_NAME = auto()
    _GROUP_NAME_IN = auto()
    _GROUP_ENTRY = auto()
    _GROUP_MAKE = auto()
    _MYSTERY_POSTMAN_INIT = auto()
    _MYSTERY_PRESENT_CHECK = auto()
    _MYSTERY_GET_PRESENT_ID = auto()
    _MYSTERY_RECEIVE_CHECK = auto()
    _MYSTERY_RECEIVE_PRESENT = auto()
    _MYSTERY_DISABLE_MSG = auto()
    _MYSTERY_ENABLE_MSG = auto()
    _MYSTERY_POSTMAN_END = auto()
    _MYSTERY_POSTMAN_SAVE_END = auto()
    _UNKNOWN_MSG = auto()
    _TV_INTERVIEW_MSG = auto()
    _TV_INTERVIEW_ENTRY = auto()
    _TV_START = auto()
    _TV_END = auto()
    _TV_START_NUMBER = auto()
    _TV_SET_ENDFLAG = auto()
    _TV_MAKE_MSG = auto()
    _TV_GET_DATA_TOTAL = auto()
    _AC_INDEX_ANIME = auto()
    _AC_INDEX_ANIME_WAIT = auto()
    _DEBUG_RESET_WORK = auto()
    _SET_SYS_FLAG = auto()
    _RESET_SYS_FLAG = auto()
    _CAMERA_SET_COS_ANGLE = auto()
    _CAMERA_COS_ANGLE_WAIT = auto()
    _HERO_MOVE_GRID_CENTER_FRONT = auto()
    _WARP_ENABLE_SET = auto()
    _DOOR_ENABLE_SET = auto()
    _AC_ANIM_LOCK = auto()
    _AC_ANIM_RELEASE = auto()
    _SET_OFFSET = auto()
    _OFFSET_WAIT = auto()
    _NAMINORI_END = auto()
    _TAKIKUDARI = auto()
    _KABENOBORI_CHECK = auto()
    _TALK_POKE_GET_TEMOTI_INDEX = auto()
    _NATURAL_PARK_GET_MONOHIROI_ITEM_NO = auto()
    _CON_OPEN_POKE_SELECT_MENU = auto()
    _CON_OPEN_CAPSULE_SELECT_MENU = auto()
    _CON_OPEN_BOUTIQUE_SELECT_MENU = auto()
    _CON_WAIT_CONTEST_MENU = auto()
    _CON_MY_ENTRY_NO_WORD_SET = auto()
    _CON_BEST_PERFORMER_CHECK = auto()
    _CON_CATEGORY_RIBBON_NAME_SET = auto()
    _CON_HAVE_CONTEST_STAR_CHECK = auto()
    _CON_CONTEST_STAR_NAME_SET = auto()
    _CON_REWARD_NAME_SET = auto()
    _OBJ_ANIME_FUREAI = auto()
    _AC_MARK_EMO = auto()
    _CON_CATEGORY_AND_RANK_SET = auto()
    _CON_RANK_SET = auto()
    _NATURAL_PARK_POKE_CREATE = auto()
    _NATURAL_PARK_POKE_KAISAN = auto()
    _NATURAL_PARK_POKE_SYUUGOU = auto()
    _CON_CHECK_ENTRY_POKE = auto()
    _NATURAL_PARK_POKE_SELECT_MENU = auto()
    _AC_NECK_ROTATE = auto()
    _CON_RESET_PARAMETER = auto()
    _CON_SELECT_SINGLE_MODE = auto()
    _CON_SELECT_MULTI_MODE = auto()
    _DPR_SHOP_OPEN = auto()
    _DPR_SHOP_OPEN_WAIT = auto()
    _DOOR_TRANSITION_ZONE_SET = auto()
    _IMAGE_CLIP_VIEW_CON_CHECK_PROC = auto()
    _MOVE_COMBAT_GYM_WALL = auto()
    _EV_ENTITY_PLAYER_MOVE_START = auto()
    _EV_ENTITY_PLAYER_MOVE_END = auto()
    _EV_ENTITY_PLAYER_MOVE_RESET = auto()
    _CHECK_CAN_SEED_WATER = auto()
    _SHOP_OPEN_FIXED = auto()
    _SHOP_OPEN_SEAL = auto()
    _SHOP_OPEN_BATTLE = auto()
    _SHOP_OPEN_FLOWER = auto()
    _SHOP_OPEN_OTENKI = auto()
    _SHOP_OPEN_SELL = auto()
    _AC_OFFSET = auto()
    _GET_COSTUME = auto()
    _SHOP_OPEN_BOUTIQUE_BUY = auto()
    _SHOP_OPEN_BOUTIQUE_CHANGE = auto()
    _CON_REWARD_SHOWMASTER_NAME_SET = auto()
    _CON_TWINKLE_STAR_NAME_SET = auto()
    _ANAWOHORU = auto()
    _ANANUKENOHIMO = auto()
    _TELEPORT = auto()
    _AMAIKAORI = auto()
    _CHECK_POFIN = auto()
    _AMAIMITU = auto()
    _WARP_START_ANIMATION = auto()
    _WARP_END_ANIMATION = auto()
    _SAFARI_SCOPE_SEQUENCE = auto()
    _EVENT_CAMERA_INDEX = auto()
    _EVENT_CAMERA_END_WAIT = auto()
    _SHOP_OPEN_PALPARK = auto()
    _BTOWER_APP_WAIT = auto()
    _FLOOR_OPEN = auto()
    _FLOOR_CLOSE = auto()
    _MONEY_OPEN = auto()
    _MONEY_CLOSE = auto()
    _AZUKARIYA_EXIST_EGG = auto()
    _AZUKARIYA_STORED_COUNT = auto()
    _AZUKARIYA_SET_STORED_NAME = auto()
    _AZUKARIYA_STORE = auto()
    _AZUKARIYA_RESTORE = auto()
    _AZUKARIYA_LOVE_LEVEL = auto()
    _AZUKARIYA_GET_STORED_MONSNO = auto()
    _AZUKARIYA_GET_EGG = auto()
    _AZUKARIYA_DISCARD_EGG = auto()
    _AZUKARIYA_SET_STORED_INFO_STR = auto()
    _AZUKARIYA_GET_STORED_SEX = auto()
    _AZUKARIYA_OLDMAN_INIT = auto()
    _ADD_CUSTUM_WIN_LABEL_WORD_SET = auto()
    _OPEN_CUSTUM_WIN_WORD_SET = auto()
    _AC_INVISIBLE_ON = auto()
    _AC_INVISIBLE_OFF = auto()
    _BTL_ENCSEQ_LOAD = auto()
    _USE_SPRAY = auto()
    _BIRTH_MOUNTH_INPUT = auto()
    _BIRTH_DAY_INPUT = auto()
    _SPEAKERS_NAME = auto()
    _GET_PLAYER_CAP = auto()
    _CAMERA_SHAKE = auto()
    _EVENT_ENTITY_CLIP_PLAY = auto()
    _EVENT_ENTITY_CLIP_WAIT = auto()
    _FACE_INDEX = auto()
    _AC_FACE_INDEX = auto()
    _TEMOTI_BALL_LOAD = auto()
    _TEMOTI_BALL_LOAD_WAIT = auto()
    _POKECEN_PUT_BALL = auto()
    _POKECEN_CLEAR_BALL = auto()
    _CHARA_LOOK_LOCK = auto()
    _CHARA_LOOK_RELEASE = auto()
    _TALK_OBJ_START_LOOK_NONE = auto()
    _BOUKENNOOTO_TIPS_OPEN = auto()
    _HIDENEFF_WAIT = auto()
    _GET_URAYAMA_ENCOUNT_INDEX = auto()
    _CUSTOM_BALL_NUM_ADD = auto()
    _CHANGE_FASHION_REQ = auto()
    _WARP_PANEL_START = auto()
    _WARP_PANEL_END = auto()
    _CON_OPEN_MATCHING_MENU = auto()
    _OPEN_PASSWORD_SWKEYBOARD = auto()
    _DENDOU_NUM_SET = auto()
    _TEMOTI_BOX_POKE_CHK = auto()
    _TEMOTI_BOX_MONSNO = auto()
    _CALL_WAZA_OMOIDASHI_UI = auto()
    _CALL_WAZA_WASURE_UI = auto()
    _CALL_WAZA_OSHIE_UI = auto()
    _CHECK_WAZA_OSHIE = auto()
    _CHECK_WAZA_OSHIE_ALL = auto()
    _TEMOTI_BOX_POKEMON_NAME = auto()
    _BTWR_TOOL_CHK_ENTRY_POKE_NUM = auto()
    _BTWR_TOOL_CLEAR_PLAY_DATA = auto()
    _BTWR_TOOL_PUSH_NOW_LOCATION = auto()
    _BTWR_TOOL_POP_NOW_LOCATION = auto()
    _BTWR_TOOL_GET_WIFI_RANK = auto()
    _BTWR_TOOL_SET_PLAY_MODE = auto()
    _BTWR_TOOL_SET_NOW_WIN = auto()
    _BTWR_TOOL_SET_RANK = auto()
    _BTWR_SUB_CHK_ENTRY_POKE = auto()
    _BTWR_SUB_GET_NOW_ROUND = auto()
    _BTWR_SUB_INC_ROUND = auto()
    _BTWR_SUB_IS_CLEAR = auto()
    _BTWR_SUB_GET_RENSHOU_CNT = auto()
    _BTWR_SUB_SET_SCORE = auto()
    _BTWR_SUB_CHOICE_BTL_PARTNER = auto()
    _BTWR_SUB_LOCAL_BTL_CALL = auto()
    _BTWR_SUB_GET_PLAY_MODE = auto()
    _BTWR_SUB_SET_LEADER_CLEAR_FLAG = auto()
    _BTWR_SUB_GET_LEADER_CLEAR_FLAG = auto()
    _BTWR_SUB_ADD_BATTLE_POINT = auto()
    _BTWR_SUB_RENSHOU_RIBBON_SET = auto()
    _BTWR_SUB_GET_MINE_OBJ = auto()
    _BTWR_SUB_UPDATE_RANDOM = auto()
    _BTWR_DEB_IS_WORK_NULL = auto()
    _BOUKENNOOTO_TIPS_WAIT = auto()
    _SAVE_RENDOU_ENABLE = auto()
    _RETURN_LOOP = auto()
    _INPUT_JUMP = auto()
    _BTWR_SUB_BTL_TRAINER_SET = auto()
    _BTWR_SUB_GET_RANK = auto()
    _BTWR_SUB_RANK_DOWN_LOSE = auto()
    _BTWR_SUB_RANK_DOWN_LOSE_RESET = auto()
    _BTWR_SUB_ADD_LOSE = auto()
    _SET_VISIBILITY = auto()
    _LOAD_CAMERA_CONTROLLER = auto()
    _LOAD_WAIT_CAMERA_CONTROLLER = auto()
    _CAMERA_CONTROLLER_PLAY = auto()
    _CAMERA_CONTROLLER_END = auto()
    _TEMOTI_ROTOMU_FORM_CHG_CHECK = auto()
    _TEMOTI_POKE_CHK_NUM = auto()
    _TEMOTI_ROTOMU_FORM_GET = auto()
    _POKELIST_FORM_CHANGE_SET_PROC = auto()
    _POKELIST_FORM_CHANGE_GET_RESULT = auto()
    _TUREARUKI_POKEMON_TALK = auto()
    _TUREARUKI_POKEMON_INDEX = auto()
    _TUREARUKI_TAKE_ITEM = auto()
    _TUREARUKI_ITEM_TIMER_SET = auto()
    _RELEASE_CAMERA_CONTROLLER = auto()
    _FIND_BG_ENABLE = auto()
    _FIND_BG_DISABLE = auto()
    _CALL_EFFECT = auto()
    _STOP_EFFECT = auto()
    _RELEASE_EFFECT = auto()
    _CASSET_VERSION_GET = auto()
    _BOX_OPEN_NORMAL = auto()
    _BOX_OPEN_SELECT = auto()
    _CALL_EFFECT_OBJ = auto()
    _SORAWOTOBU_END = auto()
    _CON_OPEN_RESUME_MATCHING_MENU = auto()
    _BOX_SEAL_UI_WAIT = auto()
    _OBJ_POS_CHANGE_WORLD = auto()
    _OPEN_SPECIAL_WIN_LABEL = auto()
    _WAIT_SPECIAL_WIN_LABEL = auto()
    _AK_LISNER_TRA = auto()
    _AK_LISNER_POS = auto()
    _AK_LISNER_ROT = auto()
    _UNION_PROC = auto()
    _CAMERA_CONTROLLER_WAIT = auto()
    _SET_TV_INT = auto()
    _SET_TV_PLAYER_NAME = auto()
    _SET_TV_POKE_NICK_NAME = auto()
    _TV_TPIC_ENABLE = auto()
    _TV_TPIC_BRANCH = auto()
    _TUREARUKI_POKE_CREATE = auto()
    _TUREARUKI_POKE_DELETE = auto()
    _AUTO_TANKEN_SET = auto()
    _SET_MATCHING_GROUP = auto()
    _AUTO_TANKEN_SET_WAIT = auto()
    _USE_TANKENSET = auto()
    _TALK_UNION_NPC = auto()
    _CHECK_ONLINE_ACCOUNT = auto()
    _WAIT_CHECK_ONLINE_ACCOUNT = auto()
    _LOCALKOUKAN_APPLY = auto()
    _ZUKAN_TOUROKU = auto()
    _ZUKAN_TOUROKU_WAIT = auto()
    _CHK_ZUKAN_TOUROKU = auto()
    _AUTO_SAVE = auto()
    _ENDING_DEMO = auto()
    _AZUKARIYA_TAKE_OVER_POKE = auto()
    _POKETORE_GET_CHARGE = auto()
    _POKETORE_START = auto()
    _BICYCLE_COLOR_SET = auto()
    _BICYCLE_COLOR_GET = auto()
    _PARK_ITEM_NAME = auto()
    _LOAD_UMA_ANIME = auto()
    _RELEASE_UMA_ANIME = auto()
    _LOAD_UMA_ANIME_WAIT = auto()
    _UMA_ANIME_PLAY = auto()
    _UMA_ANIME_ATTACH = auto()
    _UMA_PLAY_WAIT = auto()
    _OBJ_ANIME_SPEED = auto()
    _OBJ_SCALE = auto()
    _BADGE_GET = auto()
    _ADD_UG_ITEM = auto()
    _TOBARI_4F_SHOP_OPEN = auto()
    _DOF_FAR_DEPTH = auto()
    _DISPLAY_MESSAGE = auto()
    _DISPLAY_MESSAGE_CLOSE = auto()
    _CUSTOM_BALL_TRAINER_PAGE = auto()
    _CUSTOM_BALL_TRAINER_COPY_OPEN = auto()
    _RECONGNIZE_TOKIKAKE = auto()
    _RECONGNIZE_OPEN_WAIT = auto()
    _UG_ITEM_NAME = auto()
    _FUREAI_TALK_START = auto()
    _FUREAI_TALK_END = auto()
    _PLAY_FUREAI_VOICE_NAKAYOSHIRANK = auto()
    _CREATE_HYOUTA = auto()
    _CALL_SHIP_DEMO_SEA_MAP = auto()
    _SETUP_SHIP = auto()
    _PC_DENDOU_SET_PROC_OPEN_WAIT = auto()
    _GET_POKETCH_APP_ID = auto()
    _FADE_DUNGEON_OUT = auto()
    _FADE_DUNGEON_IN = auto()
    _FADE_BUILDING_OUT = auto()
    _FADE_BUILDING_IN = auto()
    _FADE_AREA_OUT = auto()
    _FADE_AREA_IN = auto()
    _CUSTOM_BALL_TRAINER_PAGE_WAIT = auto()
    _C08R0801SCOPECAMERA_SEQUENCE = auto()
    _EMBANKMENT = auto()
    _ENTRY_UWASA_ZUKAN = auto()
    _TALK_UG_NPC = auto()
    _TRAINING_OPEN = auto()
    _TRAINING_OPEN_WAIT = auto()
    _CAMERA_CONTROLLER_IS_NULL = auto()
    _UMA_IS_NULL = auto()
    _GET_IS_HAVE_SECRETBASE = auto()
    _GET_UG_NPC_TALK_COUNT = auto()
    _RESET_UG_NPC_TALK_COUNT = auto()
    _TEMOTI_POKE_CHK_GET_POS = auto()
    _AC_STOP_WALK_ANIME = auto()
    _SET_FORCE_BLINK = auto()
    _CHECK_SECRET_BASE_EXPANTION = auto()
    _TV_TOPIC_BRANCH_GET = auto()
    _TV_TOPIC_INT_GET = auto()
    _TV_TOPIC_STR_WORD_SET = auto()
    _OOKISA_VALUE_SET_BUF = auto()
    _SET_LIGHTINTENSITY = auto()
    _SET_LIGHTINTENSITY_CHARCTER = auto()
    _SET_LIGHTINTENSITY_POKE = auto()
    _END_LIGHTINTENSITY = auto()
    _END_LIGHTINTENSITY_CHARCTER = auto()
    _END_LIGHTINTENSITY_POKE = auto()
    _AC_ANIME_DURATION = auto()
    _TV_RED_GYARADOS_ON = auto()
    _TV_RED_GYARADOS_OFF = auto()
    _PARTNER_NAME_SET = auto()
    _TV_MONITOR_SET = auto()
    _TV_MONITOR_RESET = auto()
    _EFF_SCALE = auto()
    _GET_ITEM_COUNT = auto()
    _PLAY_EMO_SE = auto()
    _AUTO_MSG = auto()
    _AUTO_MSG_STOP = auto()
    _GET_TAG_PATNER_ID = auto()
    _ADD_WAZA = auto()
    _NICKNAME_PLACEMENT = auto()
    _UNIQUE_POKE_TEMP = auto()
    _UNIQUE_POKE_FIX = auto()
    _GET_FORM = auto()
    _NICK_NAME_ALL = auto()
    _DOF_CHANGE_TARGET_POS = auto()
    _DOF_RESET_TARGET_POS = auto()
    _ADD_MAROYAKA_POFFIN = auto()
    _ALL_MONSNO = auto()
    _ALL_MONS_OWN_CHK = auto()
    _CON_CATEGORY_NAME = auto()
    _CON_RANK_NAME = auto()
    _POKE_TYPE_NAME = auto()
    _POFFIN_NAME = auto()
    _DRESS_NAME = auto()
    _EVENT_ENTITY_VISIBLE = auto()
    _UG_LEAVE_HOYUTA = auto()
    _AZUKARIYA_STORE_UI = auto()
    _SET_TELEPORT_ID = auto()
    _POKE_LVUP_HOW_MANY = auto()
    _USE_SPECIAL_ITEM = auto()
    _GET_BP = auto()
    _ZONE_NAME2 = auto()
    _CMD_NAME_END = auto()