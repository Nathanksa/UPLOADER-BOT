#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modifieded By : @DC4_WARRIOR

import os
import logging
from config import Config
from pyrogram import Client as Clinton
from aiohttp import web
from plugins import web_server
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

PORT = "8080"

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Warrior = Clinton("@BOT_X_BOT",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins)
    Warrior.run()
    
    app = web.AppRunner(await web_server())

        await app.setup()

        bind_address = "0.0.0.0"

        await web.TCPSite(app, bind_address, PORT).start()
