nums = input("请输入若干数字，用空格分隔：").split()
nums = [float(x) for x in nums]

if nums:
    max_val = max(nums)
    min_val = min(nums)
    avg_val = sum(nums) / len(nums)
    print(f"最大值：{max_val}")
    print(f"最小值：{min_val}")
    print(f"平均值：{avg_val:.2f}")
else:
    print("没有输入任何数字！")