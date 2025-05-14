from configs import default_file

import threading
import datetime
import inspect
import queue
import sys

class RuntimeLogger:
    
    # logger level
    __warn, __info, __fail = "WARN", "INFO", "FAIL"

    def __init__(self, development: bool = False) -> None:
        """
            initiate logger singleton usable acorss diff class
        
        """
        self.developmewnt: bool = default_file.UnderDevelopment
        self.output: str = default_file.DefaultLogOutput
        
        self.halt = threading.Event()
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self.__logs, daemon=True)
        self.thread.start()
        
    def __logs(self) -> None:
        """
            collect log tiem from queue, write to local output file
        
        """
        with open(file=self.output, mode="a", encoding="utf-8") as f:
            # stop log collection when queue empty and halt flag set to true
            while not self.queue.empty() or not self.halt.is_set():
                try:
                    content = self.queue.get(timeout=0.2)
                except queue.Empty:
                    continue
                f.write(content + "\n")
                f.flush()
                if self.developmewnt:
                    sys.stdout.write(content + "\n")
                    sys.stdout.flush()
                self.queue.task_done()

        return None
    
    def stops(self) -> None:
        """
            terminate logger consumption, wait all write thread till complete
            invoke only before program safe exit
        
        """
        self.halt.set()
        self.thread.join()
    
    def warns(self, context: str, message: str = None) -> None:
        """
            write warn level log with param
        
        """
        
        content = "[{level}] {context}: {message}".format(level=self.__fail, context=context, message=message)
        self.queue.put(content)
    
    def infos(self, context: str, message: str = None) -> None:
        """
            write info level log with param
        
        """
        content = "[{level}] {context}: {message}".format(level=self.__fail, context=context, message=message)
        self.queue.put(content)
    
    def fails(self, context: str, message: str = None) -> None:
        """
            write fail level log with param
        
        """
        content = "[{level}] {context}: {message}".format(level=self.__fail, context=context, message=message)
        self.queue.put(content)


# logger singleton by var
logger = RuntimeLogger()
