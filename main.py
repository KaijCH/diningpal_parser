from loggers.runtime_logger import logger
from configs import default_file
import sys

def main() -> None:
    # check logger initiation
    if  logger is None:
        sys.exit(-1)
    
    pass

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        default_file.UnderDevelopment = True
    main()
