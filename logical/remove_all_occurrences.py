def remove_all_occurrences(string_val, part_val):
    while len(part_val) < len(string_val) and part_val in string_val:
        find_part_index = string_val.find(part_val)

        string_val = string_val[:find_part_index] + string_val[find_part_index + len(part_val):]

    return string_val

str_input = "daabcbaabcbc"
part = "abc"

res = remove_all_occurrences(string_val=str_input, part_val=part)
print(res)