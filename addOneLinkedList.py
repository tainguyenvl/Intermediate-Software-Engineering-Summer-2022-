class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

def addOne(head:Node):
  addWithCarry(head)
  return head

def addWithCarry(head:Node):
  if (head == None):
    return 1

  carry = addWithCarry(head.next)
  sum = head.data + carry

  head.data = sum % 10
  return sum // 10

def oddEvenList(head: Node):
  if (head!= None):
    odd = head
    even =  head.next
    evenHead = even

    while even != None and even.next != None:
      odd.next = odd.next.next
      even.next = even.next.next
      odd = odd.next
      even = even.next
    
    odd.next = evenHead
  return head

  
if __name__ == '__main__':
    first = Node(1)
    second = Node(2)
    third = Node(3)
    four = Node(4)

    first.next = second
    second.next = third
    third.next = four
    #addOne(first)
    oddEvenList(first)
    temp = first
    while temp:
        print(temp.data)
        temp = temp.next

