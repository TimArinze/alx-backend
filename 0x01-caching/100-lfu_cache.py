#!/usr/bin/env python3
"""
LFU Caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Least frequently Used"""
    def __init__(self):
        """initializing"""
        super().__init__()
        self.dictionary = {}

    def put(self, key, item):
        """putting into cache"""
        if key and item:
            if key in self.cache_data.keys():
                self.dictionary[key] =+ 1
            if key not in self.cache_data.keys():
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    sorted_dict = dict(sorted(self.dictionary.items(),
                            key=lambda x:x[1]))
                    first_key = list(sorted_dict.keys())[0]
                    self.cache_data.pop(first_key)
                    self.dictionary.pop(first_key)
                    print("DISCARD: {}".format(first_key))
                self.dictionary[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        """retreiving data from cache"""
        if key and key in self.cache_data.keys():
            self.dictionary[key] =+ 1
            return self.cache_data.get(key)
