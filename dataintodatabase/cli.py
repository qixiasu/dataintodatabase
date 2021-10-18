import argparse
import sys
from dataintodatabase.filefunc.did import printer
from dataintodatabase.filefunc.version import version
from dataintodatabase.filefunc.function_run_time import print_run_time


@print_run_time
def main():
    parser = argparse.ArgumentParser(description='PostgreSQL入库工具', prog='PostgreSQL入库工具')
    parser.add_argument('-t', '--tablename', required=True, help="需要建的表名")
    parser.add_argument('-f', '--filename', required=True, help="待入库的文件名")
    parser.add_argument('-v', '--version', action="version", version='PostgreSQL入库工具 %s' % version, help="版本信息")
    args = parser.parse_args()
    printer(args.filename, args.tablename)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
