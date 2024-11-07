def to_decimal(my_str, num_base):
    res = 0
    base = 0
    letters_numbers = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    for i in my_str[::-1]:
        if i.isdigit() == True:
            if base == 0:
                res += int(i) * 1
                base = num_base
            else:
                res += int(i) * base
                base = base * num_base
        else:
            if base == 0:
                res += int(letters_numbers[i])
                base = num_base
            else:
                res += int(letters_numbers[i]) * base
                base = base * num_base
    return res

def to_number(my_num, num_base):
    res = ""
    letters_numbers = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    while my_num >= num_base:
        if (my_num % num_base) <= 9 and my_num >= num_base:
            res = str(my_num % num_base) + res
            my_num = int((my_num - (my_num % num_base)) / num_base)
        elif my_num % num_base > 9 and my_num >= num_base:
            res = letters_numbers[my_num % num_base] + res
            my_num = int((my_num - (my_num % num_base)) / num_base)
    res = str(my_num) + res
    return res

num_1 = input().lower()
num_2 = input()
num_base = int(input())
num_1_decimal = to_decimal(num_1, num_base)
num_2_decimal = to_decimal(num_2, num_base)
num_add = num_1_decimal + num_2_decimal
num_3 =to_number(num_add, num_base)
print(num_3)