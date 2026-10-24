#日志配置
import logging

def set_log():

    logg =logging.getLogger()
    logg.handlers.clear()

    logg.setLevel(logging.DEBUG)
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    fh = logging.FileHandler(r"E:\VS_tools\Project\Learn_python\结束\data\run.log",encoding="utf-8",mode = "a")
    fh.setFormatter(fmt)

    fs = logging.StreamHandler()
    fs.setFormatter(fmt)

    logg.addHandler(fs)
    logg.addHandler(fh)

    return logg
