# date: 2018-12-10
# author: zp
# goal: draw holland rada

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
radar_labels = np.array(['研究型','艺术型','社会型','企业','常规型','现实型'])
data_labels = ['艺术家','实验员','工程师','推销员','社会工作者','记事员']
data = np.random.random((6,6))
angles = np.linspace(0,2*np.pi,6, endpoint=False)
print(data)
print(data[0])
print([data[0]])

new_data = np.concatenate((data,[data[0]]))
new_angles = np.concatenate((angles,[angles[0]]))
print(new_data)
print(angles)
print(new_angles)

#two way 
# print( np.random.randint(0,15,size=(3,5)) )
# print(np.random.random((3,4)))

#draw the plot
fig = plt.figure()
plt.subplot(111,polar=True)
plt.plot( new_angles, new_data, 'o-',linewidth=1,alpha=0.2 )
plt.fill( new_angles, new_data, alpha=0.25 )
plt.thetagrids(angles*180/np.pi, radar_labels,frac=1.2)
plt.title('holland radar')
plt.figtext(0.5,0.9,'radar',ha='center',size=20)
legend = plt.legend(data_labels,loc=(0.9,0.8))
plt.setp(legend.get_texts(),fontsize='large')
plt.grid(True)
# plt.show()
plt.savefig('hplland_radar.png')
