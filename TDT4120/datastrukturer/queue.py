class Queue:
    queueList = []
    
    def enqueue(self, element):
        self.queueList.append(element)

    def dequeue(self):
        try:
            return self.queueList.pop(0)
        except:
            #print underflow
            return None



#test
'''
q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print q.dequeue()
print q.dequeue()
'''
