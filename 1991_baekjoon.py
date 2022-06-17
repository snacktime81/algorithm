import sys

class Node:
    def __init__(self, right, left, root):
        if(right == '.'):
            self.right = None
        else:
            self.right = right
        if(left == '.'):
            self.left = None
        else:
            self.left = left
        self.root = root
    def getR(self):
        return self.right
    def getL(self):
        return self.left
    def getRoot(self):
        return self.root
    def setR(self, r):
        self.right = r
    def setL(self, l):
        self.left = l


def preorder(node):
    if(node == None):
        return
    print(node.getRoot(), end='')
    preorder(node.getL())
    preorder(node.getR())

def inorder(node):
    if(node == None):
        return
    inorder(node.getL())
    print(node.getRoot(), end='')
    inorder(node.getR())

def postorder(node):
    if(node == None):
        return
    postorder(node.getL())
    postorder(node.getR())
    print(node.getRoot(), end='')


tc = int(sys.stdin.readline())
li = []
for i in range(tc):
    rt, le, ri = map(str, sys.stdin.readline().split())
    n = Node(ri, le, rt)
    li.append(n)

for i in range(0, len(li)):
    l = li[i].getL()
    r = li[i].getR()
    for j in li:
        if(j.getRoot() == l):
            li[i].setL(j)
        elif(j.getRoot() == r):
            li[i].setR(j)


preorder(li[0])
print()
inorder(li[0])
print()
postorder(li[0])

