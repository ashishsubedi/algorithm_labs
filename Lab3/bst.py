
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
        result = []
        self._inorder(self.root,result)
        return result

    def _inorder(self,p,result):
        if(p is not None):
            self._inorder(p.left,result)
            
            result.append(p.key)
            self._inorder(p.right,result)
        



    # Perform postorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 4, 3, 2].
    def postorder_walk(self):
        pass

        result = []
        self._postorder(self.root,result)
        

        return result

    def _postorder(self,p,result):
        if p is not None:
            self._postorder(p.left,result)
            self._postorder(p.right,result)
            result.append(p.key)
        return result

    # Perform preorder traversal. Must return a list of keys visited in inorder way, e.g. [2, 1, 3, 4].
    def preorder_walk(self):
        result = []
        if self.root is None: return result
        
        stack = []

        
        curr = self.root

        while True:
            while curr is not None:
            
                stack.append(curr)
                result.append(curr.key)
                curr = curr.left
            curr = stack.pop()            
            curr = curr.right
             

            if(len(stack) == 0 and curr is None): break

        return result




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

        p = self.root
        prev = None

        while p is not None:
            if p.key == key:
                # Delete key
                
                # If node has no child
                if p.left is None and p.right is None:
                    p = None
                    if prev == None:
                        self.root = None

                else:                    
                    # Check if right child exist and 
                    if p.right is None:
                        #No right child, assign prev child to p.left
                        if prev == None:
                            # Root is being deleted, update root
                            self.root = p.left

                        else:
                            if key < prev.key:
                                #left child of prev
                                prev.left = p.left
                                p = None
                            else:
                                prev.right = p.left
                                p = None

                    else:
                        # Since both child exist, swap with smallest node in right
                        temp = p.right
                        temp_prev = p 

                        #Could have called self.smallest() but need to keep track of previous node as well
                        while temp.left is not None:
                            temp_prev = temp
                            temp = temp.left

                        if(p.right == temp):
                            #temp is the right child of p
                            temp.left = p.left
                            p.right = None
                            del p

                            #Check if root is being deleted
                            if prev == None:
                                self.root = temp

                        else:
                            p.key = temp.key
                            p.value = temp.value

                            if(temp.key < temp_prev.key):
                                temp_prev.left = None

                            else:
                                
                                temp_prev.right = None
                        
                            del temp
                self._size -= 1
                return True 

            elif key < p.key:
                prev = p

                p = p.left

            else:
                prev = p
                p = p.right
            
        return False
        
       

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


