# define the node
class Node:

    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        # define capacity
        self.capacity = capacity

        # define dummy node
        self.dummy = Node()

        # define pre and next
        self.dummy.pre = self.dummy
        self.dummy.next = self.dummy
        
        # for search/get hash table
        self.key_to_dict = {}
        
    # first get the node
    def get_node(self, key):
        # if we do not have the key
        if key not in self.key_to_dict:
            return None
        # we have the key
        node = self.key_to_dict[key]
        # put the node at the first
        self.remove(node)
        self.push_front(node)
        return node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        # get the node
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        # put the node to the front
        node = self.get_node(key)
        
        # if exist
        if node:
            node.value = value
            return
        
        # if it is new, start new node
        self.key_to_dict[key] = node = Node(key, value)
        self.push_front(node)

        # if the capacity is full
        if len(self.key_to_dict) > self.capacity:
            # delete the last in list
            back_node = self.dummy.pre
            del self.key_to_dict[back_node.key]
            self.remove(back_node)
        
    # remove node process
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    # add the node to the front
    def push_front(self, node):
        node.pre = self.dummy
        node.next = self.dummy.next
        self.dummy.next = node
        node.next.pre = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
