import binary_search_tree
import unittest


class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")

    def test_balanced_binary_search_tree_two(self):
        print("\n")
        print("tree_insert_with_individual_check_two")
        t = lab3.Tree()

        t.insert(20)
        t.insert(10)
        t.insert(40)
        t.insert(5)
        t.insert(15)
        t.insert(25)
        t.insert(75)
        t.insert(3)
        t.insert(7)
        t.insert(12)
        t.insert(16)
        t.insert(24)
        t.insert(30)
        t.insert(65)
        t.insert(90)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 20)

        self.assertEqual(t.root.left.data, 10)
        self.assertEqual(t.root.left.left.data, 5)
        self.assertEqual(t.root.left.left.left.data, 3)
        self.assertEqual(t.root.left.left.right.data, 7)
        self.assertEqual(t.root.left.right.data, 15)
        self.assertEqual(t.root.left.right.right.data, 16)
        self.assertEqual(t.root.left.right.left.data, 12)

        self.assertEqual(t.root.right.data, 40)
        self.assertEqual(t.root.right.left.data, 25)
        self.assertEqual(t.root.right.left.left.data, 24)
        self.assertEqual(t.root.right.left.right.data, 30)
        self.assertEqual(t.root.right.right.data, 75)
        self.assertEqual(t.root.right.right.right.data, 90)
        self.assertEqual(t.root.right.right.left.data, 65)

        print("\n")

    def test_unbalanced_binary_search_tree(self):
        print("\n")
        print("test_unbalanced_bst")
        t = lab3.Tree()

        t.insert(50)
        t.insert(40)
        t.insert(80)
        t.insert(30)
        t.insert(47)
        t.insert(22)
        t.insert(35)
        t.insert(25)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 50)
        self.assertEqual(t.root.left.data, 40)
        self.assertEqual(t.root.left.left.data, 30)
        self.assertEqual(t.root.left.right.data, 47)
        self.assertEqual(t.root.right.data, 80)
        self.assertEqual(t.root.left.left.left.data, 22)
        self.assertEqual(t.root.left.left.left.right.data, 25)
        self.assertEqual(t.root.left.left.right.data, 35)

        print("\n")

    def test_skewed_left_binary_search_tree(self):
        print("\n")
        print("test_skewed_left_bst")
        t = lab3.Tree()

        t.insert(100)
        t.insert(50)
        t.insert(35)
        t.insert(2)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 100)
        self.assertEqual(t.root.left.data, 50)
        self.assertEqual(t.root.left.left.data, 35)
        self.assertEqual(t.root.left.left.left.data, 2)

        print("\n")

    def test_skewed_right_binary_search_tree(self):
        print("\n")
        print("test_skewed_right_bst")
        t = lab3.Tree()

        t.insert(5)
        t.insert(100)
        t.insert(1000)
        t.insert(1234)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 5)
        self.assertEqual(t.root.right.data, 100)
        self.assertEqual(t.root.right.right.data, 1000)
        self.assertEqual(t.root.right.right.right.data, 1234)

        print("\n")

class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

    def test_if_min_is_left_most_node(self):
        print("\n")
        print("Checkin if the min is the left most node")
        t = lab3.Tree()

        t.insert(20)
        t.insert(10)
        t.insert(30)
        t.insert(5)
        t.insert(15)
        t.insert(25)
        t.insert(35)

        minimum = t.min()
        self.assertEqual(t.root.left.left.data, minimum)

        print("\n")

    def test_if_max_is_right_most_node(self):
        print("\n")
        print("Checkin if the max is the right most node")
        t = lab3.Tree()

        t.insert(20)
        t.insert(10)
        t.insert(30)
        t.insert(5)
        t.insert(15)
        t.insert(25)
        t.insert(35)

        maximum = t.max()
        self.assertEqual(t.root.right.right.data, maximum)

        print("\n")

    def max_on_empty_tree(self):
        print("\n")
        print("Checkin if the None returns on an empty tree calling max")
        t = lab3.Tree()

        maxim = t.max()
        self.assertEqual(maxim, None)

    def min_on_empty_tree(self):
        print("\n")
        print("Checkin if the None returns on an empty tree calling min")
        t = lab3.Tree()

        minim = t.max()
        self.assertEqual(minim, None)


class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")


    def test_postorder_of_unbalanced_tree(self):
        print("\n")
        print("test_postorder_of_unbalanced_tree")
        t = lab3.Tree()

        t.insert(50)
        t.insert(40)
        t.insert(80)
        t.insert(30)
        t.insert(47)
        t.insert(22)
        t.insert(35)
        t.insert(25)

        postorder = [node for node in t.postorder()]
        self.assertEqual(postorder, [25, 22, 35, 30, 47, 40, 80, 50])
        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function


        print("\n")

class T3_successor(unittest.TestCase):

    def test_contains_and__find_node(self):
        print("\n")
        print("Contains method which uses the __find_node private method")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        checkT = tree_success.contains(6)
        checkF1 = tree_success.contains(50)
        checkF2 = tree_success.contains(2)
        self.assertEqual(checkT, True)
        self.assertEqual(checkF1, False)
        self.assertEqual(checkF2, False)

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")

    def required_test_successor(self):
        print("\n")
        print("Successor function after putting in 5, 4, 1, 9, 6, 2, 0 and finding Node(2)")

        tree_success = lab3.Tree()
        tree_success.insert(5)
        tree_success.insert(4)
        tree_success.insert(1)
        tree_success.insert(9)
        tree_success.insert(6)
        tree_success.insert(2)
        tree_success.insert(0)

        this_test = tree_success.find_successor(2).data
        self.assertEqual(this_test, 4)


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]

        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

    def test_delete_with_no_nodes(self):
        print("\n")
        print("test delete with no nodes in the tree")
        t = lab3.Tree()

        with self.assertRaises(KeyError):
            t.delete(7)

    def test_delete_on_tree_w_only_root(self):
        print("\n")
        print("test delete with only the root node in the tree")
        t = lab3.Tree()
        t.insert(25)

        self.assertEqual(t.delete(25), None)

class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

    def test_contains_with_no_node(self):
        print("\n")
        print("contains when it doesnt exist")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        self.assertEqual(t.contains(13), False)
        print("\n")

if __name__ == '__main__' :
    unittest.main()
