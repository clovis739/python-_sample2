def merge_sort(list):
    """
     sort a list in ascending order
    Returns a new sorted list
    
    Dive: find the midpoint of the list and divide in sublist.
    Conquer : Recursively sort sublists created in previos steps
    Combine : merge the sorted sublist created in previos steps

    Taks overall O(n log n) time
    """
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right )

def split(list):
    """Divide the unsorted list at midpoint in to sublist 
    Returns two sublist -- left and  right

    takes overall O(  log n ) time 
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right 

def merge(left ,right):
    """merges two list (arrays), sorting them in the process 
    Returns a new merged list
    """

    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1
    return l
alist = [12,3,35,67,76,65,454,32,16,78,43,2] 
l = merge_sort(alist)
print(l)  
# 
#      

def verified_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True 
    return list[0] < list[1] and verified_sorted(list[1:])
print(verified_sorted(alist))
print(verified_sorted(l))
