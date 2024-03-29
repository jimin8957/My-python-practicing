
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

root_node = Node("A")

node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")
node_h = Node("H")

root_node.left_child = node_b
root_node.right_child = node_c
node_b.left_child = node_d
node_b.right_child = node_e
node_e.left_child = node_g
node_e.right_child = node_h
node_c.right_child = node_f

# 실행 코드
test_node = root_node.right_child.right_child
print(test_node.data)

test_node = root_node.left_child.right_child.left_child
print(test_node.data)

test_node = root_node.left_child.right_child.right_child
print(test_node.data)