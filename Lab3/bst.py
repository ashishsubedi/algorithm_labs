
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        self._size = 0
        
    class Node:
        def __init__(self,key,value):
            self.left = None 
            self.right = None
            self.key = key
            self.value = value



   # Add a node to the BST
    def add(self, key, value):

        if self.root is None:
            self.root = self.Node(key,value)
        else:
            p = self.root
            while True:
                if(key<p.key):

                    if(p.left is not None):
                        p = p.left
                    else:
                        p.left = self.Node(key,value)
                        break
                else:
                    if(p.right is not None):

                        p = p.right
                    else:
                        p.right = self.Node(key,value)
                        break
        
        self._size += 1
    # Return the number of nodes in the BST
    def size(self):

        return self._size
    # Perform inorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 2, 3, 4].
    def inorder_walk(self):
        pass

    # Perform postorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 4, 3, 2].
    def postorder_walk(self):
        pass

    # Perform preorder traversal. Must return a list of keys visited in inorder way, e.g. [2, 1, 3, 4].
    def preorder_walk(self):
        pass

    # Search the BST for the given key. Return False if the key is not found.
    def search(self, key):
        p = self.root
        while p is not None:
            if (key == p.key):
                return p.value
            elif(key<p.key):
                p = p.left
            else:
                p = p.right  
        return False 


    # Remove a key from the BST. Return False if the key is not present in the BST.
    def remove(self, key):
        
        pass

    # Find the smallest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def smallest(self):
        p = self.root

        while(p.left is not None):
            p = p.left
        return(p.key,p.value)
    # Find the largest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def largest(self):

        p = self.root

        while(p.right is not None):
            p = p.right
        return(p.key,p.value)


