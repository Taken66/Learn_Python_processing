def safe_divide(a, b):
    try :
        return a / b
    except ZeroDivisionError :
        return "除数不能为0"
    except TypeError:
        return "参数类型错误"
if __name__ == "__main__":
    print(safe_divide(10, 2) )
    print(safe_divide(10,0 ) )
    print(safe_divide("m", 2) )
