def person(age, height, weight):
	print "You are %d years old" % age
	print "You are %d inches tall!" % height
	print "You are %d pounds, whoa.\n" % weight

#pass through numbers only
person(23, 78, 190)

age = 34
height = 67
weight = 130
person(age, height, weight)

age = 23
person(age, 87, 290 + 10)

person(12 + 11, 45, 98)

age = 19 + 10
height = age + 50
person(age, height, 180)

print "How old are you?"
age = int(raw_input("?"))

person(age, 45, 90)
