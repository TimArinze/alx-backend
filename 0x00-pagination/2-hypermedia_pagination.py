#!/usr/bin/env python3
"""
Simple pagination
"""
from typing import Tuple, List, Dict, Union, Any
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and end index
    corresponding to the range of indexes to return in a list of pagination
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return appropriate page"""
        assert type(page) and type(page_size) == int
        assert page > 0 and page_size > 0
        index = index_range(page, page_size)
        start = index[0]
        end = index[1]
        pages = self.dataset()[start:end]
        return pages

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns dictionary of the details of the pagination"""
        total_pages = len(self.dataset()) / page_size
        pages = self.get_page(page, page_size)
        next_page = page + 1
        if len(pages) == 0:
            page_size = 0
            next_page = None
        prev_page = page - 1
        if prev_page < 1:
            prev_page = None
        dictionary = {
                "page_size": page_size,
                "page": page,
                "data": pages,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": math.ceil(total_pages)
                }
        return dictionary
