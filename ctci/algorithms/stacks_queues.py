class stac :
    stack = []
    queue = []

    def pushchar(self, s):
        self.stack.append(s)

    def enqueue(self, s):
        self.queue.insert(0,s)
        self.queue.insert(0, s)

    def pop(self):
        self.stack.pop()

    def pop_q(self):
        self.queue.pop(())

    def p_stack(self):
        return (self.stack)

    def q_queue(self):
        return (self.queue)


ob = stac()
ob.enqueue(3)
ob.enqueue(5)
print(ob.q_queue())
