import turtle as t
import time

def drawGap():
	t.penup()
	t.fd(5)

def drawline(draw):
	drawGap()
	t.pendown() if draw else t.penup()
	t.fd(40)
	drawGap()
	t.right(90)
def drawDigit(digit):
	drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
	drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,2,6,8,] else drawline(False)
	t.left(90)
	drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
	drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
	t.left(180)
	t.penup()
	t.fd(20)

def drawDate(date):
	t.pencolor("red")
	for i in date:
		if i == '-':
			t.write("Y", font=("Arial", 38, "normal"))
			t.pencolor("green")
			t.fd(40)
		elif i == '=':
			t.write("M", font=("Arial", 38, "normal"))
			t.fd(40)
		elif i == '+':
			t.write("D", font=("Arial", 38, "normal"))
			t.fd(40)
		else:
			drawDigit(eval(i))

def main():
	t.setup(800, 350, 200, 200)
	t.penup()
	t.fd(-300)
	t.pensize(5)
	drawDate(time.strftime("%Y-%m=%d+", time.gmtime()))
	t.hideturtle()
	t.done()
main()
