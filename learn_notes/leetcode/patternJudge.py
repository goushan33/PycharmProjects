'''
pattern = "abba", str="北京 杭州 杭州 北京" 返回 ture
pattern = "aabb", str="北京 杭州 杭州 北京" 返回 false
pattern = "abc", str="北京 杭州 杭州 南京" 返回 false
pattern = "acac", str="北京 杭州 北京 广州" 返回 false
'''


def judge(pattern, str):
    list_str = str.split()
    if len(pattern) != len(list_str):
        return False
    dict = {}
    length = len(list_str)
    for i in range(length):
        if not dict.get(pattern[i]):
            dict[pattern[i]] = list_str[i]
        else:
            if list_str[i] != dict[pattern[i]]:
                return False
    return True

print(judge("abba","北京 杭州 北京 广州" ))

