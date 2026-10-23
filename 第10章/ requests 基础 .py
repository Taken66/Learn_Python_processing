
# 题目：用 requests 请求一个公开 API（如 
# https://httpbin.org/get
# ）， 
# ① 打印状态码
# ② 把返回的 JSON 转成字典并打印某个字段
# ③ 带上自定义参数请求

# 验收标准：

# [ ] ① 状态码是 200
# [ ] ② 用了 .json() 方法
# [ ] ③ 传参用了 params 参数（不是自己拼 URL）
# [ ] 能说出超时参数为什么必须设置
import requests as req

x = req.get("https://httpbin.org/get",params={"name":"LX","age":20},timeout=5)
print(x.text)
print(x.status_code)
print(x.json())
print(x.json()["args"])

