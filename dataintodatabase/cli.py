"""Console script for dataintodatabase."""
import argparse
import sys
from dataintodatabase import printer

def main():
    """Console script for dataintodatabase."""
    parser = argparse.ArgumentParser(description='postgresql入库工具',prog='postgresql入库工具')
    parser.add_argument('-t', '--tablename', required=True, help="需要建的表名")
    parser.add_argument('-f', '--filename', required=True, help="待入库的文件名")
    args = parser.parse_args()
    printer(args.filename,args.tablename)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
