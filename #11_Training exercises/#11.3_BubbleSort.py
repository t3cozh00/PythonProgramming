def bubble_sort(iterable):
    new_list = list(iterable)
    list_len = len(new_list)
    for i in range(list_len-1):
        for j in range(list_len - i - 1):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return new_list

a = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element : " %i))
    a.append(value)
print("The Sorted List in Ascending Order : ", bubble_sort(a))