import sys


class Node:
    def __init__(self, freq, char=None):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
        self.char = char

    def is_left(self):
        return self.father.left == self


def count_freq(text):
    chars = []
    chars_freqs = []
    for i in range(0, len(text)):
        if text[i] in chars:
            pass
        else:
            chars.append(text[i])
            char_freq = (text[i], text.count(text[i]))
            chars_freqs.append(char_freq)
    return chars_freqs


def create_nodes(data_list):
    return [Node(data[1], data[0]) for data in data_list]


def get_tree(node_list):
    queue = node_list[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]


def get_codes(node_list, root, text, data_list):
    huffman_str = ''
    if len(node_list) > 1:
        codes = [''] * len(node_list)
        for i in range(len(node_list)):
            node_tmp = node_list[i]
            while node_tmp != root:
                if not node_tmp.is_left():
                    codes[i] = '0' + codes[i]
                else:
                    codes[i] = '1' + codes[i]
                node_tmp = node_tmp.father
        huffman_str = ''
        for char in text:
            i = 0
            for item in data_list:
                if char == item[0]:
                    huffman_str += codes[i]
                i += 1

        return huffman_str
    else:
        for i in range(len(text)):
            huffman_str += '1'
        return huffman_str


def huffman_encoding(text):
    if text:
        print("huffman_encoding start: ", text)
        data_list = count_freq(text)
        node_list = create_nodes(data_list)
        if len(node_list) == 1:
            huffman_str = get_codes(node_list, node_list[0], text, data_list)
            print("====>", huffman_str)
            return huffman_str, node_list[0]

        root = get_tree(node_list)

        huffman_str = get_codes(node_list, root, text, data_list)
        return huffman_str, root
    else:
        return '', None


def huffman_decoding(encoded_data, tree):
    output = ''
    if encoded_data and tree.char is None:
        output = ''
        node = tree
        for char in encoded_data:

            if char == '0':
                node = node.right
                if node.char:
                    output += node.char
                    node = tree

            elif char == '1':
                node = node.left
                if node.char:
                    output += node.char
                    node = tree

    else:
        for i in range(len(encoded_data)):
            output +=  tree.char
    return output


if __name__ == "__main__":
    codes = {}

    print("--- Test case 1 ---")
    a_great_sentence_1 = "abccc"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence_1)))
    print("The content of the data is: {}\n".format(a_great_sentence_1))

    encoded_data, tree = huffman_encoding(a_great_sentence_1)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("--- Test case 2 ---")
    a_great_sentence_2 = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence_2)))
    print("The content of the data is: {}\n".format(a_great_sentence_2))

    encoded_data, tree = huffman_encoding(a_great_sentence_2)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("--- Test case 3 ---")
    a_great_sentence_3 = None

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence_3)))
    print("The content of the data is: {}\n".format(a_great_sentence_3))

    encoded_data, tree = huffman_encoding(a_great_sentence_3)

    print("The size of the encoded data is: [", encoded_data, "]")
    print("The content of the encoded data is: [", encoded_data, "]")

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: [{}]\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: [{}]\n".format(decoded_data))

    print("--- Test case 4 ---")
    a_great_sentence_4 = "aaaaa"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence_4)))
    print("The content of the data is: {}\n".format(a_great_sentence_4))

    encoded_data, tree = huffman_encoding(a_great_sentence_4)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

