import hashlib as hl
import random

class HashClass:
    def __init__(self, id_num):
        self.id_num = id_num
        self.hash_num = self.hash_it(id_num)

    def hash_it(self, id_num):
        id_num = " ".encode()
        self.salt = random.randint(1, 1000)
        
        self.hash_num = str(id_num) + str(self.salt)

        self.hashed = hl.sha1(id_num).hexdigest()

        return self.hashed

    def print_it(self):
        print(f"Your generated hash number: {self.hash_num}")

my_hash = HashClass(12574825)
my_hash.print_it()