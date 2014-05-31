class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        node = self.Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
        return True

    def insertBefore(self, element, data):
        if self.head is None:
            self.add(data)
            return True

        node = self.Node(data)
        cur = self.head
        while cur:
            if cur.next and cur.next.data == element:
                node.next = cur.next
                cur.next = node
                return True
            cur = cur.next
        return False

    def remove(self, element):
        cur = self.head
        while cur:
            if cur.next and cur.next.data == element:
                removed = cur.next
                cur.next = cur.next.next
                del(removed)
                return True
        return False

    def search(self, element):
        cur = self.head
        while cur and cur.data != element:
            cur = cur.next
        if cur and cur.data == element:
            return cur
        return None

    def __repr__(self):
        if self.head:
            string = "[" + str(self.head.data)
        else:
            string = "["

        cur = self.head.next
        while cur:
            string +=  ", " + str(cur)
            cur = cur.next
        string += "]"
        return string


    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def __repr__(self):
            return str(self.data)
