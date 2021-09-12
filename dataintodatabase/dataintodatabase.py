import os
from get_csv_header import get_csv_header
from head_handle import special_character_handle
from get_encoding import get_encoding
from rich import print
#生成建表语句和入库语句
def printer (filename, tablename):
    lst_head = get_csv_header(filename)
    
    print("-" * os.get_terminal_size()[0])

    print("CREATE TABLE %s\n(" % tablename)

    for h in lst_head[0:-1]:
        #如果包含特殊字符，对表头加引号处理
        if special_character_handle(h):
            print("\"%s\" TEXT," % h.replace('\n', '').replace('\xef\xbb\xbf',''))
        else:
            print("%s TEXT," % h.replace('\n', ''))

    #打印最后一个表头信息
    if special_character_handle(lst_head[-1]):
        print("\"%s\" TEXT" % lst_head[-1].replace('\n', ''))
    else:
        print("%s TEXT" % lst_head[-1].replace('\n', ''))


    print(");")

    print("COPY %s FROM '%s' DELIMITER ',' CSV HEADER ENCODING '%s';" %(tablename, os.path.abspath(filename),get_encoding(filename)['encoding']))
    
    print("-" * os.get_terminal_size()[0])

