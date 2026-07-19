'''
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

    LRUCache(int capacity) Initialize the LRU cache of size capacity.
    int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1)O(1) average time complexity.

Example 1:

Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);      // return -1 (not found)

Constraints:

    1 <= capacity <= 100
    0 <= key <= 1000
    0 <= value <= 1000
'''
class Node:
    def __init__(self, key, value, next = None, previous = None):
        self.key = key
        self.value = value
        self.previous = previous
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.map_nodes = {}
        self.usage_list = None
        self.capacity = capacity
        self.head = None
        self.tail = None

    def _get(self, key: int) -> Node:
        node = self.map_nodes.get(key, None)
        if  node is not None and node != self.head:
            if node.next is None:
                if node.previous is not None:
                    self.tail = node.previous
                    self.tail.next = None
            else:
                node.next.previous = node.previous

            if node.previous is not None:
                prev = node.previous
                prev.next = node.next
            
            node.previous = None
            node.next = self.head
            self.head.previous = node
            self.head = node

        return node

    def get(self, key: int) -> int:
        node = self._get(key)
        return node.value if node is not None else -1
        

    def put(self, key: int, value: int) -> None:
        # print('put')
        node = self._get(key)
        if node is not None:
            node.value = value
            return

        if self.capacity == 0:
            # print('capacity 0')
            # print(f'{self.map_nodes.keys()=}')
            if self.tail is not None:
                del self.map_nodes[self.tail.key]
                if len(self.map_nodes) == 0:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = None

                self.capacity += 1


        new_node = Node(key, value) 

        # print(f'{self.map_nodes.keys()=}')
        # print('adding node')
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.map_nodes[key] = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self.map_nodes[key] = new_node

        self.capacity -= 1
        # print(f'{self.head=}, {self.tail=}')
                

        
