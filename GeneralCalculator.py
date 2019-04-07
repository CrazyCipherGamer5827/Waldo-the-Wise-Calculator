import math
import tkinter

class BasicMath():
	def __init__(self, add, subtract, multiply, divide):
		self.add = add
		self.subtract = subtract
		self.multiply = multiply
		self.divide = divide
	
	def add(numbers, i, iterations):
		Sum = 0

		for i in numbers:
			Sum += i
		return Sum

	def subtract(numbers, i, iterations):
		difference = 0

		for i in numbers:
			difference = difference - i
		return difference

	def multiply(numbers, i, iterations):
		product = 1

		for i in numbers:
			product = product * i
		return product

	def divide(numbers, i, iterations):
		quotient = 1
		
		for i in numbers:
			quotient = quotient / i
		return quotient

class TrigFunctions():
	def __init__(self, sin, cos, tan, csc, sec, cot):
		self.sin = sin
		self.cos = cos
		self.tan = tan
		self.csc = csc
		self.sec = sec
		self.cot = cot

	def sin(angle):
		value = math.sin(angle)
		return value

	def cos(angle):
		value = math.cos(angle)
		return value

	def tan(angle):
		value = math.tan(angle)
		return value

	def csc(angle):
		value = 1 / (math.sin(angle))
		return value

	def sec(angle):
		value = 1 / (math.cos(angle))
		return value

	def cot(angle):
		value = 1 / (math.tan(angle))
		return value

	def asin(angle):
		value = math.asin(angle)
		return value

	def acos(angle):
		value = math.acos(angle)
		return value

	def atan(angle):
		value = math.atan(angle)
		return value

	def toDegrees(angle):
		value = math.degrees(angle)
		return value

	def toRadians(angle):
		value = math.radians(angle)
		return value

class Main():
	question = str(input("Welcome to the general calculator! This calculator performs basic arithmatic operations as well as trigonometric functions! " +
	"Please enter what part of the calculator you wish to use."))

	if question == "basic":
		global BasicMath
		operation = str(input("What operation would you like to perform?"))

		if operation == "add":
			iterations = float(input("Please enter the number of iterations you wish to do."))
			i = 0
			numbers = []

			while i < iterations:
				i = i + 1
				number = float(input("Please enter the numbers."))
				numbers.append(number)
			
			Sum = BasicMath.add(numbers, 0, iterations)
			print("sum: " + str(Sum))

		if operation == "subtract":
			iterations = float(input("Please enter the number of iterations you wish to do."))
			i = 0
			numbers = []

			while i < iterations:
				i = i + 1
				number = float(input("Please enter the numbers."))
				numbers.append(number)
			
			difference = BasicMath.subtract(numbers, 0, iterations)
			print("difference: " + str(difference))

		if operation == "multiply":
			iterations = float(input("Please enter the number of iterations you wish to do."))
			i = 0
			numbers=  []

			while i < iterations:
				i = i + 1
				number = float(input("Please enter the numbers."))
				numbers.append(number)
			
			product = BasicMath.multiply(numbers, 0, iterations)
			print("product: " + str(product))

		if operation == "divide":
			iterations = float(input("Please enter the number of iterations you wish to do."))
			i = 0
			numbers = []

			while i < iterations:
				i = i + 1
				number = float(input("Please enter the numbers."))
				numbers.append(number)
			
			quotient = BasicMath.divide(numbers, 0, iterations)
			print("quotient: " + str(quotient))

	if question == "trig":
		global TrigFunctions
		operation = str(input("Please enter the trigonometric function you wish to do."))

		if operation == "sin":
			angle = float(input("Please enter the angle (in radians)."))
			TrigFunctions = TrigFunctions.sin(angle)

			print("sin of " + str(angle) + ": " + str(TrigFunctions))

		if operation == "cos":
			angle = float(input("Please enter the angle (in radians)."))
			TrigFunctions = TrigFunctions.cos(angle)

			print("cos of " + str(angle) + ": " + str(TrigFunctions))

		if operation == "tan":
			angle = float(input("Please enter the angle (in radians)."))
			TrigFunctions = TrigFunctions.tan(angle)

			print("tan of " + str(angle) + ": " + str(TrigFunctions))

		if operation == "csc":
			angle = float(input("Please enter the angle (in radians)."))
			TrigFunctions = TrigFunctions.csc(angle)

			print("csc of " + str(angle) + ": " + str(TrigFunctions))

		if operation == "sec":
			angle = float(input("Please enter the angle (in radians)."))
			TrigFunctions = TrigFunctions.sec(angle)

			print("sec of " + str(angle) + ": " + str(TrigFunctions))

		if operation == "cot":
			angle = float(input("Please enter the angle (in radians)."))
			TrigFunctions = TrigFunctions.cot(angle)

			print("cot of " + str(angle) + ": " + str(TrigFunctions))

		if operation == "asin":
			value = float(input("Please enter the value between -1 and 1."))
			TrigFunctions = TrigFunctions.asin(value)

			print("asin of " + str(value) + ": " + str(TrigFunctions))

		if operation == "acos":
			value = float(input("Please enter the value between -1 and 1."))
			TrigFunctions = TrigFunctions.acos(value)

			print("acos of " + str(value) + ": " + str(TrigFunctions))

		if operation == "atan":
			value = float(input("Please enter the value between -1 and 1."))
			TrigFunctions = TrigFunctions.atan(value)

			print("atan of " + str(value) + ": " + str(TrigFunctions))

		if operation == "to degrees":
			angle = float(input("Please enter the angle."))
			TrigFunctions = TrigFunctions.toDegrees(angle)

			print("degree measurement of " + str(angle) + ": " + str(TrigFunctions))

		if operation == "to radians":
			angle = float(input("Please enter the angle."))
			TrigFunctions = TrigFunctions.toRadians(angle)

			print("radian measurement of " + str(angle) + ": " + str(TrigFunctions))
