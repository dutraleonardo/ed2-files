#!/usr/bin/env python3
# AVL Tree in 'Data Structure and Algorithm Analysis' P.110
#
# Keypoint: After insertion, roatate the tree if AVL-condition is not reached.
#           Every node keep updated with the height information.
#

class BinaryTree(object):
    def __init__(self, content=-1):
        self.val = content
        self.left = None
        self.right = None

    @classmethod
    def _build_tree_string(cls, root, curr_index, index=False, delimiter='-'):
        """Recursively traverse down the binary tree build a pretty-print string.

        In each recursive call, a "box" of characters visually representing the
        current (sub)tree is constructed line by line. Each line is padded with
        whitespaces to ensure all lines in the box have the same length. Then the
        box, its width, and start-end positions of its root value repr (required
        for drawing branches) are sent up to the parent call. The parent call then
        combines its left and right sub-boxes to construct a larger box etc.

        :param root: The root node of the binary tree.
        :type root: binarytree.Node | None
        :param curr_index: The level-order_ index of the current node (root is 0).
        :type curr_index: int
        :param index: If set to True, include the level-order_ node indexes
            using the following format: ``{index}{delimiter}{value}``
            (default: False).
        :type index: bool
        :param delimiter: The delimiter character between the node index and value
            (default: '-').
        :type delimiter:
        :return: The box of characters visually representing the current subtree,
            the width of the box, and the start-end positions of the new root value
            repr string.
        :rtype: ([str], int, int, int)
        """
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if index:
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.val)
        else:
            node_repr = str(root.val)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = \
            cls._build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            cls._build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

        # Draw the branch connecting the current root to the left sub-box
        # Pad with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the current root to the right sub-box
        # Pad with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root positions
        return new_box, len(new_box[0]), new_root_start, new_root_end

    # def display(self):
    #     def print_tree(tree, depth):
    #         if tree:
    #             if depth:
    #                 print("|  " * (depth-1) + '+--+' +str(tree.val))
    #             else:
    #                 print('+' +str(tree.val))

    #             if tree.left or tree.right:
    #                 print_tree(tree.left, depth+1)
    #                 print_tree(tree.right, depth+1)
    #         else:
    #             print ("  " * depth + 'None')
        # call the recursive function
    @classmethod
    def display(cls, tree):
        lines = cls._build_tree_string(tree, 0, False, '-')[0][:-1]
        print('\n' + '\n'.join((line.rstrip() for line in lines)))

class AVL(BinaryTree):
    def __init__(self, content="EmptyNode"):
        self._height = 0
        super(AVL,self).__init__(content)

    @classmethod
    def createFromList(cls, in_list):
        if not in_list:
            return AVL()
        length, res = len(in_list), cls()
        for item in in_list:
            res = res.insert(item)
            cls.display(res)
        return res

    @classmethod
    def getHeight(cls, node):
        if isinstance(node, cls):
            return node._height
        else:
            return -1

    def makeEmpty(self):
        self.value = 'EmptyNode'
        self._height = 0
        self.left = None
        self.right = None

    def find(self, match):
        """
        find item in the AVL

        >>> import random
        >>> test = range(20)
        >>> random.shuffle(test)
        >>> bst = AVL.createFromList(test)
        >>> for x in xrange(20):
        ...     res = bst.find(x)
        ...     if res and res.val == x:
        ...         continue
        ...     else:
        ...         print x
        ...
        >>> bst.find(20) == None
        True
        >>> bst.find(21) == None
        True
        """
        this_tree = self
        while this_tree and match != this_tree.val:
            if match < this_tree.val:
                this_tree = this_tree.left
            else:
                this_tree = this_tree.right
        return this_tree if this_tree else None

    def findMin(self):
        """
        return the node with the smallest value
        """
        this_tree = self
        while this_tree.left:
            this_tree = this_tree.left
        return this_tree

    def findMax(self):
        """
        return the node with the largest value
        """
        this_tree = self
        while this_tree.right:
            this_tree = this_tree.right
        return this_tree

    def singleRotate(self, flag):
        """
        Single rotate to handle outer unbalance.
        Paras: flag = 0 -> left node unbalanced
               flag = 1 -> right node unbalanced
        """
        # Right node unbalanced
        print('RS({0})'.format(self.val))
        if flag:
            k1, k2 = self, self.right
            k1.right, k2.left = k2.left, k1
        # Left node unbalanced
        else:
            k1, k2 = self, self.left
            k1.left, k2.right = k2.right, k1

        k1._height = max(AVL.getHeight(k1.left), AVL.getHeight(k1.right)) + 1
        k2._height = max(AVL.getHeight(k2.left), AVL.getHeight(k2.right)) + 1
        return k2

    def doubleRotate(self, flag):
        """
        Single rotate to handle inner unbalance.
        Paras: flag = 0 -> left node unbalanced
               flag = 1 -> right node unbalanced
        """
        # Right node unbalanced
        print('DR({1})'.format(self.val))
        if flag:
            k1, k2, k3 = self, self.right, self.right.left
            k1.right, k2.left, k3.left, k3.right = \
                    k3.left, k3.right, k1, k2
        else:
            k1, k2, k3 = self, self.left, self.left.right
            k1.left, k2.right, k3.left, k3.right = \
                    k3.right, k3.left, k2, k1       
        k1._height = max(AVL.getHeight(k1.left), AVL.getHeight(k1.right)) + 1
        k2._height = max(AVL.getHeight(k2.left), AVL.getHeight(k2.right)) + 1
        k3._height = max(AVL.getHeight(k3.left), AVL.getHeight(k3.right)) + 1
        return k3

    def insert(self, content):
        """
        Should be called as avl = avl.insert()

        >>> avl = AVL.createFromList(xrange(1,8))
        >>> print AVL.getHeight(avl)
        2
        >>> avl = avl.insert(15)
        >>> avl = avl.insert(16)
        >>> avl = avl.insert(14)
        >>> print AVL.getHeight(avl)
        3
        """
        # When input_tree is an empty tree
        if self.val == "EmptyNode":
            self.val = content
            # self.root = self
            return self
        # Left subtree operation
        elif content < self.val:
            if self.left:
                self.left = self.left.insert(content)
                if AVL.getHeight(self.left) - AVL.getHeight(self.right) == 2:
                    # Single rotate when there is an outer case
                    if content < self.left.val:
                        self = self.singleRotate(0)
                    else:
                        self = self.doubleRotate(0)
            # If left subtree is None
            else:
                new_node = AVL(content)
                self.left = new_node

        # Right subtree operation
        else:
            if self.right:
                self.right = self.right.insert(content)
                if AVL.getHeight(self.right) - AVL.getHeight(self.left) == 2:
                    if content >= self.right.val:
                        self = self.singleRotate(1)
                    else:
                        self = self.doubleRotate(1)
            # If right subtree is None
            else:
                new_node = AVL(content)
                self.right = new_node
            # Keep searching through right subtree
        # Operation on height
        self._height = max(AVL.getHeight(self.left), AVL.getHeight(self.right)) + 1
        return self

    def _deleteMin(self, p_node):
        """
        this method is to support delete method, makes it efficient
        """
        this_tree = self
        while this_tree.left:
            p_node = this_tree
            this_tree = this_tree.left
        # this_tree is the node with the Min val
        if p_node.left and p_node.left.val == this_tree.val:
            # p_node.left -> this_tree
            p_node.left = this_tree.right
        else:
            p_node.right = this_tree.right
        return this_tree.val

    def delete(self, match):
        """
        should be called as bst = bst.deletion(XX)

        >>> my_avl = AVL()
        >>> item_set = range(20)
        >>> for i in xrange(4):
        ...     random.shuffle(item_set)
        ...     for item in item_set:
        ...         my_avl = my_avl.insert(item)
        ...     for i in xrange(20):
        ...         my_avl = my_avl.delete(i)
        ...     my_avl.display()
        ...
        +EmptyNode
        +EmptyNode
        +EmptyNode
        +EmptyNode
        """
        def _delete(self, match):
            if match < self.val:
                if self.left:
                    self.left = _delete(self.left, match)
                else:
                    raise ValueError("deletion node not found!!")
            elif match > self.val:
                if self.right:
                    self.right = _delete(self.right, match)
                else:
                    raise ValueError("deletion node not found!!")
            else:
                # need to delete this root node
                if self.right and self.left:
                    # this node has 2 children
                    self.val = self.right._deleteMin(self)
                else:
                    # this node has at most 1 children
                    self = self.right if self.right else self.left
            return self
        # if all nodes of the tree have been deleted, return EmptyNode
        # There exists EmptyNode in the tree only at ROOT of the Tree
        after_deletion = _delete(self, match)
        if after_deletion:
            return after_deletion
        else:
            return AVL()        

# if __name__ == "__main__":
#     import doctest
#     import random
#     doctest.testmod()
#     my_avl = AVL.createFromList(xrange(1,100))
#     my_avl.display() 