#!/usr/bin/env python3
""" Simple helper module """
import csv
from math import ceil

from typing import Tuple, List, Dict


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
            """
            List of pagination
            """
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0

            range: Tuple = index_range(page, page_size)
            pagination: List = self.dataset()

            return (pagination[range[0]:range[1]])

    def get_hyper(self, page: int =1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing diffents key-value pairs
        """
        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        total_pages: int = len(dataset) if dataset else 0
        total_pages = ceil(total_pages / page_size)
        prev_page: int = (page - 1) if (page - 1) >= 1 else None
        next_page: int = (page + 1) if (page + 1) <= total_pages else None

        hypermedia: Dict = {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
        return hypermedia


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size containing a start index and
    an end index corresponding to the range of indexes
    """
    end: int = page * page_size
    start: int = end - page_size

    return (start, end)
