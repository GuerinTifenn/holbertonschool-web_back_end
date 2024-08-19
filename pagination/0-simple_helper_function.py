#!/usr/bin/env python3
"""
Simple helper function to calculate start and end index for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing a start index and an end index.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
