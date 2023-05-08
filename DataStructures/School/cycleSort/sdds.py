def cycleSort(array):
    for i in range(len(array)):
        item = array[i]
        pas = i
        for j in range(i+1, len(array)):
            if array[j] < item:
                pas += 1
        if pas == i:
            continue
        while item == array[pas]:
            pas += 1
        array[pas], item = item, array[pas]
        while pas != i:
            pas = i
            for j in range(i+1, len(array)):
                if array[j] < item:
                    pas += 1
            while item == array[pas]:
                pas += 1
            array[pas], item = item, array[pas]
    return array

array = [10, 3, 2, 5, 56, 43, 23, 12]
print(cycleSort(array))
