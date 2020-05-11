class queue:
    def __init__(self):
        self.queue = []
    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(1)
    def enqueue(self,item):
        return self.queue.append(item)
    def printQueue(self):
        if len(self.queue)<1:
            return None
        for i in self.queue:
            print(i)
    def size(self):
        return len(self.queue)

obj = queue()
obj.enqueue(1)
obj.enqueue(2)
obj.printQueue()
obj.dequeue()
obj.printQueue()
