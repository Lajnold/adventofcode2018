class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata


def load_input_file():
    with open('input.txt') as f:
        return list(map(int, f.read().strip().split()))


def parse_node(tree_def, start_idx):
    num_children = tree_def[start_idx]
    num_metadata = tree_def[start_idx + 1]
    i = start_idx + 2

    children = []
    while len(children) < num_children:
        child, child_consumed = parse_node(tree_def, i)
        children.append(child)
        i += child_consumed

    metadata = []
    while len(metadata) < num_metadata:
        metadata.append(tree_def[i])
        i += 1

    node = Node(children, metadata)
    consumed = i - start_idx
    return node, consumed


def traverse_tree(tree):
    yield tree
    for c in tree.children:
        yield from traverse_tree(c)


def node_value(node):
    if node.children:
        children_sum = 0
        for m in node.metadata:
            if 1 <= m <= len(node.children):
                children_sum += node_value(node.children[m - 1])
        return children_sum
    else:
        return sum(node.metadata)


def part1():
    tree_def = load_input_file()
    root, _ = parse_node(tree_def, 0)

    metadata_sum = 0
    for node in traverse_tree(root):
        metadata_sum += sum(node.metadata)

    print('Part 1: {}'.format(metadata_sum))


def part2():
    tree_def = load_input_file()
    root, _ = parse_node(tree_def, 0)

    print('Part 2: {}'.format(node_value(root)))


part1()
part2()
