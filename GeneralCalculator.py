import math

class Basic Math():
	def __init__(self, add, subtract, multiply, divide):
		self.add = add
		self.subtract = subtract
		self.multiply = multiply
		self.divide = divide
	
	def add(number, i, Sum, iterations):
		for i in iterations:
			Sum = Sum + number
		return Sum

	def subtract(number, i, difference, iterations):
		for i in iterations:
			difference = difference - number
		return differnce

	def multiply(number, i, product, iterations):
		for i in iterations:
			product = product * number
		return product
	def divide(number, i, quotient, iterations):
		for i in iterations:
			quotient = quotient / number
		return quotient

class TrigFunctions():
	def __init__(self, sin, cos, tan, csc, sec, cot):
		self.sin = sin
		self.cos = cos
		self.tan = tan
		self.csc = csc
		self.sec = sec
		self.cot = cot

	def sin(angle, value):
		value = math.sin(angle)
		return value

	def cos(angle, value):
		value = math.cos(angle)
		return value

	def tan(angle, value):
		value = math.tan(angle)
		return value

	def csc(angle, value):
		value = 1 / (math.sin(angle))
		return value

	def sec(angle, value):
		value = 1 / (math.cos(angle))
		return value

	def cot(angle, value):
		value = 1 / (math.tan(angle))
		return value
