import queue

q = queue.Queue(4)
q.put(1)
q.put(2)
q.put(4)

print(q.qsize())

l = queue.PriorityQueue