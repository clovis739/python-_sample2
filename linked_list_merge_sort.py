from list import LinkedList

def merge_sort(linked_list):
    """
    sort a linked list in assending order 
    -Recursively didvide thr linked list in to sublist containing a single node
    -Repeatedly merge the sublists to produce sorted sublist untill one remains 

    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left= merge_sort(left_half)
    right = merge_sort(right_half)

    return merge_sort(left, right)

def split(linked_list):
    """
   divide the unsorted list at midpoint into subist
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else