class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# enter -1 when don't want to create node
def create_BT():
    val = int(input("Enter the value :"))
    if val == -1:
        return None

    root = TreeNode(val)
    print(f"Enter the left child of {val} : ")
    root.left = create_BT()
    print(f"Enter the right child of {val} : ")
    root.right = create_BT()

    return root

def preorder(root):
    if root == None:
        return
    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)


root = create_BT()
print("\n\nPreorder Traversal : ")
preorder(root)

