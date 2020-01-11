from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        # self.size = 0

    def append(self, item):
        if self.capacity == self.storage.length:
            self.current.value = item
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

            # self.size -= 1
        else: 
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            # self.size += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head

        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        print(f'Head Value: {self.storage.head.value}')
        print(list_buffer_contents)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.get()

buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.get()