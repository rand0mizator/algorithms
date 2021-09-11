from heapq import heappop, heappush, heapify


def parse_string(string):
    """parsing input string in list of this kind: [number of times letter appears in string, letter]"""
    letters = {}
    for char in string:
        if char not in letters.keys():
            letters[char] = 1
        else:
            letters[char] += 1
    letters = [(freq, letter) for letter, freq in letters.items()]
    letters.sort(key=lambda l: l[0])
    return letters


def make_tree(letters):
    """
    Makes binary tree using min heap (priority queue). Root of tree - sum of all frequencies of letters.
    Nodes - sum of frequencies of their children.
    """
    heap = []
    for letter in letters:
        heappush(heap, [letter])
    while len(heap) > 1:
        child0 = heappop(heap)
        child1 = heappop(heap)
        freq0, label0 = child0[0]
        freq1, label1 = child1[0]
        freq = freq0 + freq1
        label = label0 + label1
        node = [(freq, label), child0, child1]
        heappush(heap, node)
    return heap.pop()


def traverse_tree(code_tree, code_map, code_prefix):
    """
    Traverses tree by its edges adding 0 for left child of node, and 1 for right child.
    """
    if len(code_tree) == 1:
        freq, label = code_tree[0]
        code_map[label] = code_prefix
    else:
        value, child0, child1 = code_tree
        traverse_tree(child0, code_map, code_prefix + '0')
        traverse_tree(child1, code_map, code_prefix + '1')


def make_code_map(code_tree):
    """
    makes code map according to binary tree. So most frequent characters in string (and top nodes in tree) has lowest
    byte code.
    Example:
        string = abacabad
        codes:
        a: 0
        b: 10
        c: 110
        d: 111
    """
    code_map = {}
    traverse_tree(code_tree, code_map, '')
    return code_map


def encoder(string, code_map):
    """encodes string using code_map"""
    encoded_string = ''
    for letter in string:
        encoded_string += code_map[letter]
    return encoded_string


def main():
    string = input()
    letters_list = parse_string(string)
    if len(letters_list) > 1:
        tree = make_tree(letters_list)
        code_map = make_code_map(tree)
        bin_str = encoder(string, code_map)
        print(len(letters_list), len(bin_str))
        for letter, code in sorted(code_map.items()):
            print(f"{letter}: {code}")
        print(bin_str)
    else:
        print(1, letters_list[0][0])
        print(f"{letters_list[0][1]}: 0")
        print(f"{'0' * letters_list[0][0]}")


if __name__ == '__main__':
    main()
