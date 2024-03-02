def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last )//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
# constant time log n o(n)
    return None


def verufy(index):
    if index is not None :
        print("target found at index", index)
    else:
        print("target not found in list ")

numbers=[1,2,3,4,5,6,7,8,9,10]
result = binary_search(numbers, 12)
verufy(result)        
result = binary_search(numbers, 6)
verufy(result)        
result = binary_search(numbers, 10)
verufy(result)        