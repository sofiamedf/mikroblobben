# imports
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# data frame xlsx
df = pd.read_excel("TBE_SVE.xlsx")

# subplot for 2 y-axes
fig = make_subplots(rows=2, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.05)

# plots - tot - sthlm
fig.add_trace(
    go.Scatter(x=df["year"], y=df["f_sthlm"],
    name="Stockholm",
    line=dict(color=px.colors.qualitative.Plotly[0],
    width=1.5),
    mode='lines'),
    row=1, col=1),

# plots - inc - sthlm
fig.add_trace(
    go.Scatter(x=df["year"], y=df["i_sthlm"],
    name="Stockholm",
    line=dict(color=px.colors.qualitative.Plotly[0],
    width=1.5,
    dash='dot'), mode='lines'),
    row=2, col=1),

# plots - tot - uppsala
fig.add_trace(
    go.Scatter(x=df["year"], y=df["f_uppsala"],
    name="Uppsala",
    line=dict(color=px.colors.qualitative.Plotly[1],
    width=1.5),
    mode='lines'),
    row=1, col=1),

# plots - inc - uppsala
fig.add_trace(
    go.Scatter(x=df["year"], y=df["i_uppsala"],
    name="Uppsala",
    line=dict(color=px.colors.qualitative.Plotly[1],
    width=1.5,
    dash='dot'), mode='lines'),
    row=2, col=1),

# plots - tot - gotland
fig.add_trace(
    go.Scatter(x=df["year"], y=df["f_gotland"],
    name="Gotland",
    line=dict(color=px.colors.qualitative.Plotly[2],
    width=1.5),
    mode='lines'),
    row=1, col=1),

# plots - inc - gotland
fig.add_trace(
    go.Scatter(x=df["year"], y=df["i_gotland"],
    name="Gotland",
    line=dict(color=px.colors.qualitative.Plotly[2],
    width=1.5,
    dash='dot'), mode='lines'),
    row=2, col=1),

# plots - tot - blekinge
fig.add_trace(
    go.Scatter(x=df["year"], y=df["f_blekinge"],
    name="Blekinge",
    line=dict(color=px.colors.qualitative.Plotly[4],
    width=1.5),
    mode='lines'),
    row=1, col=1),

# plots - inc - blekinge
fig.add_trace(
    go.Scatter(x=df["year"], y=df["i_blekinge"],
    name="Blekinge",
    line=dict(color=px.colors.qualitative.Plotly[4],
    width=1.5,
    dash='dot'), mode='lines'),
    row=2, col=1)

# y-axes titles
fig.update_yaxes(title_text="Fall", row=1, col=1)
fig.update_yaxes(title_text="Incidens (per 100 000)", 
    row=2, col=1)

# background color
fig.layout.plot_bgcolor = "#FAFAFA"

# title
fig.update_layout
    (title_text="TBE i 4 svenska regioner 2004 – 2021")

# text font mm
fig.update_layout(
    font=dict(
        family="Helvetica",
        size=15,
        color="black"
    )
)

# show figure
fig.show()

# offline
plotly.offline.plot(fig, filename='TBE_epi_go.html')
