import math


def calculate_average(list_of_numbers):
    counter = 0.0
    list_of_numbers_size = len(list_of_numbers)
    for element in list_of_numbers:
        counter += float(element)
    return counter / list_of_numbers_size


def calculate_standard_deviation(list_of_numbers, average_number):
    counter_sum = 0.0
    for element in list_of_numbers:
        counter_sum += (float(element) - float(average_number)) * (float(element) - float(average_number))
    standard_deviation = math.sqrt(counter_sum / len(list_of_numbers))
    return standard_deviation


def file_to_list(file_split, iris_name):
    iris_data = []
    length_sepal = []
    width_sepal = []
    petal_length = []
    petal_width = []
    for line in file_split:
        if iris_name in line[4]:
            length_sepal.append(line[0])
            width_sepal.append(line[1])
            petal_length.append(line[2])
            petal_width.append(line[3])
    iris_data.append(length_sepal)
    iris_data.append(width_sepal)
    iris_data.append(petal_length)
    iris_data.append(petal_width)
    return iris_data


def calculate_averages(iris_data):
    averages = []
    for i in range(len(iris_data)):
        averages.append(calculate_average(iris_data[i]))
    return averages


def calculate_standards_deviations(iris_data, averages_data):
    standard_deviations = []
    for i in range(len(iris_data)):
        standard_deviations.append(calculate_standard_deviation(iris_data[i], averages_data[i]))
    return standard_deviations


def print_data(iris_averages, iris_standard_deviations, iris_name):
    print("\n\nAll data for " + iris_name + ":\n")
    print("The average of septal length is: " + str(iris_averages[0]))
    print("The average of sepal width is: " + str(iris_averages[1]))
    print("The average of petal length is: " + str(iris_averages[2]))
    print("The average of petal width is: " + str(iris_averages[3]) + "\n")
    print("The standard deviation of septal length is: " + str(iris_standard_deviations[0]))
    print("The standard deviation of sepal width is: " + str(iris_standard_deviations[1]))
    print("The standard deviation of petal length is: " + str(iris_standard_deviations[2]))
    print("The standard deviation of petal width is: " + str(iris_standard_deviations[3]))


def file_to_data(file_path):
    with open(file_path, 'r') as file:
        file_split_to_rows = file.readlines()
        file_splited = []
        for row in file_split_to_rows[:-1]:
            file_splited.append(row.split(','))
    return file_splited


if __name__ == '__main__':
    file_dir = r"C:\Users\brhva\Desktop\אוניברסיטה\שנה א\מבוא למדעי הנתונים\exercise\pythonProject1\Ex2\iris.csv"
    file_data = file_to_data(file_dir)
    iris_setosa_data = file_to_list(file_data, "setosa")
    iris_versicolor_data = file_to_list(file_data, "versicolor")
    iris_virginica_data = file_to_list(file_data, "virginica")

    iris_names = ["Iris Setosa", "Iris Versicolor", "Iris Virginica"]
    # calculate averages
    iris_setosa_averages = calculate_averages(iris_setosa_data)
    iris_versicolor_averages = calculate_averages(iris_versicolor_data)
    iris_virginica_averages = calculate_averages(iris_virginica_data)
    # calculate standard deviation
    iris_setosa_standard_deviation = calculate_standards_deviations(iris_setosa_data, iris_setosa_averages)
    iris_versicolor_standard_deviation = calculate_standards_deviations(iris_versicolor_data, iris_versicolor_averages)
    iris_virginica_standard_deviation = calculate_standards_deviations(iris_virginica_data, iris_virginica_averages)
    # print the data of averages and standard deviation
    print_data(iris_setosa_averages, iris_setosa_standard_deviation, iris_names[0])
    print_data(iris_versicolor_averages, iris_versicolor_standard_deviation, iris_names[1])
    print_data(iris_virginica_averages, iris_virginica_standard_deviation, iris_names[2])
