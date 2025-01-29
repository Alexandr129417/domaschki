number = int(input('enter a five-digit number: '))

a = number//10000

b = (number//1000)%10

c = (number//100)%10

d = (number//10)%10

e = number%10

print (e, d, c, b, a)
