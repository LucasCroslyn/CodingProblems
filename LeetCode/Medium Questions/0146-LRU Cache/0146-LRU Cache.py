class LRUCache:

    def __init__(self, capacity: int):
        # Python Dicts are ordered by intertion in recent python
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        # Remove item from dict and readd to move to end of cache dict
        val = self.cache.pop(key, -1)
        if val == -1:
            return val
        self.cache[key] = val
        return val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key, 0)
        # Only need to check size of cache if we're adding a new item
        elif len(self.cache) == self.cap:
            # next(iter()) gets key of first item in dict (LRU item)
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value
    
    def __str__(self) -> str:
        return str(self.cache)