import numpy as np
vy = float(input("enter vy : ")) 
v = float(input("enter v : "))
# function : 
vx = np.sqrt(v**2 - vy**2)
tan_theta = vx/vy
print("the value of horizontal velocity is : ", vx )
print("the value of tan theta is : ", tan_theta )
