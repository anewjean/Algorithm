# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# def preorder(node):
#     if not node:
#         return
#     print(node.val, end='')
#     preorder(node.left)
#     preorder(node.right)

# def inorder(node):
#     if not node:
#         return
#     inorder(node.left)
#     print(node.val, end='')
#     inorder(node.right)

# def postorder(node):
#     if not node:
#         return
#     postorder(node.left)
#     postorder(node.right)
#     print(node.val, end='')

# # 입력 처리
# N = int(input())
# nodes = {}

# for _ in range(N):
#     root, left, right = input().split()

#     if root not in nodes:
#         nodes[root] = Node(root)
#     node = nodes[root]

#     if left != '.':
#         if left not in nodes:
#             nodes[left] = Node(left)
#         node.left = nodes[left]

#     if right != '.':
#         if right not in nodes:
#             nodes[right] = Node(right)
#         node.right = nodes[right]

# # 문제 조건상 'A'가 항상 루트
# root = nodes['A']

# preorder(root)
# print()
# inorder(root)
# print()
# postorder(root)






























class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder_traversal(node: Node) -> None:
    """
    root -> left -> right
    """
    if not node:
        return
    print(node.val, end="")
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node: Node) -> None:
    """
    left -> root -> right
    """
    if not node:
        return
    inorder_traversal(node.left)
    print(node.val, end="")
    inorder_traversal(node.right)

def postorder_traversal(node: Node) -> None:
    """
    left -> right -> root
    """
    if not node:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.val, end="")

N = int(input())
nodes = {}

for _ in range(N):
    root, left, right = input().split()
    
    if root not in nodes:
        nodes[root] = Node(root)
    node = nodes[root]

    if left != '.':
        if left not in nodes:
            nodes[left] = Node(left)
        node.left = nodes[left]

    if right != '.':
        if right not in nodes:
            nodes[right] = Node(right)
        node.right = nodes[right]

root = nodes['A']

preorder_traversal(root) 
print()
inorder_traversal(root) 
print()
postorder_traversal(root)