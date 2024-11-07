my_num = int(input())
num_base = int(input())
res = ""
letters_numbers = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
while my_num >= num_base:
    if (my_num % num_base) <= 9 and my_num >= num_base:
        res = str(my_num % num_base) +res
        my_num = int((my_num - (my_num % num_base)) / num_base)
    elif my_num % num_base > 9 and my_num >= num_base:
        res = letters_numbers[my_num % num_base] +res
        my_num = int((my_num - (my_num % num_base)) / num_base)
res = str(my_num) + res
print(res)

