# 题目：nums = \[5, 2, 8, 1, 9, 3]，
# 完成： ① 升序排序 ② 降序排序 ③ 追加 10 ④ 在索引 2 处插入 99 
# ⑤ 删除值为 8 的元素 ⑥ 求最大值、最小值、总和

# 验收标准：
# [ ] 六个操作都正确
# [ ] 能说出 sort() 和 sorted() 的区别
# [ ] 能说出 remove() 和 pop() 的区别

nums = [5, 2, 8, 1, 9, 3]

nums.append(int(10))
print(f"追加10：{nums}")

nums.insert(2,99)
print(f"在索引2处插入99：{nums}")
print(f"下标为3的元素 ：{nums.pop(3)}")

# nums.remove(8)
# print(f"删除值为 8 的元素 ：{nums}")


nums.sort(reverse = False)
print(f"升序排序 :{nums}")
nums.sort(reverse = True)
print(f"降序排序 :{nums}")

print(f"max：{max(nums)}、min:{min(nums)}、sum:{sum(nums)}")
