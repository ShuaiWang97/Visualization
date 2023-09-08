import plotly.graph_objs as go
import matplotlib
from matplotlib.colors import to_rgb
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist
import math
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

import pdb
import os

#name_ = ["dis" + str(i) for i in range(12)]
name_ = ["abstract_expressionism", "art_nouveau_modern", "baroque", "cubism", "expressionism", "fauvism", "impressionism", 
                "naive_art_primitivism", "northern_renaissance","post_impressionism", "realism", "romanticism" ]

pdb.set_trace()
if os.path.exists("dis_df.csv"):
    all_features = np.load("../result/features_wikiart_artists_E_paintings_noT.npy")
    labels = np.load("../result/labels_wikiart_artists_E_paintings_noT.npy")
    top_num = 12


    umap_document_vectors = all_features[:labels.shape[0],:]
    umap_topic_vectors = all_features[-top_num:,:]

    pdb.set_trace()
    artist_vectors = all_features[labels.shape[0]:labels.shape[0]+23:]
    date_vectors = all_features[labels.shape[0]+23:labels.shape[0]+273:]


    pdb.set_trace() 
    name_.append("class")
    df = pd.DataFrame(columns=name_)

    pdb.set_trace() 
    for th, i in enumerate(umap_document_vectors):
        dist_00 = [math.dist(i, umap_topic_vectors[id]) for id in range(12) ]
        dist_00.append(name_[labels[th]])

        df.loc[len(df)] = dist_00
    
    for th, i in enumerate(artist_vectors):
        dist_00 = [math.dist(i, umap_topic_vectors[id]) for id in range(12) ]
        dist_00.append(name_[labels[th]])

        df.loc[len(df)] = dist_00

    df.to_csv("dis_df.csv")




# Define indices corresponding to flower categories, using pandas label encoding
df = pd.read_csv("dis_df.csv")
index_vals = df['class'].astype('category').cat.codes



fig = px.scatter_matrix(df,
    dimensions= name_[2:-4],
    #dimensions=[name_[0], name_[1], name_[2], name_[3]],
    color="class")

fig.update_traces(diagonal_visible=False,  showupperhalf=False)

fig.update_layout(
    #title='Iris Data set',
    dragmode='select',
    width=1200,
    height=800,
    hovermode='closest',
)


fig.show()