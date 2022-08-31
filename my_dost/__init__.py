import getopt 
import sys

__version__ = '1.0'
__release_id__ = 1
__author__ = 'PyBOTs LLC'
__email__ = 'support@pybots.ai'

argument_list = sys.argv[1:]
compatible_system = False

short_options = "v"
long_options = ["version"]

arguments, values = getopt.getopt(
    argument_list, short_options, long_options)
for current_argument, current_value in arguments:
    if current_argument in ("-v", "--version"):
        print(f"{__version__},{__release_id__}")
        sys.exit(0)

from my_dost.Engine import *