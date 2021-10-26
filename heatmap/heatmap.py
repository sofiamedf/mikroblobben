### heatmap.py ### 
import plotly.express as px 

data=[[1, 25, 30, 50, 1], [20, 1, 60, 15, 30], 
    [30, 60, 1, 5, 80]] 

fig = px.imshow(data, labels=dict (x="Veckodag", 
    y="Tid på dagen", color="Provmängd"), 
    x=['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 
    'Fredag'], y=['Förmiddag', 'Middag', 
    'Eftermiddag'] ) 

fig.update_xaxes(side="top") 

fig.show()
