# py_template/src/mods/__init__.py

import os

MODULES_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_CODE_DIR = os.path.abspath(os.path.join(MODULES_DIR, '..'))
FULL_PROJECT_ROOT = os.path.abspath(os.path.join(SOURCE_CODE_DIR, '..'))

ENV_PATH = os.path.join(FULL_PROJECT_ROOT, '.env')

ind1_4 = "    "
ind2_4 = "        "
ind3_4 = "            "
ind4_4 = "                "
