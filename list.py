class Node:

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
        
    def __repr__(self) :
        return"<Node data: %s> " % self.data   
class LinkedList:
    head = None

    def __init__(self):
      self.head = None

    def is_empty(self):
         return self.head == None
      
    def size(self):
         """ 
         returns the number od nodes in the list takes linear time O(n) time
         """
         

         current = self.head
         count = 0

         while current :
            # while count != None: same as tat at the top
            count += 1
            current = current.next_node

         return count   

    def add(self, data):
       """add new node containing data at head of the list takes  O(1) time .. thats constant time """  
       new_node = Node(data)
       new_node.next_node =self.head
       self.head = new_node         

    def search(self, key):
        """search for the first node containing data that matches the key 
        returns the node or a none if not found
        
        Takes O(n) time to search
        """
        current = self.head
        while current :
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None        
    

    def insert(self, data, index):
        """Insert a new Node containing data at index position 
        Insert takes 0(1) time but finding the node at the  insertion point takes 0(n) time
        
        takes overall 0(n) time 
        """
        if index == 0:
            self.add(data)

        if index > 0:    
            new = Node(data)

            position = index 
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1
                prev_node = current
                next_node = current.next_node

                prev_node.next_node = new
                new.next_node = next_node

def remove (self, key):
    """removes Node containing data that macthes the key returns the node pr None if key does not exist 
    Takes 0(n) time"""

    current = self .head
    previous = None
    found  = False

    while current and not found :
        if current.data == key and current is self.head:
            found = True
            self.head = current.next_node
            self.__count  -= 1
            return current 
        elif current.data == key:
            found = True
            previous.next_node = current.next_node
            self.__count -= 1
            return current 
        else:
            previous = current
            current = current.next_node
        return None          


    def __repr__(self):
            """return a string representation of the list taking the best case of O(n) time linear time"""
            nodes = []
            current = self.head

            while current:
                if current is self.head:
                    nodes.append("[Head : %s]" % current.data)
                elif current.next_node is None:
                    nodes.append("[Tail: %s]" % current.data)
                else:
                    nodes.append("[%s]" % current.data)
                current = current.next_node
            return '-> '.join(nodes) 

    def __repr__(self) :
        """return a string reppresentation of the list takes 0(n) time"""
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current =  current.next_node
        return '-> '.join(nodes)        
