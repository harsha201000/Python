# Import Statements
import turtle
import random

# TreeNode class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Draawing the tree
def draw_binary_tree(node, depth, branch_len, t):
    if depth == 0:
        return

    t.color(random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'cyan']))
    t.forward(branch_len)
    t.left(30)
    draw_binary_tree(node.left, depth - 1, branch_len * 0.7, t)
    t.right(60)
    draw_binary_tree(node.right, depth - 1, branch_len * 0.7, t)
    t.left(30)
    t.backward(branch_len)

# Generating the Binary Tree
def generate_binary_tree(depth):
    if depth == 0:
        return None
    
    root = TreeNode(random.randint(1, 100))
    root.left = generate_binary_tree(depth - 1)
    root.right = generate_binary_tree(depth - 1)
    return root

# Main Program
def draw_art():
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.bgcolor("white")

    t.left(90)
    t.up()
    t.backward(200)
    t.down()

    tree = generate_binary_tree(4)

    draw_binary_tree(tree, 4, 100, t)

    screen.mainloop()


draw_art()
