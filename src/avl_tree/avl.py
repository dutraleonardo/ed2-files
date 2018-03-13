#!/usr/bin/env python3
from binarytree import Node


class AvlTree:
    balanced_factor = 1

    def __init__(self, root=None, list_values=None):
        self.root = None if root is not None else root 
        if list_values is not None:
            self.bulk_insert(list_values)

    def bulk_insert(self, list_values):
        [self.insert(value) for value in list_values]

    def insert(self, value, node=None):
        self.root = Node(value) if (self.root is None and node is None) else self.root
        node = self.root if node is None else node
        bigger_than = value > node.value
        less_than = value < node.value

        if less_than and not (node.left is None):
            node = self.insert(value, node.left)
        elif less_than and node.left is None:
            node.left = Node(value)
            return  
        if bigger_than and not (node.right is None):
            print(node.value, self.root.value)
            node = self.insert(value, node.right)
        elif bigger_than and node.right is None:
            node.right = Node(value)
            return
        else:
            self._balance(node)
    
    def _balance(self, node):
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

        .. _level-order:
            https://en.wikipedia.org/wiki/Tree_traversal
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
