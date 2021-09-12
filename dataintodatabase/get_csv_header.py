import sys, os, csv
from get_encoding import get_encoding
#获取csv文件的头信息
def get_csv_header(filename):
    try:
        with open(filename,'r',encoding=get_encoding(filename)['encoding']) as f:
            lines = csv.reader(f)
            return next(lines)

    except FileNotFoundError:
        print("No such file: '%s'" %os.path.basename(filename))
        sys.exit()