# Problem Set 4A
# Name: ayush
# Collaborators: 

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(1, Node(2), Node(5, Node(7), Node(8)))
tree2 = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6)))
tree3 = Node(10, Node(5, Node(3), Node(7)), Node(20, Node(15), Node(30)))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    if tree is None:
        return -1
    
    left_height = find_tree_height(tree.get_left_child())
    right_height = find_tree_height(tree.get_right_child())
    
    return 1 + max(left_height, right_height)

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min heap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    if tree is None:
        return True

    left = tree.get_left_child()
    right = tree.get_right_child()

    if left is not None and not compare_func(left.get_value(), tree.get_value()):
        return False
    if right is not None and not compare_func(right.get_value(), tree.get_value()):
        return False

    return is_heap(left, compare_func) and is_heap(right, compare_func)


if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
