#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6400468647:AAHd3WGvsIQWg47kBijOuxE1aM_8H1WUuFI")
    API_ID = int(os.environ.get("API_ID", "10551685"))
    API_HASH = os.environ.get("API_HASH", "6400468647:AAGzWdp0hHnPvwPol7iXQ-NlABDXCNcWIyY")
    AUTH_USERS = "1112773045,1975696269"

