# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.stack = []
		self.minValue = 0
		self.maxValue = 0
		
    def peek(self):
        if self.stack[-1] < self.minValue:
			return self.minValue
		elif self.stack[-1] > self.maxValue:
			return self.maxValue
		
		return self.stack[-1]

    def pop(self):
		number = self.stack.pop()
		
        if number < self.minValue:
			numberPopped = number
			number = self.minValue
			self.minValue = (self.minValue * 2) - numberPopped
		elif number > self.maxValue:
			numberPopped = number
			number = self.maxValue
			self.maxValue = (self.maxValue * 2) - numberPopped
		
		return number

    def push(self, number):
        if len(self.stack) == 0:
			self.stack.append(number)
			self.minValue = number
			self.maxValue = number
		elif number < self.minValue:
			self.stack.append((number * 2) - self.minValue)
			self.minValue = number
		elif number > self.maxValue:
			self.stack.append((number * 2) - self.maxValue)
			self.maxValue = number
		else:
			self.stack.append(number)

    def getMin(self):
        return self.minValue

    def getMax(self):
        return self.maxValue
