from sys import stdin

class node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

 

class binary_tree:

 

    def __init__(self):
        self.__root = None
        self.__duplicates = {}
        self.__indices = {}

 

    def predecessor(self, x):
        if x.left!= None:
            return self.max(x.left)
        y = x.parent
        while y != None and x==y.left:
            x = y
            y= y.parent
        return y 
        
    def min(self,x):
        while x.left != None:
            x = x.left
        return x
    def max(self,x):
        while x.right != None:
            x = x.right
        return x


 

    def successor(self, z):
        if x.right!= None:
            return self.min(x.right)
        y = x.parent
        while y != None and x==y.right:
            x = y
            y= y.parent
        return y 

 

    def insert(self, z):

        if z.val not in self.__duplicates:
            self.__duplicates[ z.val ] = True
            self.__indices[z.val]=1
            y = None
            x = self.__root
            while x != None:
                y = x
                if z.val < x.val:
                    x = x.left
                else:
                    x = x.right
            z.parent = y
            if y == None:
                self.__root = z
            elif z.val < y.val:
                y.left = z
            else:
                y.right = z
        else:
            self.__indices[z.val]+=1



    def delete(self, z):
        if z.left==None:
            self.transplant(self,z,z.right)
        elif z.right == None:
            self.transplant(self, z,z.left)
        else:
            y = self.min(z.right)
            if y  != z.right:
                self.transplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(self, z,y)
            y.left = z.left
            y.left.parent = y

    def transplant(self,x,z):
        if x.parent == None:
            self.__root = z
        elif x== x.parent.left:
            x.parent.left = z
        else: 
            x.parent.right = z
        if z!=None:
            z.parent = x.parent



 

    def inorder_walk(self, x):
        if x != None:
            self.inorder_walk(x.left)
            print(x.val + " " + str(self.__indices[x.val]))
            self.inorder_walk(x.right)

 

    def root(self):
        return self.__root

def main():
    test = int(stdin.readline().strip())
    tree = binary_tree()
    for _ in range(test):
        conquest = stdin.readline().split()
        print(conquest)
        tree.insert(node(conquest[0]))
    tree.inorder_walk(tree.root())


main()