class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    llist_1_node = llist_1.head
    llist_2_node = llist_2.head

    output = set()
    while(llist_1_node):
        output.add(llist_1_node.value)
        llist_1_node = llist_1_node.next

    while (llist_2_node):
        output.add(llist_2_node.value)
        llist_2_node = llist_2_node.next

    return sorted(output)


def intersection(llist_1, llist_2):
    # Your Solution Here
    llist_1_node = llist_1.head

    output = set()
    while (llist_1_node):
        value1 = llist_1_node.value
        llist_2_node = llist_2.head

        while (llist_2_node):
            value2 = llist_2_node.value
            if value1 == value2:
                output.add(value2)
                break
            llist_2_node = llist_2_node.next
        llist_1_node = llist_1_node.next

    return sorted(output)


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]


for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23, 1]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))