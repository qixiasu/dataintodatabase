import os
from dataintodatabase.filefunc.get_csv_header import get_csv_header
from dataintodatabase.filefunc.head_handle import special_character_handle
from dataintodatabase.filefunc.get_encoding import get_encoding
from rich import print


# 生成建表语句和入库语句
def printer(filename, table_name):
    lst_head = get_csv_header(filename)

    print("-" * os.get_terminal_size()[0])

    print("CREATE TABLE %s\n(" % table_name)

    for h in lst_head[0:-1]:
        # 如果包含特殊字符，对表头加引号处理
        if special_character_handle(h):
            print("\"%s\" TEXT," % h.replace('\n', '').replace('\xef\xbb\xbf', ''))
        else:
            print("%s TEXT," % h.replace('\n', ''))

    # 打印最后一个表头信息
    if special_character_handle(lst_head[-1]):
        print("\"%s\" TEXT" % lst_head[-1].replace('\n', ''))
    else:
        print("%s TEXT" % lst_head[-1].replace('\n', ''))

    print(");")

    print("COPY %s FROM '%s' DELIMITER ',' CSV HEADER ENCODING '%s';" % (
        table_name, os.path.abspath(filename), get_encoding(filename)))

    print("-" * os.get_terminal_size()[0])
