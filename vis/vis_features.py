import plotly.graph_objs as go
import matplotlib
from matplotlib.colors import to_rgb
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist
import math
from plotly.subplots import make_subplots

import pdb






features_ln = np.load("../result/features_ln_wikiart_artists_E_paintings_noT.npy")
labels = np.load("../result/labels_wikiart_artists_E_paintings_noT.npy")
top_num = 12
umap_document_vectors_ln = features_ln[:labels.shape[0],:]
umap_topic_vectors_ln = features_ln[-top_num:,:]


features_pro = np.load("../result/features_wikiart_artists_E_paintings_noT.npy")
labels = np.load("../result/labels_wikiart_artists_E_paintings_noT.npy")
top_num = 12
umap_document_vectors_pro = features_pro[:labels.shape[0],:]
umap_topic_vectors_pro = features_pro[-top_num:,:]

#artist_vectors = all_features[labels.shape[0]:labels.shape[0]+23:]
#date_vectors = all_features[labels.shape[0]+23:labels.shape[0]+273:]


# find color schemaq
colors = list(matplotlib.colors.CSS4_COLORS.keys())
rgb_colors = [to_rgb(color) for color in colors]
euclidean_distance = cdist(rgb_colors, rgb_colors, 'euclidean')

# Set the diagonal to infinity so colors are not compared to themselves
np.fill_diagonal(euclidean_distance, np.inf)

# Find the indices of the colors with the biggest color difference
top= np.argpartition(euclidean_distance.ravel(), -40)[-40:]

top_colors = [colors[i // len(colors)] for i in top]

color_to_remove=['mintcream','mistyrose','moccasin','navajowhite','oldlace','navy','whitesmoke','linen','lightyellow','lightslategray']

top_colors = [x for x in top_colors if x not in color_to_remove]
#fig = go.Figure()
fig = make_subplots(rows=1, cols=2)
quantile = 0.7

label_l =[]
for i in range(top_num):
    topic_document_ids = np.where(labels == i)[0]
    label_l.append(len(topic_document_ids))
print(label_l)
#pdb.set_trace()

style_name = ["Abstract Expressionism", "Art Nouveau Modern", "Baroque", "Cubism", "Expressionism", "Fauvism", "Impressionism", 
            "Naive Art Primitivism", "Northern Renaissance","Post Impressionism", "Realism", "Romanticism" ]

# fig.add_trace(go.Scatter(
#     x = artist_vectors[:, 0],
#     y = artist_vectors[:, 1],
#     mode = 'markers',
#     marker = dict(size = 25, color = 'DarkSlateGrey', opacity = 1,symbol='square'),
#     hoverinfo='skip',showlegend = False
# ))

# fig.add_trace(go.Scatter(
#     x = date_vectors[:, 0],
#     y = date_vectors[:, 1],
#     mode = 'markers',
#     marker = dict(size = 25, color = 'DarkSlateGrey', opacity = 1,symbol='square'),
#     hoverinfo='skip',showlegend = False
# ))

def draw(fig, umap_document_vectors, umap_topic_vectors, row=1, col=1, legend=False):

    for i in range(top_num):    
        topic_document_ids = np.where(labels == i)[0]

        #Get the distance from certain quantile docu to corresponding topic, based on 2d embedding
        all_dist = [math.dist(umap_document_vectors[id], umap_topic_vectors[i]) for id in topic_document_ids]
        quantile_dist = np.quantile(all_dist, quantile)

        # The topic circle
        # fig.add_shape(type="circle",
        #     xref="x", yref="y",
        #     fillcolor=top_colors[i],
        #     x0=umap_topic_vectors[i][0]-quantile_dist, y0=umap_topic_vectors[i][1]-quantile_dist, x1=umap_topic_vectors[i][0]+quantile_dist, y1=umap_topic_vectors[i][1]+quantile_dist,
        #     line_color=top_colors[i],opacity = 0.3)
        
        
        fig.add_trace(go.Scatter(
            x = umap_document_vectors[topic_document_ids, 0],
            y = umap_document_vectors[topic_document_ids, 1],
            mode = 'markers',
            marker = dict(size = 2, color = top_colors[i], opacity = 1,symbol='circle'),
            hoverinfo='skip',showlegend = False,),
            row=row, col=col)

        if legend:
            #The topic location (central of the circle) 
            fig.add_trace(go.Scatter(
                x = np.array(umap_topic_vectors[i][0]),
                y = np.array(umap_topic_vectors[i][1]),
                mode = 'markers+text',
                #marker = dict(size = 25, color = top_colors[i], opacity = 1, symbol='triangle-up'),
                #marker = dict(size = 3, color = top_colors[i], opacity = 1, symbol='circle'),
                marker = dict(color = top_colors[i]),
                hovertemplate ='<b>%{text}</b><extra></extra>',
                #text = [style_name[i]],
                name = style_name[i],
                textposition='bottom center',
                textfont = dict(size=16)
                ),
                row=row, col=col
                )

draw(fig, umap_document_vectors_ln, umap_topic_vectors_ln, row=1, col=1 )
draw(fig, umap_document_vectors_pro, umap_topic_vectors_pro, row=1, col=2, legend=True )


# fig.update_xaxes(zeroline=False,visible=True, showticklabels=False)
#fig.update_yaxes(visible=True, showticklabels=False,scaleanchor = 'x',scaleratio = 1)
#fig.update_yaxes(showline=True, linewidth=2, linecolor='black',mirror=True, scaleanchor = 'x',scaleratio = 1,)

fig.update_xaxes(showline=True, linewidth=2,  showticklabels=False,linecolor='black',mirror=True)
fig.update_yaxes(scaleanchor = 'x',   showticklabels=False,range=[-10, 20], showline=True,  linewidth=2, linecolor='black',mirror=True)


fig.update_layout(
    {
    'plot_bgcolor': 'rgba(0, 0, 0, 0)'
    },
    legend=dict(
        x = 1.05,
        y=  0.99,
        font=dict(
            size=22,  # Increase legend font size
        )
    ),
    width=1300,
    height =570,
    # hoverlabel=dict(
    #     bgcolor="white",
    #     font=dict(size=18),
    # ),
    font=dict(family = 'Arial',size = 13,color ='black'),
)

fig.show()
fig.write_image("space.pdf")