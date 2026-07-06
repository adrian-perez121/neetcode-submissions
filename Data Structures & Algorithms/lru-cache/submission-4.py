class Node:
    def __init__(self, key, value, front=None, back=None):
        self.key = key
        self.value = value
        self.front = front
        self.back = back


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = {}
        self.head = None
        self.tail = None
        self.size = 0

    def remove(self, node):
        if node.back:
            node.back.front = node.front
        else:
            self.head = node.front

        if node.front:
            node.front.back = node.back
        else:
            self.tail = node.back

    def append(self, node):
        node.front = None
        node.back = self.tail

        if self.tail:
            self.tail.front = node
        else:
            self.head = node

        self.tail = node

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1

        node = self.items[key]
        if node != self.tail:
            self.remove(node)
            self.append(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            node = self.items[key]
            node.value = value
            if node != self.tail:
                self.remove(node)
                self.append(node)
            return

        node = Node(key, value)
        self.items[key] = node
        self.append(node)
        self.size += 1

        if self.size > self.capacity:
            old_head = self.head
            self.remove(old_head)
            del self.items[old_head.key]
            self.size -= 1