import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

# plt.figure()
# plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
l1 = plt.plot(x,y2,label='square')
l2 = plt.plot(x,y1,color='red',linewidth=2,linestyle='--',label='linera')
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('time')
plt.ylabel('value')

# legend
# plt.legend(handles=[l1,l2])
# plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1,0,1,2,3],
        [r'$very\ low$',r'$low$',r'$normal$',r'$high$',r'$very\ high$',r'$\alpha$'])

plt.legend(loc='best')

plt.show()
