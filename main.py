# Hi gus
#welcome to hacker python channel
# today we will learn how to make bar graph
#we need to install  matplotlib package

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')

xpos=[1,2,3,4,5,6,7,8,9,10]
ypos=[1,2,3,4,5,1,6,8,2,1]
zpos=[0,0,0,0,0,0,0,0,0,0]
num_elements=len(xpos)
dx=np.ones(10)
dy=np.ones(10)
dz=[2,4,1,6,4,8,0,2,3,2]
ax1.bar3d(xpos,ypos,zpos,dx,dy,dz,color='#26ffe6')
plt.show()
# so guys thank you and have a great day