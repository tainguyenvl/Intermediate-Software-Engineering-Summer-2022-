import queue


def reverseFirstKElements(q, k):
    if (q.empty() == True or k > q.qsize()):
        return q
    if (k <= 0):
        return q

    stack = []
    for i in range(k):
        stack.append(q.get())

    for i in range(k):
        q.put(stack.pop())

    for i in range(q.qsize() - k):
        q.put(q.queue[0])
        q.get()
    return q


q = queue.Queue(maxsize=20)
q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
k = 5
print(reverseFirstKElements(queue, k))
