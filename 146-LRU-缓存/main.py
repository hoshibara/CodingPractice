from lib2to3.fixes.fix_metaclass import remove_trailing_newline


class Block:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.head = Block(None, None)
        self.tail = Block(None, None, left=self.head)
        self.head.right = self.tail

    def get(self, key: int) -> int:
        if key in self.map:
            self.renew(self.map[key])
            return self.map[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].value = value
            self.renew(self.map[key])
        else:
            tmp = Block(key, value, left=self.head, right=self.head.right)
            tmp.left.right = tmp
            tmp.right.left = tmp
            self.map[key] = tmp
            while len(self.map) > self.capacity:
                self.pop()

    def renew(self, block):
        block.left.right = block.right
        block.right.left = block.left
        block.left = self.head
        block.right = self.head.right
        block.left.right = block
        block.right.left = block

    def pop(self):
        block = self.tail.left
        block.left.right = self.tail
        self.tail.left = block.left
        self.map.pop(block.key)
        del block

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
