class Node:
    """an object for storing node of a linked list.
    models two attributes - data and link to the next node in the list.
    """

    data = None
    next_node = None

    def __init__(self, data):
       self.data = data 

    def __repr__(self):
       return "<Node data: %s>" % self.data    


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
            count += 1
            current = current.next_node

         return count   

   def add(self, data):
       """add new node containing data at head of the list takes  O(1) time .. thats constant time """  
       new_node = Node(data)
       new_node.next_node =self.head
       self.head = new_node     
   def __repr__(self):
            """return a string representation of the list taking the best case of O(n) time linear time"""
            nodes = []
            current = self.head

            while current:
                if current is self.head:
                    nodes.append("[head: s%]" % current.data)
                elif current.next_node is None:
                    nodes.append("[tail: s%]" % current.data)
                else:
                    nodes.append("[%s]" % current.data)
                current = current.next_node
            return '-> '.join(nodes)        