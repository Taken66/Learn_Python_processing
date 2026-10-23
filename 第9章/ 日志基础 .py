
# 题目：配置 logging，使日志同时输出到控制台和文件，
# 并分别记录一条 DEBUG、INFO、WARNING、ERROR 级别的日志。

# 验收标准：

# [ ] 控制台和文件里都能看到日志
# [ ] DEBUG 级别默认可能不显示——能解释为什么，并让它显示出来
# [ ] 日志格式包含：时间、级别、消息
# [ ] 能说出 print 和 logging 的区别（为什么正式代码用 logging）

import logging
from re import DEBUG


# logging.basicConfig(
#     level=logging.DEBUG,
#     format= "%(asctime)s-%(levelname)s-%(message)s",
#     filename = "test.log"
#     )
# logging.debug("A debug message")
# logging.info("A info message")
# logging.critical("A critical message")
# logging.error("An error message")
# logging.warning("A warning message")

log = logging.getLogger()
log.setLevel(logging.DEBUG)

fmt = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")

fh = logging.FileHandler("test.log",encoding="utf-8")
fh.setFormatter(fmt)

sh = logging.StreamHandler()
sh.setFormatter(fmt)

log.addHandler(fh)
log.addHandler(sh)

logging.debug("A debug message")
logging.info("A info message")
logging.critical("A critical message")
logging.error("An error message")
logging.warning("A warning message")

