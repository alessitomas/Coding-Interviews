class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def in_order_succ(node: TreeNode) -> TreeNode:
    if not node:
        return None
    
    # Case 1: Node has a right subtree
    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr
    
    # Case 2: No right subtree, move up until we find a node that is a left child of its parent
    curr = node
    while curr.parent and curr == curr.parent.right:
        curr = curr.parent
    
    return curr.parent