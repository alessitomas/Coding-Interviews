def print_indices_and_elements(elements) -> None:
    for i, e in enumerate(elements):
        print(f"{i} {e}")
 

def get_even_numbers_between(start: int, end: int) -> list[int]:
    return [i for i in range(start, end+1) if i % 2 == 0]


def get_char_set_from(s: str) -> set[str]:
    return {c for c in s}

from math import sqrt

def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return {num : sqrt(num) for num in range(start, end+1) if sqrt(num).is_integer()}


def filter_even_from(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]


def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1


def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [num if num % 2 == 0 else -1 for num in numbers if num % 5 == 0 ]


def str_lengths(strings: list[str]) -> list[int]:
    return [len(string) for string in strings]


def get_fibonacci_type(version: int) -> str:
    return "<class 'generator'>" if version == 1 else "<class 'list'>"


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return 'Generators are lazy iterables the do not execute every step once called rather when it is needed they executes the needed lines. For that reason they use way less memory, but cant consume more time than normal lists'


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


def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    return -1


def keys_with_different_value() -> list[int]:
    return []


def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        # You should add code here and remove the break
        break

    if numbers:
        # You should add code here
        pass


def append_range(start: int, end: int, step: int=1, to: list[int]=[]):
    # You may add code here

    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value == None


def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    total = e1 + e2 + sum(others)
    count = 2 + len(others)
    return total / count


def keys_with_different_value() -> list[int]:
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    
    # Find keys that exist in both dictionaries
    common_keys = set(a.keys()) & set(b.keys())
    
    # Sort the keys
    return sorted(common_keys)


def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        # Use tuple unpacking to get the first and last elements
        first, *middle, last = numbers
        print(first, last)
        # Continue with the elements between first and last
        numbers = middle

    if numbers:
        # If there's one element left (odd number of elements)
        # Use tuple unpacking to get the single element
        (middle_element,) = numbers
        print(middle_element)



def append_range(start: int, end: int, step: int=1, to=None):
    # Initialize default argument properly
    if to is None:
        to = []
        
    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    global global_var  # Add this line to declare we're using the global variable
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value is None