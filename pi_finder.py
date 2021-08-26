import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.animation import FuncAnimation
import math

inside = 0
total = 0
first = True
def find_pi(n):
    x, y = [], []



    #setup figure
    fig = plt.figure()
    ax = fig.gca()

    #create circle and add to plot
    circle = plt.Circle((0,0), 1, color = 'r')    
    ax.add_patch(circle)

    #set limits for the plot window
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    #create the graph to animate
    graph, = plt.plot([], [], 'o')

    #update function to pass in the FuncAnimation function
    def update(frame):
        global first
        #catch case because Funcanimation runs the first frame twice
        if(first == True): 
            first = False
            return graph

        #generate random coordinates for points
        x.append(random.random())
        y.append(random.random())
        
        #calculating whether the point is in the circle or 
        #not based on the distance to the origin
        before_sqrt = x[frame]**2 + y[frame]**2
        distance_to_origin = math.sqrt(before_sqrt) 


        #accessing global variables tracking the # of points inside the cirlce 
        #and the # of points total
        global inside
        global total
        if distance_to_origin < 1: 
            inside += 1
        total += 1


        #calculating pi by equating the ratio of areas to the ratio of points inside
        pi = (4*(inside/total))

        #format the float value to a more legible form 
        pi = "{:.5f}".format(pi)

        #update the title to have a live tracker of our current estimate
        ax.set_title(pi)

        #update the graph itself with the new point
        graph.set_data(x,y)

        return graph

    #call FuncAnimation to animate the points appearing one by one
    #The interval changes between runs to 
    ani = FuncAnimation(fig, update, frames=n, repeat = False, interval = 1)
    plt.show()


find_pi(10000)

