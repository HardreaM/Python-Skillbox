class DoubleElement:
    def __init__(self, *lst):
        self.collection = list(lst)
        if len(lst) % 2 != 0:
            self.collection.append(None)
        self.counter = 0
        self.limit = len(self.collection)

    def __iter__(self):
        self.a = self.collection[self.counter]
        self.b = self.collection[self.counter + 1]
        return self

    def __next__(self):
        result = (self.a, self.b)
        current_index = self.counter + 2
        if self.counter < self.limit:
            if self.limit - self.counter != 2:
                self.a, self.b = self.collection[current_index], self.collection[current_index + 1]
            self.counter += 2
        else:
            raise StopIteration
        return result