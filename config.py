#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6400468647:AAHd3WGvsIQWg47kBijOuxE1aM_8H1WUuFI")
    API_ID = int(os.environ.get("API_ID", "10551685"))
    API_HASH = os.environ.get("API_HASH", "477dff815fdc7cba803c1bc02c459d03")
    AUTH_USERS = "1112773045,1975696269"

