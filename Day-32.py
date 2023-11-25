# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 08:30:05 2023

@author: Dnyaneshwari...
"""

import pandas as pd
import matplotlib.pyplot as plt
pd.read_csv('c:/10-python/fdata.csv')
plt.show()
plt.plot()

#Write a Python program to plot two or more lines 
import matplotlib.pyplot as plt

# line 1 points 
x1 = [10,20,30]
y1 =[20,40,10]
# line 2 points
x2 = [10,20,30] 
y2= [40,10,30]
# Set the y 
plt.xlabel('x axis')
plt.ylabel('y axis')

# Set a title

plt.title("Two or more lines with different widths and colors ")

plt.plot(x1,y1, color="blue",linewidth =3,label='line1-width-3')

plt.plot(x2,y2, color='red',linewidth =5,label='line2-width-5')

# show a legend on the plot

plt.legend()
plt.show()
########################################################################
# line 1 points 
x1 = [10,20,30]
y1 =[20,40,10]
# line 2 points
x2 = [10,20,30] 
y2= [40,10,30]
# Set the y 
plt.xlabel('x axis')
plt.ylabel('y axis')

# Set a title

plt.title("Two or more lines with different widths and colors ")

plt.plot(x1,y1, color="blue",linewidth =3,label='line1-width-3')

plt.plot(x2,y2, color='red',linewidth =5,label='line2-width-5')

# show a legend on the plot
import pandas as pd
import matplotlib.pyplot as plt
# line 1 points 
x1 = [10,20,30]
y1 =[20,40,10]
# line 2 points
x2 = [10,20,30] 
y2= [40,10,30]
# Set the y 
plt.xlabel('x axis')
plt.ylabel('y axis')
# Set a title
plt.title("Two or more lines with different widths and colors ")
plt.plot(x1,y1, color="blue",linewidth =3,label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color='red',linewidth =5,label='line2-dashed',linestyle='dashed')
# show a legend on the plot
plt.legend()
plt.show()
##########################################################################
#Write a Python program to plot two or more lines and set the line markers
import pandas as pd
import matplotlib.pyplot as plt
# line 1 points 
# x axis values
x = [1,4,5,6,7]
# y axis values
y = [2,6,3,6,3]
#ploting points
plt.plot(x, y, color='red', linestyle= 'dashdot', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)
#Set the y-limits of the current axes.
plt.ylim(1,8)
#Set the x-limits of the current axes.
plt.xlim(1,8)
# naming the x axis 
# Set the x,y 
plt.xlabel('x axis')
plt.ylabel('y axis')
# Set a title
plt.title("display marker")
#show a legend on the plot
plt.show()
#################################################################
#write a program to plot several lines with differnt format
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a=np.arange(0.,5.,0.2)
plt.plot(a,a,'g--',a,a**2,a,a**3,'r^')
plt.show()
######################################################################
#write a python program to display a bar chart of the popularity 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JSP','C#','C++']
popularity=[22.2, 17.6, 8.8, 8, 7.7, 6.7] 
x_pos =[ i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue') 
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Languag Worldwide")
#horizontal so xticks
#verticle yticks
plt.xticks(x_pos, x)
plt.show()
###################################################################
#write a python program to display a bar chart of the popularity 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JSP','C#','C++']
popularity=[22.2, 17.6, 8.8, 8, 7.7, 6.7] 
x_pos =[ i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue') 
plt.xlabel("Languages")

plt.ylabel("Popularity")
plt.title("Popularity of Languag Worldwide")
#horizontal so xticks
#verticle yticks
plt.yticks(x_pos, x)
plt.show()
######################################################################
#group bar graph
import matplotlib.pyplot as plt
#data to plot 
n_groups = 5
men_means =(22, 30, 33, 30, 26) 
women_means =(25, 32, 38, 35, 29)
# create plot
fig, ax =plt.subplots() 
index = np.arange(n_groups)
bar_width=0.35
opacity=0.8
rects1 = plt.bar (index, men_means, bar_width,
                  alpha=opacity,color='g', label='Men')

rects2= plt.bar(index + bar_width, women_means, bar_width,
                alpha=opacity,color='r', label="Women")
plt.xlabel('Person') 
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index+bar_width, ('G1', 'G2', 'G3', 'G4','G5'))
plt.legend()
plt.tight_layout() 
plt.show()
##############################################################################