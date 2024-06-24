def binary_search(list_of_numbers, item):
    low = 0
    high = len(list_of_numbers) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = list_of_numbers[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return "The number wasn't found"


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 10))
print(binary_search(my_list, 11))
print(binary_search(my_list, -20))

names = ['Mary', 'Anna', 'Ivan', 'Max']
print(binary_search(names, 'Ivan'))
