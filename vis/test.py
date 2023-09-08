# Program to plot a Circle
# using Parametric equation of a Circle
 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pdb
import cv2
import matplotlib.patches as patches
import matplotlib.lines as mlines


mpl.rcParams['figure.dpi'] = 300
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


paths = ['../img/'+i for i in ['cubsim_0.png', 'img_1.png', 'img_2.png', 'img_3.png', "fauvis_0.png", "abstract_expressionism_0.png","artist0.png","artist1.png"]]
x = [2, -3,  6, 11, 13,  12,  5,   7]
y = [2,  4,  -7, 11, 9, -7, -3.5, 4.3]
def getImage(path):
   #pdb.set_trace()
   img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
   img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   resized = cv2.resize(img, (300,300), interpolation = cv2.INTER_AREA)
   #img = plt.imread(path, format="jpg")
   return OffsetImage(resized, zoom=.05)


theta = np.linspace( 0 , 2 * np.pi , 150 )
 
radius = 10
l= radius *1.3
 
a = radius * np.cos( theta )
b = radius * np.sin( theta )


 
figure, axes = plt.subplots( 1 )

#axes.plot( a1, b1 , color='#1f77b4') 

# Cubism
axes.plot( 0.3*a, 0.3*b , color='#1f77b4', linestyle='dashed') 
axes.plot( 0.5*a, 0.5*b , color='#1f77b4', linestyle='dashed')

axes.plot( 0.15*a +14, 0.15*b+10 , color='#2ca02c', linestyle='dashed')
axes.plot( 0.3*a +14, 0.3*b+10 , color='#2ca02c', linestyle='dashed')

axes.plot( 0.2*a +10, 0.2 *b -7  , color='#ff7f0e', linestyle='dashed')
axes.plot( 0.4*a +10, 0.4 *b -7  , color='#ff7f0e', linestyle='dashed')


# axes.plot([0,0], [-l,l], color='black')
# axes.plot([-l,l], [0,0], color='black')

axes.plot([0], [0], '^', color='#1f77b4', linewidth=2, markersize=5)

axes.plot([14], [10], '^', color='#2ca02c', linewidth=2, markersize=5)

axes.plot([10], [-7], '^', color='#ff7f0e', linewidth=2, markersize=5)

axes.text(1.7, -5.6,'Pablo Picasso',fontsize=5)

axes.text(4.8, 2.2,'Paul Cezanne',fontsize=5)

plt.axis('off')
axes.set_aspect( 1 )

blue_star = mlines.Line2D([], [], color='#1f77b4', marker='^', linestyle='None',
                          markersize=3, label='Cubism')
org_star = mlines.Line2D([], [], color='#2ca02c', marker='^', linestyle='None',
                          markersize=3, label='Fauvism')
green_star = mlines.Line2D([], [], color='#ff7f0e', marker='^', linestyle='None',
                          markersize=3, label='Abstract Expression')

plt.legend(handles=[blue_star, org_star, green_star], loc="upper left",bbox_to_anchor=(1.04, 1), fontsize=9)
 
for x0, y0, path in zip(x, y, paths):
    ab = AnnotationBbox(getImage(path), (x0, y0), 
                        #bbox =dict(edgecolor='red'),
                        frameon=False
                        #pad=-0.1
                        )
    axes.add_artist(ab)

    bbox_width, bbox_height = (2.4, 2.4)
    bbox_left = x0 - bbox_width / 2
    bbox_bottom = y0  - bbox_height / 2
    # bbox = patches.Rectangle((bbox_left, bbox_bottom), bbox_width, bbox_height,
    #                          linewidth=1, edgecolor='r', facecolor='none')
    # axes.add_patch(bbox)

#plt.title( 'Distance to cubism prototype' )
plt.savefig('prototype.pdf')  
plt.show()