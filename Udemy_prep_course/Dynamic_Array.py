class MyArray:
    def __init__(self):
        self.len = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def get_All(self):
        return self.data

    def add(self, item):
        self.data[self.len] = item
        self.len += 1
        return self.len

    def pop(self):
        lastItem = self.data[self.len - 1]
        del self.data[self.len - 1]
        self.len -= 1
        return lastItem

    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
        return item

    def shiftItems(self, index):
        for i in range(index, self.len - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.len - 1]
        self.len -= 1


myArray = MyArray()
myArray.add('you')
myArray.add('are')
myArray.add('not')
myArray.add('nice')
myArray.delete(2)
print(myArray.get_All())
