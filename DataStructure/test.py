

# 统计字符出现频率，生成映射表
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
    print("chars_freqs: ", chars_freqs)
    return chars_freqs


# 节点类
class Node:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def isLeft(self):
        return self.father.left == self


# 创建叶子节点
def createNodes(freqs):
    return [Node(freq) for freq in freqs]


# 创建Huffman树
def createHuffmanTree(nodes):
    queue = nodes[:]
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


# Huffman编码
def huffmanEncoding(nodes, tree):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != tree:
            if node_tmp.isLeft():
                codes[i] = '1' + codes[i]
            else:
                codes[i] = '0' + codes[i]
            node_tmp = node_tmp.father
    return codes


# 编码整个字符串
def encodeStr(text, chars_freqs, codes):
    print(codes)
    huffmanStr = ''
    for char in text:
        i = 0
        print("===", chars_freqs)
        for item in chars_freqs:
            if char == item[0]:
                huffmanStr += codes[i]
                print('huffmanStr:', huffmanStr)
            i += 1
            print('i: ', i)
    return huffmanStr


# 解码整个字符串
def decodeStr(huffmanStr, chars_freqs, codes):
    orignStr = ''
    while huffmanStr != '':
        i = 0
        for item in codes:
            if item in huffmanStr:
                if huffmanStr.index(item) == 0:
                    orignStr += chars_freqs[i][0]
                    huffmanStr = huffmanStr[len(item):]
            i += 1
    return orignStr


if __name__ == '__main__':
    text = 'abbccc'
    chars_freqs = count_freq(text)
    nodes = createNodes([item[1] for item in chars_freqs])
    tree = createHuffmanTree(nodes)
    codes = huffmanEncoding(nodes, tree)
    huffmanStr = encodeStr(text, chars_freqs, codes)
    orignStr = decodeStr(huffmanStr, chars_freqs, codes)
    print("code: ", codes)
    print('Encode result:' + huffmanStr)
    print('Decode result:' + orignStr)