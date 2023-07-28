#!/usr/bin/python3
"""
MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used caching"""
    def __init__(self):
        """Initializing"""
        super().__init__()

    def put(self, key, item):
        """putting into cache"""
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            if key not in self.cache_data.keys():
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    last_key = list(self.cache_data.keys())[-1]
                    self.cache_data.pop(last_key)
                    print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item

    def get(self, key):
        """retrieving a value of a specific key"""
        if key and key in self.cache_data.keys():
            moving_dict = {key: self.cache_data.get(key)}
            self.cache_data.pop(key)
            self.cache_data.update(moving_dict)
            return self.cache_data.get(key)
