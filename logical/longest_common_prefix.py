def longest_common_prefix(str_lst):
    if not str_lst:
        return ""

    prefix = str_lst[0]

    for string in str_lst[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix

str_lst = ["flower", "flow", "flight"]
res = longest_common_prefix(str_lst=str_lst)
print(res)
