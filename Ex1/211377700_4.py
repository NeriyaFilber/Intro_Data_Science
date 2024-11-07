binary_number = input()
number_amount = int(input())
num_to_add = "1"
while len(binary_number) < number_amount:
    binary_number = "0" + binary_number
while len(num_to_add) < number_amount:
    num_to_add = "0" + num_to_add
rev = ""
for i in binary_number:
    if i == "0":
        rev = rev + "1"
    else:
        rev = rev + "0"
#print(rev)
#print(num_to_add)
carry = "0"
res = ""
for i in range(number_amount)[::-1]:
    if carry == "0":
        if rev[i] == "1" and num_to_add[i] == "1":
            carry = "1"
            res = "0" + res
        elif (rev[i] == "1" and num_to_add[i] == "0") or (rev[i] == "0" and num_to_add[i] == "1"):
            res = "1" + res
        else:
            res = "0" + res
    else:
        if rev[i] == "1" and num_to_add[i] == "1":
            res = "1" + res
        elif (rev[i] == "1" and num_to_add[i] == "0") or (rev[i] == "0" and num_to_add[i] == "1"):
            res = "0" + res
        else:
            res = "1" + res
            carry = "0"

print(res)


