from turtle import*

def triangle(a) :
	left(60)
	forward(a)
	right(120)
	forward(a)
	right(120)
	forward(a)

	right(180)

def transi(xap,hap) :
	up()
	goto(xap,hap)
	down()

def careu(a) : #on peut faire un boucle while mais c pour optimiser
	left(90)
	forward(a)
	right(90)	
	forward(a)
	right(90)
	forward(a)
	right(90)  
	forward(a)

	right(180)

def kintana(r) :
	a = 0
	while a <12:
		a = a +1
		forward(r)
		left(150)
		



