#doubly linked list
class LLElement:
    def __init__(self):
        self.previous = None
        self.next = None
        self.key = None


class LinkedList:
    def __init__(self):
        self.head = LLElement()


    def listSearch(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x

    
'''klasse ikke ferdig... se kap. 10.2 i algdat'''
