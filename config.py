## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQB2OaXOg_6IUpSWx_4TajFmwHgKIURFmg3DJzaTZjFbSDWh_TUrMev7rZmqWHMOVDAl83aH1q1HZ75YH7HaFDBOJNeKRpmgCk3Tw8th95t8L_QM5WkBhEqpdkny8U5gwSR3czmQNGc08p6rpkGCMOzi2F8CY6ZSXktNL88UoRLZ4Gndz4g_OrdEcusOm4Nr9HbrVL-WJxVRkZ8KwPug3kWa8z0CCGTvuK-2R8VR_5sOD5i3q-O9_mP3JgVfhz1iKzGU93XLQm_RFLfqNpr86XdeOU5kDjE6Ai4F5B27zDvw2yClSxCZCCaXsPzePTyxdtWLk39B1Dv90e7OQQp2Ih-ZAAAAATym_O8A")
BOT_TOKEN = getenv("BOT_TOKEN", "5457323408:AAGuyAq9h_fkh_jrynNaSuOjR6S1QbEwlqY")
BOT_NAME = getenv("BOT_NAME", "Nikku")
API_ID = int(getenv("API_ID", "8998012"))
API_HASH = getenv("API_HASH", "b953769c69dbbb1e4b9dd7db16f1a451")
OWNER_NAME = getenv("OWNER_NAME", "♕︎𝐊𝐀𝐓𝐈𝐋'𝐱𝐃♕︎")
OWNER_USERNAME = getenv("OWNER_USERNAME", "kattar_hindu_katil")
ALIVE_NAME = getenv("ALIVE_NAME", "Nikku")
BOT_USERNAME = getenv("BOT_USERNAME", "NikkuRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Nikku Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "World_friends_chatting_hub")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "heartbrokenperson1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5301800943").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/bhumiharsaurabh/lodalelo")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
