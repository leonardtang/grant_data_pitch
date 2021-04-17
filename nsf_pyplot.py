import pandas as pd
import numpy as np
import plotly.graph_objects as go

XGROUP = 'StartDate'
directorates = ['SBE', 'MPS', 'BIO', 'GEO','EHR', 'O/D', 'CSE', 'ENG']

color = list(np.random.choice(range(256), size=3))

dataset = pd.read_csv("Awards.csv", error_bad_lines=False, encoding="ISO-8859–1")
df = pd.DataFrame(dataset)

fig = go.Figure()

df['StartDate'] = df[df.columns[4]].str[-4:]
directorates = list(set(df['NSFDirectorate']))

for directorate in directorates:
    df_new = df[df['NSFDirectorate'] == directorate]
    df_new = df_new.groupby([XGROUP]).mean()
    X1 = pd.Series(df_new.index.values).tolist()
    X1 = [int(i) for i in X1]
    Y1 = pd.Series(df_new[df_new.columns[0]]).tolist()
    Y1 = [int(i) for i in Y1]

    fig.add_trace(go.Bar(
        x=X1, 
        y=Y1, 
        name=directorate,
        #marker_color=color,
    ))

fig.update_layout(
    title=f"Comparison of Average Grant Award Amount by Directorates Over Time", 
    xaxis={'title':{'text':'Year'}},
    yaxis={'title':{'text':'Avg. Grant Awarded Amount Per Year'}},
    showlegend=True)

fig.show()

