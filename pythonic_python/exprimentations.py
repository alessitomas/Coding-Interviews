def fibonacci1(n):
    prev = 1
    curr = 1
    yield 1
    for _ in range(n-1):
        prev, curr = curr, curr + prev
        yield curr

def fibonacci2(n):
    result = [1]
    prev = 1
    curr = 1
    for _ in range(n-1):
        prev, curr = curr, curr + prev
        result.append(curr)
    return result

        

def infinite_list1():
    i = 0
    while True:
        yield i 
        i += 1

# import sys

# squared_seq = [i**2 for i in range(100000)]
# print(sys.getsizeof(squared_seq))
# squared_gen = (i**2 for i in range(100000))
# print(sys.getsizeof(squared_gen))



# import cProfile


# print(cProfile.run('sum([i * 2 for i in range(10000)])'))


# print(cProfile.run('sum((i * 2 for i in range(10000)))'))


nums =  [1,2,3,4,5]

# 


# help(iter(nums))




class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        # You can add more code here if you need
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
                num = self.elements[self.i]
                self.i += 2
                return num
            except:
                raise StopIteration()


numbers = [4, 5, 6, 7, 8]
iterator = SkipIterator(numbers)
for n in iterator:
    print(n)