numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_index = numbers.index(None)
sum_without_missing = sum(n for n in numbers if n is not None)
count = len(numbers)
mean_value = sum_without_missing / count
numbers[missing_index] = mean_value
print("Измененный список:", numbers)
