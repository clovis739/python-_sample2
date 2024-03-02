def linear_search(list, target):
    """
    returns the posintionn of tyhe targeet if found , sleae returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verufy(index):
    if index is not None :
        print("target found at index", index)
    else:
        print("target not found in list ")

numbers=[1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 12)
verufy(result)        
result = linear_search(numbers, 6)
verufy(result)        
result = linear_search(numbers, 9)
verufy(result)        