'''
著作图5
2022年1月19
肖永清
'''
import matplotlib.pyplot as plt
import numpy as np
#from scipy import interpolate
import CoolProp.CoolProp as CP
from matplotlib.backends.backend_pdf import PdfPages

t=np.arange(280,341,0.1,dtype='f')  #创建一个数组

#验证
print(type(t[1]))
D=CP.PropsSI('D','T',t[1],'P',7.6E6,'CarbonDioxide')
S=CP.PropsSI('C','T',t[1],'P',7.6E6,'CarbonDioxide')
S1=CP.PropsSI('C','T',303,'P',7.6E6,'CarbonDioxide')
S2=CP.PropsSI('C','T',333,'P',7.6E6,'CarbonDioxide')


print(D,'\n')
print(S,'\n')
print(S1,'\n')
print(S2,'\n')




mylist=[] #创建一个列表用于存储获得密度值
print(type(t))
print('mylist的类型：',type(mylist))
print(mylist)
#利用CoolProp去的参数创建数组
for v in t:          
	print(v,'\n')
	print(type(v))
	D=CP.PropsSI('D','T',v,'P',7.6E6,'CarbonDioxide')
	mylist.append(D)
	print('更新列表:',mylist)
	print(D,'\n')

t1=np.arange(280,341,0.1,dtype='f')  #创建一个数组
mylist1=[] #创建一个列表用于存储获得Cp
print(type(t1))
print('mylist的类型：',type(mylist1))
print(mylist1)
#利用CoolProp去的参数创建数组
for v in t1:          
	print(v,'\n')
	print(type(v))
	C=CP.PropsSI('C','T',v,'P',7.6E6,'CarbonDioxide')
	mylist1.append(C)
	print('更新列表:',mylist1)
	print(C,'\n')
"""输出数据到txt文件-2022.11.2"""
#合并列表
z = list(zip(t1,mylist,mylist1)) 
#a = open("C:\Users\Lenovo\Pictures\txt\txt.txt",'a', encoding='utf-8')
np.savetxt("E:\data.txt",z,fmt='%f',delimiter=',')
#np.savetxt(a,mylist,fmt='%f',delimiter=',')
#np.savetxt(a,mylist1,fmt='%f',delimiter=',')
"""结束"""
#单位换算
new_list=[x/1000 for x in mylist1]



y1=mylist

y2=new_list

#找到极值
juzhen=np.matrix(y2)
print(np.max(juzhen))
print(np.where(juzhen==np.max(juzhen)))

print(t[254])


#建设双坐标系
fig,ax1 = plt.subplots(figsize=(8, 5))

lns1=ax1.plot(t,y2,color='black',linestyle='-',label=r'$C_p$')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
lns2=ax2.plot(t,y1,zorder=5,color='black',linestyle='--',label=r'$\rho$')

ax1.scatter([t[254]],0,zorder=5,marker='o',c='black')
ax1.text(t[254]-1.7,0.5,'$T_{pc}$',ha='center',va='bottom',fontname='Arial',fontsize=14)
ax1.plot([t[254],t[254]],[0,y2[254]],zorder=5,c='black',linestyle='-.')
#设置了不能用
ax2.set_xticks([275,280,290,300,310,320,330,340,345])#设置产生的x轴刻度



#合并图例
lns=lns1+lns2
labs=[l.get_label() for l in lns]
font1={'family':'Arial','weight':'normal','size':14}#图例字体的设置
ax1.legend(lns,labs,loc=0,prop=font1)



ax1.set_xlabel(r'Temperature $T$ /[K]',fontname='Arial',fontsize=14)

ax1.set_ylabel('Specific heat $C_p$ /[kJ/kg·K]',fontname='Arial',fontsize=14)
ax2.set_ylabel(r'Density $\rho$ /[kg/$\mathregular{m^3}$]',fontname='Arial',fontsize=14)  # we already handled the x-label with ax1

#范围限定
ax1.set_xlim(275,345)
ax1.set_ylim(0,120)
ax2.set_ylim(100,1000)
ax1.grid(zorder=0,linestyle='-') 
ax2.grid(zorder=0,linestyle='--') 

ax1.tick_params(labelsize=14)
ax2.tick_params(labelsize=14)

plt.tight_layout()#去除空白部分
#plt.savefig('figure5.pdf')
plt.show()

