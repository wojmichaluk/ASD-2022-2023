#struktury z wykładu 14, wykorzystywane też w 5 i 15
#drzewo BST z operacjami
class BSTNode:
    def __init__(self,key=None,data=None):
        self.left=None
        self.right=None
        self.parent=None
        self.key=key
        self.data=data
        self.span=None #drzewa przedziałowe

def search(root,key):
    while root!=None:
        if root.key==key: return root
        elif key<root.key: root=root.left
        else: root=root.right
    return None

def insert(root,key,data=None):
    last=None
    while root!=None:
        last=root
        if root.key==key: return None
        elif key<root.key: root=root.left
        else: root=root.right
    node=BSTNode(key,data)
    node.parent=last
    if last.key>key: node.parent.left=node
    else: node.parent.right=node
    return node

def remove(root,key):
    pass
    """
    while root!=None:
        if root.key==key: break
        elif key<root.key: root=root.left
        else: root=root.right
    if root==None: return
    par=root.parent
    left=root.left
    right=root.right
    if left==None and right==None:
        if root==par.left: par.left=None
        else: par.right=None
    elif left==None:
        if root==par.left: par.left=root.right
        else: par.right=root.right
    elif right==None:
        if root==par.left: par.left=root.left
        else: par.right=root.left
    else:
        if root==par.right:
            if left.right==None:
                par.right=left
                left.right=right
                left.parent=par
                right.parent=left
            else:
                pre=pred(root)
                pre.parent.right=pre.left
                par.right=pre
                pre.left
        elif root==par.left:
            if right.left==None:
                par.left=right
                right.left=left
                right.parent=par
                left.parent=right
            else:
                suc=succ(root)
                suc.parent.left=suc.right
                par.left=suc
                suc.right=right
                right.parent=suc
                suc.left=left
                left.parent=suc
    """

def min_key(root):
    while root.left!=None:
        root=root.left
    return root

def max_key(root):
    while root.right!=None:
        root=root.right
    return root

def pred(node):
    if node.left!=None:
        return max_key(node.left)
    par=node.parent
    while par!=None:
        if par.right==node: break
        node=par
        par=node.parent
    return par

def succ(node):
    if node.right!=None:
        return min_key(node.right)
    par=node.parent
    while par!=None:
        if par.left==node: break
        node=par
        par=node.parent
    return par

#drzewo czerwono-czarne
#podręcznik Cormena
