# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default="29811190", cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="e7c88f0e4ee240aa24fca07ec579f342")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default="1AZWarzYBu1-2tjnYnVlrtUHEw6ntI-YwP0AbSjheuLmtdhnYD4B-JC-xHNDTGiTNE1HF__ybMObfSxdsdr4o-ujmSguC-BADXXOqAfaSJxe8MPsVLPGp5iyRVTS9sRzhSUyIFSiAhFsKCb56URdspnmY5rL8Krrhyr3EAvIEnfczTkXu66AD1IZK2UyIiVx8FZE0CLmKV1Da0BdP24KO3loTmtjt0nmz81WFFnLAyf-TcOGlIDA7MeYQjjeB0E0a3qSvTmpbHMe6X0m7kIdTzOfYYPuhUKLpjAGncToD-6Ljdf0fBfIygPN6x3WFHsj0BJ7P30K814y_OC6LHLGkAwKwtmHAXow=")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", default="http://redis-13758.c301.ap-south-1-1.ec2.cloud.redislabs.com"))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default="FFp0JibyhUhPPAYHrJJDoL4DCmgBMtnJ")
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
