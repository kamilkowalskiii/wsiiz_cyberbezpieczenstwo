x=50
y=30
z=70
if x>y:
    x,y = y,x
if y>z:
    y,z = z,y
if z>x:
    z,x = x,z

print(x,y,z)
