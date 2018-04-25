from avl_tree.avl_weiss import AVL as avl_tree



tree = avl_tree()
root = tree.createFromList([45,89,56,20,2,4,9])
# print(root.val)
tree.display(root)