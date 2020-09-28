from doubly_linked_list import DoublyLinkedList 

# create the class
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == 0:
            if not self.storage.head:
                self.storage.add_to_tail(item)

            else:
                self.storage.head.value = item 

        else:
            i = 0
            current_node = self.storage.head 
            while i < self.current:
                if not current_node.next:
                    self.storage.add_to_tail(item)
                else:
                    current_node = current_node.next
                    i += 1
            current_node.value = item
        self.current += 1

        if self.current >= self.capacity:
            self.current = 0

    def get(self):
        list_buffer_contents = []

        start_node = self.storage.head
        list_buffer_contents.append(start_node.value)
        while start_node.next is not None:
            start_node = start_node.next 
            list_buffer_contents.append(start_node.value)
        return list_buffer_contents



