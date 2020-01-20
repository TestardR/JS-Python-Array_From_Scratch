class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def append(self, item):
        self.data[self.length] = item
        self.length +=1
        return self.length

    def pop(self):
        lastItem = self.data[self.length -1]
        del self.data[self.length -1]
        self.length -= 1
        return lastItem

    def delete(self, index):
        item = self.data[index]
        self._shiftItems(index)
        self.length -= 1
        return item
    
    def _shiftItems(self, index):
        for i in range(index):
            self.data[i] = self.data[i+1]

        del self.data[self.length - 1]
        


""" newArray = MyArray()
newArray.append('hi')
newArray.append('you')
print(newArray)
newArray.delete(1)
print(newArray) """