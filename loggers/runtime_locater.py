import datetime
import inspect

def locate_execution() -> str:
    frame = inspect.currentframe()
    if not frame or not frame.f_back:
        return "exceptional location"
    info = inspect.getframeinfo(frame=frame.f_back)
    
    local = datetime.datetime.now()
    epochs = int(local.timestamp())

    context = "[{epochs} {local}] {filename} {function} {lineno}".format(epochs=epochs, local=str(local), filename=info.filename, function=info.function, lineno=str(info.lineno))
    
    return context
