import sys

if sys.version_info < (3, 12):
    raise RuntimeError("This program requres Python 3.12+")