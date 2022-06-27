#imports necessary libraries
from matplotlib import pyplot as plt
import matplotlib.font_manager
from matplotlib.pyplot import figure

#configures style of graph
figure = plt.figure()
figure.patch.set_facecolor('#A9CCE3')
plt.rcParams['axes.facecolor'] = '#A9CCE3'
plt.rcParams['font.family'] = 'Verdana'

#configures size of the graph
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10.8, 8)

#defines x and y axis
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

widget_g = [100, 200, 300, 400, 600, 640, 700, 940, 1000, 1300]
plt.plot(hours, widget_g, linewidth=3, label="Germans", color = 'k')

widget_a = [50, 80, 100, 300, 240, 250, 400, 800, 1200, 1500]
plt.plot(hours, widget_a, linewidth=3, label="Austrians", color = 'w')

#labeling
figure.suptitle("Hours Spent Versus Widgets Produced", fontsize= 18)
plt.title("How does German and Austrian productivity compare?", fontsize = 10)
plt.xlabel("Hours")
plt.ylabel("Widgets")
plt.grid(color='k', linewidth = .2)
plt.legend()

#execute
plt.show()
