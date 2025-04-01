from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if index < 0 or not isinstance(node, Node):
        raise TypeError
    for i in range(index):
        if node.next == None:
            raise TypeError
        node = node.next
    return node
  