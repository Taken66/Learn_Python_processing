# 题目：把一个包含"实验配置"的字典（含姓名、日期、参数列表、嵌套字典）： 
# ① 保存为 JSON 文件 ② 读回来并打印某个嵌套字段 
# ③ 支持中文（不能被转义成 \uXXXX）

# 验收标准：
# [ ] 用了 json.dump 和 json.load
# [ ] ③ 用了 ensure\_ascii=False
# [ ] 读回后能访问嵌套字段
# [ ] 能说出 JSON 和字典的区别
import json

exp_config = {
    "姓名": "Alice",
    "日期": "2026-10-23",
    "参数列表": [0.01, 128, 20, "SVM"],   # 列表
    "模型设置": {                        # 嵌套字典！
        "kernel": "rbf",
        "seed": 42,
        "max_iter": 500
    }
}
json_s = json.dumps(exp_config, ensure_ascii=False)
print(json_s)

data = json.loads(json_s)
print(data["模型设置"])
