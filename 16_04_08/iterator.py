"""
只要对象实现了_iter_方法就可以对其进行迭代；
下面自己实现了一个range()
"""
class testIterator():
    def __init__(self, num):
        self.num = num
        self.temp = 0
    def __next__(self):
        if self.temp < self.num:
            self.temp += 1
        else:
            raise  StopIteration
        return self.temp
    def __iter__(self):
        return  self

if __name__ == "__main__":
    it = testIterator(8)

    print(type(range(1)))
    print(isinstance(range,testIterator))
    print(list(it))