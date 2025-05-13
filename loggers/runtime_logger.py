from configs import default_file

import threading
import datetime
import queue
import sys

class RuntimeLogger:
    
    # logger level
    __warn, __info, __fail = "WARN", "INFO", "FAIL"

    def __init__(self, development: bool = False) -> None:
        """
            initiate logger singleton usable acorss diff class
        
        """
        
        self.developmewnt = default_file.UnderDevelopment
        self.output = default_file.DefaultLogOutput
        
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
    
    def warns(self, subsys: str, message: str = None) -> None:
        """
            write warn level log with param
        
        """
        epochs = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
        local = datetime.datetime.now()
        content = "[{level}] [{epochs} - {local}] [{subsys}]: {message}".format(
            level=self.__warn, epochs=epochs, local=local, subsys=subsys, message=message
            )
        self.queue.put(content)
    
    def infos(self, subsys: str, message: str = None) -> None:
        """
            write info level log with param
        
        """
        epochs = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
        local = datetime.datetime.now()
        content = "[{level}] [{epochs} - {local}] [{subsys}]: {message}".format(
            level=self.__info, epochs=epochs, local=local, subsys=subsys, message=message
            )
        self.__logs(message=content)
    
    def fails(self, subsys: str, message: str = None) -> None:
        """
            write fail level log with param
        
        """
        epochs = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
        local = datetime.datetime.now()
        content = "[{level}] [{epochs} - {local}] [{subsys}]: {message}".format(
            level=self.__fail, epochs=epochs, local=local, subsys=subsys, message=message
            )
        self.__logs(message=content)


# logger singleton by var
logger = RuntimeLogger()