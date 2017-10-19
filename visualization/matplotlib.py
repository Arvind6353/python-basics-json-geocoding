
import matplotlib.pyplot as plt

fig = plt.figure('Histogram')
ax = fig.add_subplot(1,1, 1 )
ax.hist([11,23,54,28,46,31,56,15], bins = 7 , facecolor = 'g')
plt.title('sample')
plt.xlabel('count')
plt.ylabel('amt')
plt.show()


fig1 = plt.figure('Box-plot')
ax1 = fig1.add_subplot(1,1,1)
ax1.boxplot([11,23,54,28,46,31,56,15])
plt.show()