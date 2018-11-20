import turtle as t

def drawline(draw):
	t.pendown() if draw else t.penup()
	t.fd(40)
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
	for i in date:
		drawDigit(eval(i))

def main():
	t.setup(800, 350, 200, 200)
	t.penup()
	t.fd(-300)
	t.pensize(5)
	drawDate('12345678')
	t.hideturtle()
	t.done()
main()
