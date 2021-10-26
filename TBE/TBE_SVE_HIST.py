#imports
import pandas as pd
import plotly.express as px

#dataframe
df = pd.read_excel("TBE_SVE.xlsx")

#figure
fig = px.bar(df, x="year", y="f_sve", color="i_sve",
    color_continuous_scale='Reds'
    labels={"i_sve": "Incidens"}
    )

#snygg.com
fig.update_layout(bargap=0.0)
fig.layout.plot_bgcolor = "#FFFFFF"
fig.update_yaxes(title_text="Antal fall")
fig.update_xaxes(title_text="År")
fig.update_layout(title=
    "Totalt antal TBE-fall per år i Sverige 2004 – 2021")

#show
fig.show()
