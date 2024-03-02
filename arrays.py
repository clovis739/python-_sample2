"""
given an array [15, 13, 9, 3, 4, 13,, 3, 10]
(a): find the minimu  and maximum values 
(b): find the range
find the mean and mode of the arrays
find the standared deviation of the array
creat a new array storing the z-score of each value in the array
remove all repeatinf numbers in the original array
print all the values with a z-score of above 3 or below 3

"""
lst =  [15, 13, 9, 3, 4, 13, 3, 10]
l=eval(input("Enter a list of numbers: "))
large = l[0]
small = l[0]
for num in l:
    if num > large:
        large = num
    if num < small:
        small= num
print("min number: ", small)
print("max number: ", large)            

def find_range(l):
    range_val= large - small
    val_range = range_val / (large - small)
    print("range value", range_val)
    print("coff", val_range)
find_range(l)  

def mode (lst):
    freq= {}
    for i in lst:
        freq.setdefault(i, 0)
        freq[i]+=1
    large
    largelst = []
    for i, j in freq.items():
        if j == large:
            largelst.append(i)
    return largelst
print("mode of list",mode(lst))    
   



def deviation_std(l):
    mean_val= sum(l) / len (l)
    variance_val= sum([((x- mean_val) **2)
                       for x in l]) / len(l)
    result = variance_val **0.5

    print("standard deviation", + str(result))