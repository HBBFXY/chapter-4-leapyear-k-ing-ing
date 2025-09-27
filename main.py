def is_leap_year(year):
    """判断闰年的核心逻辑"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
    input_year = input("请输入年份：")
    year = int(input_year)
    
    if is_leap_year(year):
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")

except ValueError:
    print(f"错误：输入 '{input_year}' 不是有效数字！请输入整数年份")
except Exception as e:
    print(f"发生未知错误：{str(e)}")
