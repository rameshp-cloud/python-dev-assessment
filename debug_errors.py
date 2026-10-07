def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]

        return total / len(numbers)

    except ZeroDivisionError:
        # Return None because an empty list has no average.
        return None


def get_list_element(my_list, index):
    try:
        if not isinstance(my_list, list):
            raise TypeError("my_list must be a list")

        return my_list[index]

    except IndexError:
        print("Error: Index is out of range.")
        return None

    except TypeError:
        print("Error: my_list must be a list and index must be an integer.")
        return None


data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []

print(calculate_average(data1))
print(calculate_average(data2))
print(calculate_average(data3))


sample_list = ["apple", "banana", "cherry"]

print(get_list_element(sample_list, 1))
print(get_list_element(sample_list, 5))
print(get_list_element(sample_list, "1"))
