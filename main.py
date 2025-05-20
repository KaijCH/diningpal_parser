from loggers.runtime_logger import logger
from loggers.runtime_locater import locate_execution
from explorers.explorer import explorer
from configs import default_file

import sys


def main(sign: str) -> None:
    # check component initiation
    if logger is None:
        sys.exit(-1, "failure in logger initialization")
    if not explorer or explorer.checks() is not None:
        logger.fails(context=locate_execution(), message="failure in author initialization")
        sys.exit(-1, "failure in author initialization")
    
    pass


if __name__ == "__main__":
    args = sys.argv
    length = len(args)
    if length < 2:
        sys.exit(-1, "Hint: program cmd param:\n Python_Env main.py  __signature  __optional_debug_flag")
    explorer.signs(sign=args[1])
    if length >= 3:
        default_file.UnderDevelopment = True
    main(args[1])
