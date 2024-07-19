print((lambda x: x**2)(3))

l = [1,2,3,4,5]
l1 = map (lambda i: i**2, l)
print (list(l1))

l2 = filter (lambda i: i%2==0, l)
print (list(l2))

l3 = [1,2,3,4,5]
l4 = map (lambda x,y: x+y, l,l3)
print (list(l4))

n1 = ["Rashid ","Saima ","Abdullah "]
n2 = ["Mahmood", "Naheed","Rashid"]
name = map(lambda x,y: x + y, n1, n2)
print (list (name))

i = range (101)
i1 = filter (lambda x: x%10==0, i)
i2 = list(i1)
del i2[0]
print (i2)