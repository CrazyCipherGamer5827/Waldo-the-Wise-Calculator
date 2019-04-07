import math
from tkinter import *

# class Graphics():
# 	def __init__(self, button):
# 		self.button = button

# 	initializer = Tk()

# 	def interact1():
# 		print(1)

# 	def interact2():
# 		print(2)

# 	def interact3():
# 		print(3)

# 	def interact4():
# 		print(4)
	
# 	def interact5():
# 		print(5)

# 	def interact6():
# 		print(6)

# 	def interact7():
# 		print(7)

# 	def interact8():
# 		print(8)

# 	def interact9():
# 		print(9)

# 	def interact10():
# 		print(0)

# 	def interact11():
# 		print("+")

# 	def interact12():
# 		print("-")

# 	def interact13():
# 		print("*")

# 	def interact14():
# 		print("/")

# 	def interact15():
# 		print("=")

# 	def interact16():
# 		print("clear")
	
# 	def interact17():
# 		print("sin")

# 	def interact18():
# 		print("cos")

# 	def interact19():
# 		print("tan")

# 	def interact20():
# 		print("csc")

# 	def interact21():
# 		print("sec")

# 	def interact22():
# 		print("cot")

# 	def interact23():
# 		print("asin")

# 	def interact24():
# 		print("acos")

# 	def interact25():
# 		print("atan")

# 	def interact26():
# 		print("toDegrees")

# 	def interact27():
# 		print("toRadians")

# 	def interact28():
# 		print("-1")

# 	button1 = Button(initializer, text = "1", command = interact1)
# 	button2 = Button(initializer, text = "2", command = interact2)
# 	button3 = Button(initializer, text = "3", command = interact3)
# 	button4 = Button(initializer, text = "4", command = interact4)
# 	button5 = Button(initializer, text = "5", command = interact5)
# 	button6 = Button(initializer, text = "6", command = interact6)
# 	button7 = Button(initializer, text = "7", command = interact7)
# 	button8 = Button(initializer, text = "8", command = interact8)
# 	button9 = Button(initializer, text = "9", command = interact9)
# 	button10 = Button(initializer, text = "0", command = interact10)
# 	button11 = Button(initializer, text = "-", command = interact28)
# 	button12 = Button(initializer, text = "sin", command = interact17)
# 	button13 = Button(initializer, text = "cos", command = interact18)
# 	button14 = Button(initializer, text = "tan", command = interact19)
# 	button15 = Button(initializer, text = "csc", command = interact20)
# 	button16 = Button(initializer, text = "sec", command = interact21)
# 	button17 = Button(initializer, text = "cot", command = interact22)
# 	button18 = Button(initializer, text = "asin", command = interact23)
# 	button19 = Button(initializer, text = "acos", command = interact24)
# 	button20 = Button(initializer, text = "atan", command = interact25)
# 	button21 = Button(initializer, text = "toDegrees", command = interact26)
# 	button22 = Button(initializer, text = "toRadians", command = interact27)
# 	button23 = Button(initializer, text = "=", command = interact15)
# 	button24 = Button(initializer, text = "clear", command = interact16)
# 	button25 = Button(initializer, text = "+", command = interact11)
# 	button26 = Button(initializer, text = "-", command = interact12)
# 	button27 = Button(initializer, text = "*", command = interact13)
# 	button28 = Button(initializer, text = "/", command = interact14)


# 	button1.pack()
# 	button2.pack()
# 	button3.pack()
# 	button4.pack()
# 	button5.pack()
# 	button6.pack()
# 	button7.pack()
# 	button8.pack()
# 	button9.pack()
# 	button10.pack()
# 	button11.pack()
# 	button12.pack()
# 	button13.pack()
# 	button14.pack()
# 	button15.pack()
# 	button16.pack()
# 	button17.pack()
# 	button18.pack()
# 	button19.pack()
# 	button20.pack()
# 	button21.pack()
# 	button22.pack()
# 	button23.pack()
# 	button24.pack()
# 	button25.pack()
# 	button26.pack()
# 	button27.pack()
# 	button28.pack()

# 	mainloop()

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

	#global Graphics

	#Graphics = Graphics.interact()

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
			numbers = []

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

#Sources: https://pythonspot.com/tk-window-and-button/, https://www.python-course.eu/tkinter_buttons.php,, https://wiki.python.org/moin/TkInter,
#http://effbot.org/tkinterbook/button.htm, https://developers.google.com/edu/python/lists, w3schools.com, various other websites on the internet
