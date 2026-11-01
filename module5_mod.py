class NumbersProcessor:
    def __init__(self):
        self.numbers = []

    def input(self, i):
        num = int(input(f"Number {i+1}: "))
        self.insert(num)

    def insert(self, number):
        self.numbers.append(number)

    def search(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1  # 1-based index
        return -1