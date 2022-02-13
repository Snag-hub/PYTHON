# Write a program to implement the concept of queue using list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp


if __name__ == '__main__':
    q = Queue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))
