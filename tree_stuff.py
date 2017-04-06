"""
This module has all the  stuff for making the graph
at the moment its just the node class - should i put it with the syntax part?

"""

class Tree():
    def __init__(self):
        self.start = None
        self.current = None

    def traverse(self):
        """self.start.print_node()
        current = self.start
        while current.has_children():
            current.print_node()
            current = current.left_child"""

def traverse_tree(node):
    #print the node
    print('node contents ', node.contents)
    if node.left_child:
        print('left child: ', node.left_child.contents,)
    if node.right_child:
        print('right child ', node.right_child.contents)
    print('\n')
    #recurse on left child
    if node.left_child:
        traverse_tree(node.left_child)
    #recurse on right child
    if node.right_child:
        traverse_tree(node.right_child)

# node parents class - later will have child class for each type of token?
class Node():
    def __init__(self):
        self.contents = None
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.content_type = None #later will use child(?) classes instead of this


    def add_contents(self, contents):
        self.contents = contents

    def add_child(self, child):
        #add child node and return child!
        if self.left_child == None:
            self.left_child = child
            self.left_child.parent = self
            return self.left_child
        else:
            self.right_child = child
            self.right_child.parent = self
            return self.right_child

    def add_child_with_contents(self, contents, child):
        child = self.add_child(child)
        child.contents = contents

    def print_node(self):
        indent = ' ' * self.indent
        print('node: ', self.contents)
        print('children: ', self.left_child.contents, self.right_child.contents)

    def has_children(self):
        if self.left_child != None or self.right_child != None:
            return True
        else:
            return False
