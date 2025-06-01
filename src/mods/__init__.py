# py_template/src/mods/__init__.py

from pydantic_graph import BaseNode, GraphRunContext, End
from typing import Optional, Union, List, Dict, Any
from dataclasses import dataclass, field
from pydantic import BaseModel, Field
from datetime import datetime

import os, re, sys, glob, time, shutil, asyncio, logging, collections

from colorama import init, Fore, Style
init(autoreset=True)
nrm = Style.RESET_ALL
red = Fore.RED
grn = Fore.GREEN
yel = Fore.YELLOW
blu = Fore.BLUE
mag = Fore.MAGENTA

# Custom logging formatter to color levelname by log level
handler = logging.StreamHandler()
class ColorFormatter(logging.Formatter):
    LEVEL_COLORS = {
        logging.ERROR: red,
        logging.WARNING: yel,
        logging.INFO: grn,
        logging.DEBUG: blu,
        logging.CRITICAL: mag,
    }
    BASE_FORMAT = '\n(%(asctime)s) ***{color}%(levelname)s{reset}***\n: %(message)s'

    def format(self, record):
        color = self.LEVEL_COLORS.get(record.levelno, nrm)
        fmt = self.BASE_FORMAT.format(color=color, reset=nrm)
        formatter = logging.Formatter(fmt, datefmt='%#m/%#d/%Y, %#H:%M:%S')
        return formatter.format(record)

handler.setFormatter(ColorFormatter())
logging.basicConfig(
    level=logging.INFO,
    handlers=[handler],
    force=True
)

MOD_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(MOD_DIR, '..'))
ROOTPTH = os.path.abspath(os.path.join(SRC_DIR, '..'))
ENV_PATH = os.path.join(ROOTPTH, '.env')

GRAPH_DIR = os.path.abspath(os.path.join(MOD_DIR, 'graph'))
STATE_DIR = os.path.abspath(os.path.join(GRAPH_DIR, 'state'))
if not os.path.exists(STATE_DIR):
    os.makedirs(STATE_DIR, exist_ok=True)

ind1_4 = "    "
ind2_4 = "        "
ind3_4 = "            "
ind4_4 = "                "

from dotenv import load_dotenv
load_dotenv(dotenv_path=ENV_PATH)