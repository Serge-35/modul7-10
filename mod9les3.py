class EvenNumbers:
    """Итератор последовательности четных чисел в заданном диапазоне"""

    def __init__(self, start, end):
        self.start = (start + 1) // 2 * 2
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i = self.start
        if self.i <= self.end:
            result = self.start
            self.start += 2
            return result
        else:
            raise StopIteration()

en = EvenNumbers(10, 25)
print(en)
for i in en:
    print(i)
