def count_child_nodes(root):
    if root is None:
        return 0
    return 1 + count_child_nodes(root.left_leg) + count_child_nodes(root.right_leg)