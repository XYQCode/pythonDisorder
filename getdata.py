'''
调用coolprop获取data
'''

import matplotlib.pyplot as plt
import numpy as np
import CoolProp.CoolProp as CP

t = np.arange(200e3,500e3,1e3,dtype = 'f')#创建数组
p = np.arange(5e6,20e6,1e6,dtype = 'f')
enthalpy = CP.PropsSI('T','H',t[0],'P',p[0],'CarbonDioxide')

print(enthalpy,'\n')
print(t.size)

enthalpyALL=[]
print(enthalpy)


for v in t:
    enthalpy1 = [] 
    for i in p:
        enthalpy = CP.PropsSI('T','H',v,'P',i,'CarbonDioxide')
        enthalpy1.append(enthalpy)

    enthalpyALL.append(enthalpy1) 

print(enthalpyALL)

np.savetxt("E:\data.txt",enthalpyALL,fmt='%f',delimiter=',')
""" 
figsize=(8, 5)
plt.plot(enthalpy1,t)
plt.show()
print(enthalpy1)  
"""

        

        