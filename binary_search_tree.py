class Node:

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def add(self,current,value):
        if self.root is None:
            self.root=Node(value)
        else:
            if value < current.value:
                if current.left == None:
                    current.left = Node(value)
                else:
                    self.add(current.value,value)
            else:
                if current.right == None:
                    current.right = Node(value)
                else:
                    self.add(current.value,value)



