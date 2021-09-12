from charset_normalizer import from_path

def get_encoding(file_path):
    '''
    输入文件路径，返回文件编码
    '''
    results = from_path(file_path)
    for match in results:
        result = match.encoding,match._has_sig_or_bom, match.language, match.encoding_aliases
        return {'encoding':result[0],'has_sig_or_bom':result[1],'language':result[2],'encoding_aliases':result[3]}