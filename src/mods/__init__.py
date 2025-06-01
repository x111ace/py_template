# py_template/src/mods/__init__.py

import os, re, sys, glob, time, shutil, signal, asyncio, logging, collections

from pydantic_graph import BaseNode, GraphRunContext, End, Edge
from typing import Annotated, Optional, Union, List, Dict, Any
from dataclasses import dataclass, field
from pydantic import BaseModel, Field
from datetime import datetime
from pathlib import Path

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
from dotenv import load_dotenv
load_dotenv(dotenv_path=ENV_PATH)

GRAPH_DIR = os.path.abspath(os.path.join(MOD_DIR, 'graph'))
STATE_DIR = os.path.abspath(os.path.join(GRAPH_DIR, 'state'))
if not os.path.exists(STATE_DIR):
    os.makedirs(STATE_DIR, exist_ok=True)

APP_PERSISTENCE_FILE = Path(os.path.join(STATE_DIR, 'app_graph_state.json'))

INNER_GRAPH_DIR = os.path.abspath(os.path.join(GRAPH_DIR, 'inner'))
# INNER_STATE_DIR = os.path.abspath(os.path.join(INNER_GRAPH_DIR, 'state'))
# if not os.path.exists(INNER_STATE_DIR):
#     os.makedirs(INNER_STATE_DIR, exist_ok=True)

# TEST_APP_PERSISTENCE_FILE = Path(os.path.join(INNER_STATE_DIR, 'test_app_graph_state.json'))

ind1_4 = "    "
ind2_4 = "        "
ind3_4 = "            "
ind4_4 = "                "