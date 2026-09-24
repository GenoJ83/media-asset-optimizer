class HashCache:
    _hashes = set()
    @classmethod
    def is_processed(cls, h): return h in cls._hashes
    @classmethod
    def mark_processed(cls, h): cls._hashes.add(h)
