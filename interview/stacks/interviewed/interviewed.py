# Space is O(N)
# Time O(1)

class StackWithMin:
	def __init__(self ):
		self.size = 0
		self.data = []
		self.min = []


	def add_min(self, v):
		if self.size == len(self.data):
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
		if self.size == len(self.data):
			self.data.append(v)
		else: 
			self.data[self.size] = v
		
		self.size += 1

		self.add_min(v)
		
		return 


	def pop(self):
		if self.size  ==  0:
			raise Exception("Stack is empty")
			
		pop_value = self.data[self.size -1]
		self.size -= 1

		return pop_value


	def min(self):
		if self.size  ==  0:
			raise Exception("Stack is empty")
			return
		return self.min[self.size - 1]
		
	def empty(self):
		return True if self.size == 0 else False

