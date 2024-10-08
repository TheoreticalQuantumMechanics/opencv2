import numpy as np
# cos_theta = np.cos(45)
cos_theta = np.cos(np.pi/4)

# print(cos_theta)
a = float(input("enter a : "))
b = float(input("enter b : "))
input_pi = float(input("enter pi value in 3.14 : "))
theta_pi = float(input("enter theta fraction in radian : "))
theta = input_pi/theta_pi
c =np.sqrt(a**2 + b**2 -2*a*b*np.cos(theta))

print("the resultant is : ", c)