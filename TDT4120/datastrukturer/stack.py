class Stack:
    stackList = []

    def push(self, element):
        self.stackList.append(element)

    def pop(self):
        try:
            return self.stackList.pop()
        except:
            #print underflow
            return None
        
    def peek(self):
        try:
            return self.stackList[-1]
        except:
            return None


#test
'''
s = Stack()
s.push('a')
s.push('b')
print s.peek()
print s.pop()
'''
