import math

class BasicMath():
	def __init__(self, add, subtract, multiply, divide):
		self.add = add
		self.subtract = subtract
		self.multiply = multiply
		self.divide = divide
	
	def add(number, i, Sum, iterations):
		while i < iterations:
			i = i + 1
			Sum = Sum + number
		return Sum

	def subtract(number, i, difference, iterations):
		while i < iterations:
			i = i + 1
			difference = difference - number
		return differnce

	def multiply(number, i, product, iterations):
		while i < iterations:
			i = i + 1
			product = product * number
		return product
	def divide(number, i, quotient, iterations):
		while i < iterations:
			i = i + 1
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

class Main():
	question = str(input("Welcome to the general calculator! This calculator performs basic arithmatic operations as well as trigonometric functions! " +
	"Please enter what part of the calculator you wish to use."))

	if question == "basic":
		global BasicMath
		operation = str(input("What operation would you like to perform?"))

		if operation == "add":
			iterations = float(input("Please enter the number of iterations you wish to do."))
			BasicMath = BasicMath.add(5, 6, 7, 8)
