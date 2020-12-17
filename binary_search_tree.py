class Node(object):
    """
    Initialize a Node.

    Parent, left, right is set to None and can be updated later.
    The data is defined when initialized as an argument.
    """
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        """
        Binary Search Tree

        Supports most standard heap operations (print, insert, delete, find node, min, max, traverse, find successor).
        Since Python doesn't have built-in arrays, the underlying implementation uses a
        Python list instead. When initialized, only the root is defined as None, but it is redefined then the first
        Node is inserted.
        """
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)

    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)

    def insert(self, data):
        """
        Inserts an item to the BST

        data: item, a number, to be added to the BST

        Side effect: inserts an item at the correct spot in the BST
        Return: root node
        """
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is null, calling n.getData() will cause an error
        insert_node = Node(data)
        # First check if the insert_node is going to be the first node. If so, insert it at the root.
        if self.root is None:
            self.root = insert_node
            return
        # Now check the parent and see if this insert_node is greater or less than the parent.
        current_node = self.root
        while True:
            if current_node.data < insert_node.data:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = insert_node
                    current_node.right.parent = current_node
                    break
            else:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = insert_node
                    current_node.left.parent = current_node
                    break
        return self.root

    def min(self):
        """
        Finds the minimum value in the BST
        Goes left all the way in the tree.

        Return: minimum node data value
        """
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        # Base case
        if self.root is None:
            return None
        current_node = self.root
        # check that there is still a left and then redefine to that left until the loop goes as far left as possible
        while True:
            if current_node.left is not None:
                current_node = current_node.left
            else:
                break
        # Added .data because the Grade Scope tests seemed to deem it necessary
        return current_node.data

    def max(self):
        """
        Finds the maximum value in the BST
        Goes right all the way in the tree.

        Return: maximum node data value
        """
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        current_node = self.root
        while True:
            if current_node.right is not None:
                current_node = current_node.right
            else:
                break
        # Added .data because the Grade Scope tests seemed to deem it necessary
        return current_node.data

    def __find_node(self, data):
        """
        Finds the node with the data integer given as the argument.
        Returns: Node that has the data that was given as the methods parameter.
                 If the node does not exist it will return None
                 Also, if the root value is null it will return None
        """
        # returns the node with that particular data value else returns None
        # check base case
        temp = self.root
        if temp is None:
            return None
        # keep on updating the temp node and go right or left if necessary
        while temp:
            if temp.data < data:
                temp = temp.right
            elif temp.data > data:
                temp = temp.left
            # Case for temp is the Node with the data we want to find
            else:
                return temp

    def contains(self, data):
        """
        Checks if the tree contains a certain value
        Returns: Node that has the data that was given as the methods parameter.
                 If the node does not exist it will return None
                 Also, if the root value is null it will return None
        """
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        t_or_f = self.__find_node(data)

        if t_or_f is not None:
            # For testing purposes
            # print(t_or_f.data)
            return True
        else:
            # For testing purposes
            # print(t_or_f)
            return False

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        """
        Used by pre-, in-, and post-order methods to give an array of outputs from the BST in the correct
        order based on the traversal_type

        :param curr_node: gives the node that you want want to start the order at
        :param traversal_type: determines if it is in pre or post-order
        :return: nothing
        Side effect: prints out a python list of the nodes in correct order
        """
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        if curr_node is not None and traversal_type == 1:
            yield curr_node.data
            yield from self.__traverse(curr_node.left, 1)
            yield from self.__traverse(curr_node.right, 1)
        elif curr_node is not None and traversal_type == 2:
            yield from self.__traverse(curr_node.left, 2)
            yield curr_node.data
            yield from self.__traverse(curr_node.right, 2)
        elif curr_node is not None and traversal_type == 3:
            yield from self.__traverse(curr_node.left, 3)
            yield from self.__traverse(curr_node.right, 3)
            yield curr_node.data
        # Yield data of the correct node/s

    def find_successor(self, data):
        """
        returns the number one node higher than the node with data.
        Returns None if the node with data does not exist

        :param data: the node you want to find the successor of
        :return: Node with data closest to the data parameter but also greater than the data parameter
        """
        # helper method to implement the delete method but may be called on its own
        # if the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty,then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Return object of successor if found else return None

        node = self.__find_node(data)
        if node is None:
            return None
            # print("The node with that data does not exist")
            # raise RuntimeError
        if node.right is not None:
            baby = node.right
            while baby.left is not None:
                baby = baby.left
            return baby
        parent = node.parent
        while (parent is not None) and (node == parent.right):
            node = parent
            parent = node.parent
        return parent

    def num_children(self, data):
        """
        Helper method that tells how many kids a certain Node has.
        CREDIT: Jaeger Jochimsen, we were working together on this method and he discovered that this method could
        help shorten the delete method
        :param data: data of the node we want
        :return: tuple of 1 or 0s whether ther is zero, one, or two kids of the Node with data
        """
        node = self.__find_node(data)
        children = [0, 0]
        if node.right is not None:
            children[1] = 1
        if node.left is not None:
            children[0] = 1
        # Turn List to tuple
        return tuple(children)

    def delete(self, data):
        """
        Deletes the node with said data and rearranges the tree based on the deletion.

        :param data: the node data of the node that should be deleted
        :return: nothing
        Side effect: removes the node with data and rearranges the BST around the fact
        that the node with data is gone
        raises a key error if there is not a node with the data argument value.
        """
        # Find the node to delete.
        # If the value specified by delete does not exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to Null.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        node_to_delete = self.__find_node(data)
        # print(node_to_delete.data)
        # Base Case
        if node_to_delete is None:
            raise KeyError
        children = self.num_children(data)
        parent = node_to_delete.parent

        # CASE 1: If the node has no children
        if children == (0, 0):
            if parent is None:
                self.root = None
            elif parent.left is node_to_delete:
                parent.left = None
            else:
                parent.right = None

        # CASE 2: If the node has one child
        # RIGHT CHILD
        elif children == (0, 1):
            if parent is None:
                self.root = node_to_delete.right
                node_to_delete.right.parent = None
            elif parent.left is node_to_delete:
                parent.left = node_to_delete.right
                node_to_delete.right.parent = parent
            else:
                parent.right = node_to_delete.right
                node_to_delete.right.parent = parent

        # LEFT CHILD
        elif children == (1, 0):
            if parent is None:
                self.root = node_to_delete.left
                node_to_delete.left.parent = None
            elif parent.left is node_to_delete:
                parent.left = node_to_delete.left
                node_to_delete.left.parent = parent
            else:
                parent.right = node_to_delete.left
                node_to_delete.left.parent = parent

        # CASE 3: If the node has two children
        else:
            successor = self.find_successor(data)
            new_data = successor.data
            self.delete(successor.data)
            node_to_delete.data = new_data
