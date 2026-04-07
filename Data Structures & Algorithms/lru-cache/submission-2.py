class Node:
    def __init__(self):
        self.key = None
        self.val = []
        self.next_ptr = None
        self.prev_ptr = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next_ptr = self.tail
        self.tail.prev_ptr = self.head
        self.capacity = capacity
        self.myDict = {}
    
    def _remove(self, key):
        node = self.myDict[key]
        print(f"Removing node: {key} value: {node.val}")
        prev_node = node.prev_ptr
        next_node = node.next_ptr

        prev_node.next_ptr = next_node
        if next_node != None:
            next_node.prev_ptr = prev_node
        node.next_ptr = None
        node.prev_ptr = None
        self.myDict.pop(key)
        
    
    def _add(self, key, val):
        new_node = Node()
        new_node.key = key
        new_node.val = val

        first = self.head.next_ptr
        new_node.next_ptr = first
        new_node.prev_ptr = self.head
        first.prev_ptr = new_node
        self.head.next_ptr = new_node

        self.myDict[key] = new_node


    def get(self, key: int) -> int:
        print(f"Get called key: {key}")
        if key in self.myDict:
            node = self.myDict[key]
            val = node.val
            self._remove(key)
            self._add(key, val)
            value = node.val
            print(f"Get method result: {value}")
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        print(f"Put called on key:{key} and value:{value}")
        if key in self.myDict:
            node = self.myDict[key]
            self._remove(key)
            self._add(key, value)
        else:
            if len(self.myDict) >= self.capacity:
                # Remove the tail node
                print("Reaching capacity so removing node")
                prev_node = self.tail.prev_ptr
                self._remove(prev_node.key)
            self._add(key, value)


        
