import cchardet as chardet


def get_encoding(filename):
    with open(filename, "rb") as f:
        msg = f.read()
        result = chardet.detect(msg)
        # 如果编码的可信度很高，则直接使用检测出的编码
        if result['confidence'] > 0.9:
            return (result['encoding'])
        # 如果编码的可信度比较低，则使用gb2312编码
        else:
            return 'gb2312'
