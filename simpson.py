import numpy as np
from scipy import integrate

x_value1=np.arange(1,4) 
y_value1=np.arange(1,4)
value_1=integrate.simps(y_value1,x_value1);
print(value_1)

x_value2=np.arange(1,4)
y_value2=np.power(x_value2,2)
value_2=integrate.simps(y_value2,x_value2,dx=1)
print(value_2)

x_value3=np.arange(1,4)
y_value3=np.power(x_value2,3)
value_3=integrate.simps(y_value3,x_value3,dx=1,axis=-1,even='last')
print(value_3)

x_value4=np.linspace(0,1,5)
y_value4=1/((x_value4**2)+1)
value_4=integrate.simps(y_value4,x_value4,dx=1,axis=-1,even='first')


x_dom = np.linspace(0,90,4)
x_dom2=np.linspace(0,0.5*np.pi,4)
print("dom of x = ",x_dom2)
y_range=3*(np.sin(x_dom*np.pi/180))**2+(np.cos(x_dom*np.pi/180)**2)
triangle_value=integrate.simps(y_range,x_dom2,dx=1)
print("The value of triangle = ",triangle_value)


#自己解法

def Simpson(function,a,b,*args): 
   Number_interval=eval(input("請輸入數字(會乘二且加一)保持為奇數: "))
   interval = [a, b]
   h = ( interval[1] - interval[0] ) / (2 * Number_interval)
   n = (2 * Number_interval) + 1
   x = np.linspace(interval[0],interval[1],n)
   y = function(x,*args)
   value = 0
   start = -2
   for i in range(0,Number_interval):
        start = start + 2
        count = 0
        for i in range(start, start+3):
            count = count + 1
            if (count ==3 or count == 1):
                 value = ((h/3) * y[i]) + value
            else:
                value = ((h/3) * 4 * y[i]) + value
   return value

def f(x):
    return 1/((x**2)+1)
value_5 = Simpson(f,0,1)

x_value6=np.linspace(0,1,5)
y_value6=1/((x_value4**2)+1)
value_6=np.trapz(y_value6,x_value6,dx=1.0,axis=-1)

print("trapz = ",value_6)
print("Simpson = ",value_5)   
print("integrate.simps = ",value_4)