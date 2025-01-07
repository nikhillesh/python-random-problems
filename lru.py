class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # stores key -> node
        self.head = self.Node(0, 0)  # dummy head
        self.tail = self.Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the doubly linked list"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_front(self, node):
        """Insert a node right after the head (most recent)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """Return the value of the key if the key exists, else return -1"""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_at_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Insert a new key-value pair or update the value of an existing key"""
        if key in self.cache:
            # Remove the old node and insert the updated one
            node = self.cache[key]
            self._remove(node)
            node.value = value
            self._insert_at_front(node)
        else:
            # If the cache exceeds the capacity, remove the least recently used (LRU) node
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            # Insert the new node at the front
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self._insert_at_front(new_node)