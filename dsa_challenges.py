def filter_and_sort_evens(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    even_numbers.sort()
    return even_numbers


numbers = [5, 2, 8, 3, 10, 7]

result = filter_and_sort_evens(numbers)

print(result)


def count_character_frequency(text):
    frequency = {}

    for character in text.lower():
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    return frequency


text = "Hello World"

result = count_character_frequency(text)

print(result)