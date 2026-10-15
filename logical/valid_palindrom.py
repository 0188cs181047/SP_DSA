def is_valid_palindrom(pali_str):
    flag = True
    start = 0 
    end = len(pali_str)-1

    while start < end:
        if not pali_str[start].isalnum():
            start += 1

        if not pali_str[end].isalnum():
            end -= 1

        if pali_str[start].lower() != pali_str[end].lower():
            flag = False

        start += 1
        end -= 1

    return "Yes! The string is a valid palindrom" if flag else "No! The string is not valid palindrom"


pali_str = "Ac3?e3c&a"
res = is_valid_palindrom(pali_str=pali_str)
print(res)