import getopt 
import sys

__version__ = '0.0.1'
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
        print(f"{__version__}")
        sys.exit(0)

