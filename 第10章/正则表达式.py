
# 给定文本，用 re 完成：
#  ① 提取所有日期（格式 2026-10-08） 
#  ② 提取所有邮箱地址 
#  ③ 把多个连续空格替换成单个空格

# 验收标准：

# [ ] 三个都用了 re 模块
# [ ] ① 用了正确的字符类（\\d 等）
# [ ] ② 的邮箱提取不能漏掉带 + 或 . 的
# [ ] 能说出 re.search / re.match / re.findall 的区别

txt = ''' 今天是 2026-10-23 ，实验截止日期：2026-11-05。
联系负责人邮箱：stu_ai@mail.guet.edu.cn ，助教邮箱 test123@qq.com 
备注：   数据文件   已上传，   2026-10-20 提交初稿。
请勿发送至 bad-email@xxx （这不是合法邮箱）
'''
import re
pa = r"\d{4}-\d{2}-\d{2}"
print(re.findall(pa,txt))

print(re.findall(r"\b\w+@[A-Za-z0-9.][A-Za-z0-9.]+.[a-z]\b",txt))

print(re.sub(r"\s+"," ",txt))

