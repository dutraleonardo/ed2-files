#!/usr/bin/env python3
# from binarytree import Node


class Node(object):
    def __init__(self, value, left=None, right=None):

        """Basic node representation
            :param value: key value node
            :param left: left node object of the current node( self )
            :param right: right node object of the current node( self )
        """
        self.value = value
        self.left = left
        self.right = right
        self.height = 0
    
    def __str__(self):
        return str(self.value)


class AvlTree:
    balanced_factor = 1

    # def __init__(self, nodes=None):
    #     self.nodes = []
    #     if nodes is not None:
    #         self.bulk_insert(nodes)

    def __init__(self, root=None, list_values=None):
        self.root = None if root is not None else root 
        # self.nodes = []
        if list_values is not None:
            self.bulk_insert(list_values)

    def _height(self, node):
        return node.height if node is not None else -1
        
    def bulk_insert(self, list_values):
        """insert a collections of nodes"""
        # t = self.insert(list_values[0])
        # for item in list_values[1:]:
        #     print(t.value)
        #     t = self.insert(item,t)
        [self.insert(item) for item in list_values]
            

    def insert(self, value, current_node=None):
        """Basic insertion of one node in essential Binary tree
            :param value: value's node
            :param node: current node which the child node(node value) is associated ( left or right)
        """
        # node = self.root if node is None else node
        

        if current_node is None:
            current_node = self.root if self.root is not None else None
            
        else:
<<<<<<< HEAD
            pass
            # self.root = current_node if self.root is None else self.root
            
        bigger_than = value > current_node.value
        less_than = value < current_node.value

        if less_than:
            current_node.left = self.insert(value, current_node.left)
            current_node = self._balance(current_node)

        if bigger_than:
            current_node.right = self.insert(value, current_node.right)
            current_node = self._balance(current_node)

        current_node.height = max(self._height(current_node.left), self._height(current_node.right)) + 1
        return current_node
=======
            return self._balance(node)
>>>>>>> patter node added
    
    def _balance(self, node):
        print('node to balance: ' + str(node.value))
        if node is None:
            return None
        
        if self._height(node.left) - self._height(node.right) > 1:
            if self._height(node.left.left) >= self._height(node.left.right):
                node = self._rotate_with_left_child(node)
            else:
                node = self._double_with_left_rotate(node)
            # node = self._rotate_with_left_child(node) \
            # if self._height(node.left.left) >= self._height(node.left.right) else \
            # self._double_with_left_rotate(node)
        
        elif self._height(node.right) - self._height(node.left) > 1:
            if self._height(node.right.right) >= self._height(node.right.left):
                node = self._rotate_with_right_child(node)
            else:
                node = self._double_with_right_rotate(node)
            # node = self._rotate_with_right_child(node)
            # if self._height(node.right.right) >= self._height(node.right.left) else \
            # self._double_with_right_rotate(node)
        
        # node.height = max(self._height(node.left), self._height(node.right)) + 1
        return node
    
    def _rotate_with_left_child(self, node):
        print('test')
        aux_node = node.left
        node.left = aux_node.right
        aux_node.right = node
        node.height = max(self._height(node.left), self._height(node.right) ) + 1
        aux_node.height = max(self._height(aux_node.left), node.height) + 1
        return aux_node

    def _rotate_with_right_child(self, node):
        pass
    
    def _double_with_left_rotate(self, node):
        pass
    
    def _double_with_right_rotate(self, node):
        pass

    def _build_tree_string(self, root, curr_index, index=False, delimiter='-'):
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
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.value)
        else:
            node_repr = str(root.value)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = \
            self._build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            self._build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

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

    def display(self):
        lines = self._build_tree_string(self.root, 0, False, '-')[0]
        print('\n' + '\n'.join((line.rstrip() for line in lines)))

    def _method(self):
        return self.insert.__name__
