#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modifieded By: @DC4_WARRIOR

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

async def run_app():
    app = web.Application()
    app_runner = web.AppRunner(app)
    await app_runner.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app_runner, bind_address, PORT).start()

if __name__ == "__main__":
    # create download directory if it doesn't exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    plugins = dict(root="plugins")
    Warrior = Clinton(
        "@BOT_X_BOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    Warrior.run()

    web_server_task = run_app()
    Warrior.loop.run_until_complete(web_server_task)
