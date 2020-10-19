# python script to run on a function f to determine if it is cyclic
# it outputs the period as well as the length of the tail before the cycle

def f(x):
	return (x**2 + 2) % 17

t = 1
a = f(0)
b = f(f(0))

while a!=b:
	t += 1
	a = f(a)
	b = f(f(b))

print(t)

p = 1
b = f(b)
while a != b:
	p += 1
	b = f(b)

print(p)

a=0
b=0
for i in range(p):
	b = f(b)

t=0

while a!=b:
	t+=1
	a=f(a)
	b=f(b)

print(t)