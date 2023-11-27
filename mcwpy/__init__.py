# -*- coding: ascii -*-
""" 
 __  __  _______          _______       
|  \/  |/ ____\ \        / /  __ \      
| \  / | |     \ \  /\  / /| |__) |   _ 
| |\/| | |      \ \/  \/ / |  ___/ | | |
| |  | | |____   \  /\  /  | |   | |_| |
|_|  |_|\_____|   \/  \/   |_|    \__, |
                                   __/ |
                                  |___/ 

Minecraft with Python is a Python library for creating Minecraft datapacks using Python.
    https://github.com/vianneyveremme/minecraft_with_python
"""
# ~ #  ~ #  ~ #  ~ #  ~ #  ~ # ~
# Main modules
# ~ #  ~ #  ~ #  ~ #  ~ #  ~ # ~
from .datapack import *
from .pack_meta import *
from .workspace import *

# ~ #  ~ #  ~ #  ~ #  ~ #  ~ # ~
# Secondary modules
# ~ #  ~ #  ~ #  ~ #  ~ #  ~ # ~
"""
from .advancements import *
from .dimension import *
from .dimension_type import *
from .functions import *
from .loot_tables import *
from .predicates import *
from .recipes import *
from .structures import *
from .tags import *
from .worldgen import *
"""

# ~ #  ~ #  ~ #  ~ #  ~ #  ~ # ~
# Other modules
# ~ #  ~ #  ~ #  ~ #  ~ #  ~ # ~
from .utility import *

# ~ #  ~ #  ~ #  ~ #  ~ #  ~ # ~
# Python modules
# ~ #  ~ #  ~ #  ~ #  ~ #  ~ # ~
import sys


__version__ = '0.1.2'
REQUIRED_PYTHON_VERSION = '3.11.0'


# Check Python version
if sys.version_info < tuple([int(e) for e in REQUIRED_PYTHON_VERSION.split('.')]):
    print(f"{Font.WARN}For optimal results it is recommended to use Python {REQUIRED_PYTHON_VERSION} or above.{Font.END}")
else:
    print(f"{Font.HEADER}{Font.BOLD}Hello from the MCWPy community :){Font.END}")
del sys

# Print the location where the default path is
print(f"{Font.VARIABLE_INFO}Default path: {Datapack(pack_mcmeta='').path}.{Font.END}")
