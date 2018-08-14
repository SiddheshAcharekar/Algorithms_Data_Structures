class ListNode:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        '''
        Create a new singly linked list.
        '''
        self.head = None
        
    def __repr__(self):
        '''
        String representation of the list.
        '''
        nodes = []
        curr = self.head
        # At this point curr is a List Node with an element and next attribute
        # So while appending I convert it to its representation form
#         print(type(repr(curr)))    # Has to be a string
        while curr:
            
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ','.join(nodes) + ']'
    
    def prepend(self, data):
        '''
        Insert new element at the start of the list.
        '''
        self.head = ListNode(data = data, next = self.head)
        
    def append(self, data):
        '''
        Insert new element to the end of the list.
        If list is empty then create a new node with the data.
        Else run through each node using curr next till theres no next node and add a new node there
        '''
        if not self.head:
            self.head = ListNode(data = data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data = data)
        
    def find(self, key):
        '''
        Find a key in the list.
        '''
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
            
        return curr
    
    def remove(self, key):
        '''
        Remove the key from the list.
        '''
        curr = self.head
        prev = None
        
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
            
        elif curr:
            prev.next = curr.next
            curr.next = None
        
    def reverse(self):
        '''
        Reverse list in-place.
        '''
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node