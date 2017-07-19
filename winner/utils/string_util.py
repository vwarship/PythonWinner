def reverse(s):
    """
    字符串反向拼写
    :param s: hello
    :return: olleh
    """
    return s[::-1]


def sub_string(s, begin_str=None, end_str=None):
    """
    取字符串的子串
    如：
        s = 'hello world!'
        begin_str = 'he'
        end_str = 'ld'
        return 'llo wor'
    :param s:
    :param begin_str:
    :param end_str:
    :return:
    """

    if not s:
        return ""

    begin_pos = 0
    end_pos = len(s)

    if begin_str:
        pos = s.find(begin_str)
        if pos >= 0:
            begin_pos = pos + len(begin_str)

    if end_str:
        pos = s.find(end_str, begin_pos)
        if pos >= 0:
            end_pos = pos

    return s[begin_pos:end_pos]

