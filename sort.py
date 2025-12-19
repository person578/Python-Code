def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

array = [5, 15, 3, 9, 1, 18, 40, 50, 23, 2, 43]

sort(array)

for i in range(len(array)):
    print(array[i])