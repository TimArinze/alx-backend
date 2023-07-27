#!/usr/bin/env python3
"""
FIFO caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching"""
    def __init__(self):
        """Initializing"""
        super().__init__()

    def put(self, key, item):
        """put into the cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            removed_value = self.cache_data.pop(first_key)
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """retreives from the cache"""
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
