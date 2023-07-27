#!/usr/bin/env python3
"""
LIFO caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """FIFO Caching"""
    def __init__(self):
        """Initializing"""
        super().__init__()

    def put(self, key, item):
        """put into the cache"""
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                last_key = next(reversed(self.cache_data))
                print("DISCARD: {}".format(last_key))
                self.cache_data.pop(last_key)
            self.cache_data[key] = item

    def get(self, key):
        """retreives from the cache"""
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
