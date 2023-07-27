#!/usr/bin/env python3
"""
Basic Dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching
from typing import Any, Dict


class BasicCache(BaseCaching):
    """A basic caching system"""

    # def __init__(self):
        # """Initializing"""
        # super().__init__()

    def put(self, key: str, item: Any):
        """assign a dictionary self.cache_data (key and value)"""
        if key or item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key: str) -> Dict:
        """returns value of self.cache_data linked to key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
