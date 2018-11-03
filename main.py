

import math
import AVLTree
import RedBlackTree


# Asks user to decide between using an AVL or a R/B tree
def get_input():

    choice = None

    # Asking user which type of tree he would like to use
    while choice is not "0" and choice is not "1":
        choice = input("Would you like to use a R/B tree(0) or an AVL tree(1)? [0/1]")

        if choice is "0":
            return RedBlackTree

        elif choice is "1":
            return AVLTree

        print("Invalid input")


# Cosine similarity calculation
def cos_sim(rtree, key1, key2):
    node1 = rtree.search(key1)
    node2 = rtree.search(key2)

    dot_product = 0
    magnitude1 = 0
    magnitude2 = 0

    for i in range(len(node1.embedding)):
        dot_product = dot_product + (node1.embedding[i] * node2.embedding[i])

    for i in range(len(node1.embedding)):
        magnitude1 = magnitude1 + (node1.embedding[i] * node1.embedding[i])
        magnitude2 = magnitude2 + (node2.embedding[i] * node2.embedding[i])

    magnitude1 = math.sqrt(magnitude1)
    magnitude2 = math.sqrt(magnitude2)

    magnitude1 = magnitude1 * magnitude2

    return dot_product / magnitude1


# Method A count nodes in the tree
def count_nodes(root):

    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.right) + count_nodes(root.left)


# Method B determine height of the tree
def height(root):

    if root is None:
        return 0
    else:
        return 1 + height(root.left)


# Method C write keys
def write_afile(root, new_file):

    if root is None:
        return
    else:
        write_afile(root.left, new_file)
        new_file.write(root.key + "\n")
        write_afile(root.right, new_file)


# Method D write keys at depth
def write_dfile(root, new_file, depth):

    if root is None:
        return
    elif depth <= 0:
        new_file.write(root.key + "\n")
        return
    else:
        write_dfile(root.left, new_file, depth - 1)
        write_dfile(root.right, new_file, depth - 1)



# Opening file and initializing variables
tree_type = get_input()
file = "glove.6B.50d.txt"

# Filling AVLTree
if tree_type is AVLTree:
    tree = tree_type.AVLTree()

    with open(file) as dictionary:
        for line in dictionary:
            items = line.split()
            if 'a' <= items[0][0] <= 'z':
                for i in range(1, 51, 1):
                    items[i] = float(items[i])
                tree.insert(tree_type.Node(items.pop(0), items))

# Filling RedBlackTree
else:
    tree = tree_type.RedBlackTree()

    with open(file) as dictionary:
        for line in dictionary:
            items = line.split()
            if 'a' <= items[0][0] <= 'z':
                for i in range(1, 51, 1):
                    items[i] = float(items[i])
                tree.insert_node(tree_type.RBTNode(items.pop(0), None, items))

# Reading second file
with open("support.txt") as support:
    for line in support:
        print(line.split()[0] + " " + line.split()[1] + " " + str(cos_sim(tree, line.split()[0], line.split()[1])))

# Checking method A
print(count_nodes(tree.root))

# Checking method B
print(height(tree.root))

# Checking method C
with open("ascending_words.txt", "w") as ascending_file:
    write_afile(tree.root, ascending_file)

# Checking method D
with open("words_at_depth.txt", "w") as atdepth_file:
    write_dfile(tree.root, atdepth_file, 1)
