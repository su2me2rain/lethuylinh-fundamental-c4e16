import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot

# 1, Prepare data
labels = ['Web','iOS','Android','React Native']
values = [40,20,25,15]
colors = ['green','blue','red','pink']
explode = [0,0,0.2,0]
# 2, Plot
pyplot.pie(values,
        labels=labels,
        colors=colors,
        explode=explode)
pyplot.axis('equal')

# 3, Show
pyplot.show()
