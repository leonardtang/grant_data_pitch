import pandas as pd
import numpy as np
import plotly.graph_objects as go

dataset = pd.read_csv("NIH_data.csv", error_bad_lines=False, encoding="ISO-8859–1")
df = pd.DataFrame(dataset)
admins = list(set(df['Administering IC']))
top_admins = ['NCI', 'NIAID', 'NIGMS', 'NHLBI', 'NIDDK', 'NINDS', 'NIA', 'NIMH']

fig = go.Figure()

for admin in top_admins:
    df_new = df[df['Administering IC'] == admin]

    fiscal_by_year = {
        2011: [],
        2012: [],
        2013: [],
        2014: [],
        2015: [],
        2016: [],
        2017: [],
        2018: [],
        2019: [],
        2020: [],
        2021: []
    }

    for index, row in df_new.iterrows():
        if row['Total Cost'] != ' ':
            fiscal_by_year[row['Fiscal Year']].append(int(row['Total Cost'])) 
        elif row['Total Cost (Sub Projects)'] != ' ':
            fiscal_by_year[row['Fiscal Year']].append(int(row['Total Cost (Sub Projects)'])) 
        else:
            fiscal_by_year[row['Fiscal Year']].append(0)

    for key, value in fiscal_by_year.items():
        if len(value) != 0:
            avg = sum(value)/len(value)
            fiscal_by_year[key] = round(avg, 3)
        else:
            fiscal_by_year[key] = 0

    X = list(fiscal_by_year.keys())
    Y1 = list(fiscal_by_year.values())

    fig.add_trace(go.Bar(
        x=X,
        y=Y1,
        name=admin
    ))

    fig.update_layout(
        title=f"Comparison of Average Grant Award Amount by Administering IC Over Time (Administering ICs with >800 Total Projects and Subprojects)", 
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="right", x=1),
        xaxis = dict(tickmode = 'linear', tick0 = 0, dtick = 1, title={'text':'Year'}),
        xaxis_range=[2010,2021],
        yaxis = dict(tickmode = 'linear', tick0 = 0, dtick = 250000, title={'text':'Avg. Grant Awarded Amount Per Year'}),
        yaxis_range=[0,3500000],
        showlegend=True)

fig.show()
