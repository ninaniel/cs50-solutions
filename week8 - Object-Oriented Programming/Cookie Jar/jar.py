class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if self.cookies + n > self._capacity:
            raise ValueError("Not enough space in the jar.")
        self.cookies += n

    def withdraw(self, n):
        if self.cookies < n:
            raise ValueError("Not enough cookies in the jar.")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError("Invalid capacity!")
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies