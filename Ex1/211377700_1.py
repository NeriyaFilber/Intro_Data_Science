res = 0
my_str = input().lower()
num_base = int(input())
base = 0
letters_numbers = {"a": 10, "b                                         ": 11, "c": 12, "d": 13, "e": 14, "f": 15}
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
print(res)