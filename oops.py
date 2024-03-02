# # class Iterm :
# #     pass
# # iterm1 = 'phone'
# # iterm1_price = 100
# # iterm1_quantity = 5
# # iterm1_price_total = iterm1_price * iterm1_quantity

# # random_str= 'clovis'
# # print(random_str.upper())
# # print(type(iterm1))
# # print(type(iterm1_quantity))
# # print(type(iterm1_price))
# # print(type(iterm1_price_total))

# # class Iterm ():
# #     pass

# class Iterm :
#     pay_rate = 0.8
#     def __init__(self,name: str, price: float, quantity=0):
       
#     #    run validatipon on the receive argurment 

#        assert price >= 0, f"price  {price} is not greater than or equall to zero"
#        assert quantity >= 0, f"price  {quantity} is not greater than or equall to zero"

#     #    assign to self
#        self.name = name
#        self.price = price
#        self.quantity = quantity

#     # def calculate_total_price(self, x, y):
#     #     return x * y


# def calculate_total_price(self):
#     return self.price * self.quantity


# iterm1 = Iterm('phone', 100, 1)

# iterm2 = Iterm('laptop', 1000, 3)


# # print(iterm1.name)
# # print(iterm2.name)
# # print(iterm1.price)
# # print(iterm2.price)
# # print(iterm1.quantity)
# # print(iterm2.quantity)
# # iterm1_price_total = iterm1_price * iterm1_quantity

    

# print(Iterm.__dict__)
# print(iterm1.__dict__)

# name = input('name')
# # print(iterm1.calculate_total_price())
# # print(iterm2.calculate_total_price())


class Node :
    def __init__(self, data):
        self.previus = None
        self.data= data
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.start_node = None
        self.last_node = None

# function to add elements to double DoubleLinkedList 

def append(self, data):
    if self.last_node is None:
        self.head = Node(data)
        self.last_node= self.head
        # adding node to the tail of doubly linked list  
    else :
        new_node = Node(data)
        self.last_node.next = new_node
        new_node.previus = self.last_node
        new_node.next=None 
        self.last_node = new_node

        # function printing and traversing the content of doubly linked list from left to right and right to left  
def display(self, Type):
    if Type == "left_to_right":
        current = self.head
        while current is not None:
         print(current.data, end="")
         current =current.next
        print()

    else:
            current = self.last_node
            while current is not None:
              print (current.data, end="")
              current= current.previus
            print()
  
                

