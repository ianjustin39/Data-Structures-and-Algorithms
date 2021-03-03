class Queue:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        # if queue is already full --> increase capacity
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()

        # enqueue new element
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1  # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0

    def front(self):
        # check if queue is empty
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]

        index = 0

        # copy all elements from front of queue (front-index) until end
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # case: when front-index is ahead of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # reset pointers
        self.front_index = 0
        self.next_index = index


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.q = Queue(capacity)
        self.map = dict()
        self.key_set = []

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.map.keys():
            self.set(key, self.map[key])
            return self.map[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.q.size() < 5:
            self.q.enqueue((key, value))
            self.map[key] = value
        else:
            data = self.q.dequeue()
            del self.map[data[1]]
            self.q.enqueue((key, value))
            self.map[key] = value


print('start')
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print("Test case 1: ", our_cache.get(1) == 1)       # returns 1
print("Test case 2: ", our_cache.get(2) == 2)       # returns 2
print("Test case 3: ", our_cache.get(9) == -1)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print("Test case 4: ", our_cache.get(3) == -1)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry