#Esteban Figueroa 2190057

import sys 

#clase nodo
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 

###funciones auxiliares###
#altura
def getHeight(node):
    if not node:
        return 0
    return node.height
#balance
def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)
#actualizar altura
def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))
#rotar derecha
def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x
#rotar izquierda
def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y
#hallar la hoja mas a la izquierda
def min_value_node(nodo):
    actual=nodo
    while actual.left is not None:
        actual = actual.left

    return actual


#borrar nodo
def delete(self,value):
    if self is None:
        return self
    if value>self.value:
        self.left = delete(self.left,value)
    elif value<self.value:
        self.right = delete(self.right,value)
    else:
        if self.left is None or self.right is None:
            temp=self.left if self.left else self.right

            if temp is None:
                self = None
            else:
                self = temp
        
        else:
            temp = min_value_node(self.right)
            self.value = temp.value
            self.right = delete(self.right,temp.value)

    if self is None:
        return self

    self.height = max(getHeight(self.left),getHeight(self.right))+1

    balance = getBalance(self)

    #caso izquierda izquierda
    if balance > 1 and getBalance(self.left) >= 0:
        return rotate_right(self)
    #caso izquierda derecha
    if balance > 1 and getBalance(self.left) < 0:
        self.left = rotate_left(self.left)
        return rotate_right(self)
    #caso derecha derecha
    if balance < -1 and getBalance(self.right) <=0:
        return rotate_left(self)
    #caso derecha izquierda
    if balance < -1 and getBalance(self.right) > 0:
        self.right = rotate_right(self.right)
        return rotate_left(self)

    return self


#recorrido in order
def inorder(self):
    if self is None:
        return

    inorder(self.left)

    print(self.value, end=' ')

    inorder(self.right)


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)
        
    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value: 
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 

        updateHeight(node)

        balance = getBalance(node)
        if balance > 1 and getBalance(node.left) >= 0:
            rotate_right(node) 
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            rotate_right(node) 
        elif balance < -1 and getBalance(node.right) <= 0:
            rotate_left(node)
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            rotate_left(node) 

        return node 





avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")

inorder(avl.root)
