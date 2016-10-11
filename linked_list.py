# Node is where data and a pointer is stored 

class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next 

class LinkedList(object): 

    def __init__(self, head=None, tail=None):
        self.head = head 
        self.tail = tail 

    # print out linked list 
    def show(self): 
        """ Give printed representation of linked list."""
        print "List data displayed: "
        current = self.head 
        while current is not None:
            print current.data, "-> "
            current = current.next
        print None 

    # append node to linked list
    def append(self, data):
        """ Append node to linked list."""
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node 
        else:
            self.tail.next = node 
        self.tail = node 

    # remove node from linked list
    def remove(self, node_value): 
        """ Remove node from linked list."""
        current = self.head 
        prev = None 
        while current is not None:
            if current.data == node_value:
                # if first node (head node)
                if prev is not None:
                    prev.next = current.next 
                else:
                    self.head = current.next

            prev = current
            current = node.next 



