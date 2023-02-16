class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    # def __init__(self):
    #     self.head = None
    #


    def __init__(self, nodes=None):
       self.head = None
       if nodes is not None:
           node = Node(data=nodes.pop(0))
           self.head = node
           for elem in nodes:
               node.next = Node(data=elem)
               node = node.next


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
#Insert at beginning
#def add_first(self, node):
#    node.next = self.head
#    self.head = node

#Insert at end

#Inserting at end
#def add_last(self, node):
#    if self.head is None:
#        self.head = node
#        return
#    for current_node in self:
#        pass
#    current_node.next = node