#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""


import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
                    }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """returns a dictionary of index, next index, page_size and data"""
        # assert index <= list(self.indexed_dataset().keys())[-1]
        def get_next_index(self, dictionary, current_index, page_size):
            index_list = list(dictionary.keys)
            if current_index + page_size < len(index_list):
                return index_list[current_index + page_size]
            else:
                return None

        # next_index = get_next_index(self.indexed_dataset(), index, page_size)
        # next_index = index + page_size
        dictionary = {
                "index": index,
                "data": self.dataset()[index: index + page_size],
                "page_size": page_size
                # "next_index": next_index
                }
        return dictionary
