How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time.


att:

count_elements = int 
data = [ ]

min_values = [v1, min(v2, v1), min(v3,v2)]





[ ]
push( 2 )

[ 2 ]
c_e = 1

push ( 3 )
c_e = 2
[ 2, 3 ]


pop( )

data[ c_e -1] 
c_e -= 1

[ 2, 3 ]
c_e = 1


push(50)


[ 2, 50] 
c_e = 2




min = 0
[ 3, 5, 2, 0]


pop()

min = ? 
[ 3, 5, 2, 0]

push v -> 

len(data) == count_elements -> append(v)

count_elementes < len(data) -> data[count_elementes] = v


# Space is O(N)
# Time O(1)

class Stack:
	def __init__(self ):
		self.size = 0
		self.data = []
		self.min = []


	def add_min(self, v):
		if self.size == len(data):
if self.size == 0:
		self.min.append(v)
	else:
		prev_v = self.min[self.size -2]
		self.min[self.size -1] = (min(v, prev_v))
else:
	if self.size == 0:
		self.min[self.size] = v
	else:
		prev_v = self.min[self.size -1]
		self.min[self.size] = (min(v, prev_v))




	def push(self, v):
		if self.size == len(data):
			self.data.append(v)
		else: 
			self.data[self.size] = v
		self.size += 1
self.add_min(v)
		
		return 



	def pop(self):
		if self.size  ==  0:
			raise Exception("Stack is empty")
			return
		pop_value = self.data[self.size -1]
		self.size -= 1
		return pop_value


	def min(self):
		if self.size  ==  0:
			raise Exception("Stack is empty")
			return
		return self.min[self.size - 1]
		




s = Stack()

data =  [ ]
min = [ ] 
size = 0


pop() -> valid
min() -> valid
push( 2) 
data = [2] 
min = [2]
size = 1


push( 3 )

v = 3
data = [2, 3] 
min = [2, 2]]

prev_v = 2

size = 2



pop(  )


data = [2, 3] 
min = [2, 2 ]]
size = 1

(3)



push (10)

v = 10
data = [2, 10] 
min = [2, 2 ]]
size = 2






