# Problem 3.5 - Cracking the Coding Interview

# Write a program to sort a stack such that the smallest items are on the top. The stack supports the following operations: push, pop, peek, and is_empty.

# Constraints
# You may not copy the elements into any other data structure (such as an array);
# You can use an additional temporary stack, but not two.

# og

#   
# 
# 

# aux

# 1
# 0
# 3

# v 3
# i 2


# og, aux = uax, og


# 3

# aux

# 1
# 0

# v -> 1
# i -> 1

# og
# 3, 1


# aux 









# DO NOT CHANGE THIS CLASS
class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


# STACK | FILO
# IMPLEMENT YOUR SOLUTION HERE (DO NOT CHANGE THE ARGUMENTS)
def sort_stack(stack: Stack) -> None:
    aux_stack = Stack()
    og_len = len(stack)
    
    
    for i in range(len(stack)):
        max_elem = None
        max_elem_pos = None
        cur_index = len(stack) - 1
        
        while not stack.is_empty():
            if i != 0 and len(stack) == og_len and i > cur_index:
                break

            if max_elem_pos is not None and max_elem_pos == cur_index:
                stack.pop()
                cur_index -= 1
                continue

            cur_elem = stack.pop()

            if max_elem is None or cur_elem > max_elem:
                max_elem = cur_elem
                max_elem_pos = cur_index
            
            aux_stack.push(cur_elem)

            cur_index -= 1
        
        stack.push(max_elem)
        stack, aux_stack = aux_stack, stack
        max_elem_pos = len(stack) - max_elem_pos
    
    return stack


    
    
    




