class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def display(self, times=1):
        current = self.head
        count = 0

        while count < times:    
            print(current.data, end=",")
            current = current.next
            
            if current == self.head:
                count += 1
            


Linked_List = CircularLinkedList()
Linked_List.append(3)
Linked_List.append(4)
Linked_List.append(5)
Linked_List.append(6)

Linked_List.display(3)