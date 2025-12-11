class HashTable:
    def __init__(self, size=16):
        self.data = [None] * size

    def _hash(self, key):
        h = 0
        for i, ch in enumerate(str(key)):
            h = (h + (i + 1) * ord(ch)) % len(self.data)
        return h

    def set(self, key, value):
        index = self._hash(key)

        if self.data[index] is None:
            self.data[index] = []

        bucket = self.data[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        index = self._hash(key)
        bucket = self.data[index]

        if bucket is None:
            return None

        for k, v in bucket:
            if k == key:
                return v
        return None

    def keys(self):
        if not self.data:
            return None

        result = []

        for bucket in self.data:
            if bucket and len(bucket):
                if len(bucket) > 1:
                    for pair in bucket:
                        result.append(pair[0])
                else:
                    result.append(bucket[0][0])

        return result


ht = HashTable()

ht.set("age", 54)
ht.set("name", "Kylie")
ht.set("magic", True)
ht.set("spell", "abra kadabra")

print(ht.get("name"))
print(ht.keys())
