# 判断表头列名的第一个字符是不是数字
def first_char_is_number(str):
    try:
        int(str[0])
        return True
    except ValueError:
        return False


# 判断表头列名中有没有特殊字符
def special_character_handle(char):
    special_lst = ['(', ')', "%", " "]
    # 返回结果为布尔型
    special_char_result = any(s in char for s in special_lst)
    # 返回并集 ---如果表头第一个字符为数字 或者存在特殊字符则返回true 否则返回false
    return any(s in char for s in special_lst) | first_char_is_number(char)
