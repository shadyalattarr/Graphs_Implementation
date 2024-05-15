# a min heap is just a list representing a tree with minimum on top
from typing import List, Dict
from edge import Edge
from vertex import Vertex


#  sorting KEYS according to their VALUES
class MinHeap:

    #  order keys according to values
    def __init__(self, dictionary: Dict):
        self.dictionary = dictionary
        self.heap = list(dictionary.keys())
        self.heap_size = len(dictionary)
        self.build_min_heap()

    def build_min_heap(self):
        for i in range((self.heap_size // 2) - 1, -1, -1):  # to start minheapification from last parent
            self._min_heapify(i)

    def get_and_remove_minimum(self):
        self.heap_size -= 1
        i = self.heap_size
        self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
        self._min_heapify(0)
        return self.heap[i]  # we return the key/ vertex

    @staticmethod
    def _left_child(i):
        return 2 * i + 1

    @staticmethod
    def _right_child(i):
        return 2 * i + 2

    def _minimum_in_heap(self, parent_index) -> int:
        left = MinHeap._left_child(parent_index)
        right = MinHeap._right_child(parent_index)
        #  self.heap[left] -> returns a KEY to the dictionary
        if left < self.heap_size and self.dictionary[self.heap[left]] < self.dictionary[self.heap[parent_index]]:
            minimum_index = left
        else:
            minimum_index = parent_index
        if right < self.heap_size and self.dictionary[self.heap[right]] < self.dictionary[self.heap[minimum_index]]:
            minimum_index = right
        return minimum_index

    def _min_heapify(self, parent_index):
        min_index = self._minimum_in_heap(parent_index)
        if min_index != parent_index:  # need swap
            self.heap[min_index], self.heap[parent_index] = self.heap[parent_index], self.heap[min_index]
            self._min_heapify(min_index)
