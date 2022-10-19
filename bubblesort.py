def Bubble_Sort(data):
    for i in range(1, len(data)):
        for j in range(0,len(data) - i):
            if (data[j] > data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
        print(data)



arr = [ 2,7,9,0,5,1,3,9 ]
print(arr)
Bubble_Sort(arr)