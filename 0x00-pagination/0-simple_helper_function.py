#!/usr/bin/env python3
""" Simple helper module """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size containing a start index and
    an end index corresponding to the range of indexes
    """
    end: int = page * page_size
    start: int = end - page_size

    return (start, end)
