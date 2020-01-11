from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0

    def append(self, item):
        if self.size >= self.capacity:
            self.storage.remove_from_head()
            self.size -= 1

        self.storage.add_to_tail(item)
        self.size += 1


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        self.current = self.storage.head

        while self.current:
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next

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
buffer.get()