import itertools


def validate_input(input_str):
    new_input_str = input_str
    while not new_input_str.isdigit() or int(new_input_str) < 1:
        if len(new_input_str) < 1:
            new_input_str = input("Please enter a number greater than 1: \n")
        elif not new_input_str.isdigit():
            new_input_str = input("Please enter a digit greater than 1: \n")
        elif new_input_str.isdigit():
            if int(new_input_str) < 1:
                new_input_str = input("Please enter a number greater than 1: \n")
    return int(new_input_str)



def list_of_sample_space(my_tuple, num_of_children):
    combination = list(itertools.product(my_tuple, repeat = num_of_children))
    return combination


def calculate_probability_of_two_girls(list_of_samples):
    list_size = len(list_of_samples)
    probabilities_of_two_girls = 0
    for i in range(len(list_of_samples)):
        counter = 0
        for j in range(len(list_of_samples[i])):
            if list_of_samples[i][j] == "Girl":
                counter += 1
        if counter == 2:
            probabilities_of_two_girls += 1
    return probabilities_of_two_girls / list_size


def print_list_rows(list_of_samples):
    for i in range(len(list_of_samples)):
        print(str(i + 1) + ")\t" + str(list_of_samples[i]))


input_number = input("Enter number of children: \n")
valid_number = validate_input(input_number)
boy_girl_tuple = ("Boy", "Girl")
list_of_possabilities = list_of_sample_space(boy_girl_tuple, valid_number)
print_list_rows(list_of_possabilities)
print(list_of_possabilities)
res = calculate_probability_of_two_girls(list_of_possabilities)
print("The probability of only two girls is from " + str(valid_number) + " children is: " + format(res,
                                                                                                   '.10f'))  # I formatted it to ten figures after the dot to prevent failure in big numbers.
