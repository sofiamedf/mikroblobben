import pandas as pd
import plotly.express as px

df = pd.read_excel('gram_sol.xlsx')

fig = px.sunburst(df, path=['luft', 'gram', 'form', 'art'], color='gram',
    color_discrete_map={'(?)':'#D3D3D3', 'Grampos':'purple', 'Gramneg':'pink'}
    )

fig.update_traces(insidetextorientation='radial')

fig.show()
