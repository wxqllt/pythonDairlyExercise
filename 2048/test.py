class testIteration():
        def __init__(self,num):
            self.temp = 0
            self.number = num
        def __next__(self):
            if self.temp < self.number:
                self.temp += 1
                return  self.temp
            else: raise StopIteration
        def __iter__(self):
            return  self

if __name__ == "__main__":
    a = testIteration(5)
    print(a.__next__())
