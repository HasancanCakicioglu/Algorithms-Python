import time


array = [3,2,1,4,5,6]

def cycleSort(array):

    for i in range(len(array)):
        pas = i
        item = array[i]
        
        for j in range(i+1,len(array)):
            if item > array[j]:
                pas += 1
        if pas == i:
            continue
        while item == array[pas]:
            pas+=1
        array[pas],item = item,array[pas]

        while pas!= i:
            print(str(i)+" - "+str(pas))
            pas =i
            for j in range(i+1,len(array)):
                if item>array[j]:
                    pas+=1
            while item == array[pas]:
                pas+=1
            
            array[pas],item = item,array[pas]

        
    return array


time.sleep(2)
start_time = time.time()

a = cycleSort(array)

end_time = time.time()
elapsed_time = end_time - start_time
print(a)
print("Zaman ", elapsed_time, " saniye")
