import pandas as pd
import plotly.graph_objects as go

YEAR = "2020"
XGROUP = 'NSFDirectorate'

dataset = pd.read_csv("Awards.csv", error_bad_lines=False, encoding="ISO-8859–1")
df = pd.DataFrame(dataset)

df["AwardedAmountToDate"] = pd.to_numeric(df["AwardedAmountToDate"])
df['StartDate'] = df[df.columns[4]].str[-4:]
df = df[df['StartDate'] == YEAR]
df = df.groupby([XGROUP]).mean()
X = pd.Series(df.index.values)

Y1 = pd.Series(df[df.columns[0]])

fig = go.Figure()

fig.add_trace(go.Bar(
    x=X, y=Y1, 
    name="Avg. Grant Awarded Amount",
))

fig.update_layout(title=f"{YEAR} Comparison of Average Grant Award Amount by {XGROUP}", barmode='stack')

fig.show()
