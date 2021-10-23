import plotly.graph_objects as go
import plotly

labels = ['Stockholm','Uppsala','Västra Götaland','Södermanland', 'Östergötland', 'Övriga']
values = [41.0, 12.8, 12.3, 9.3, 5.3, 19.3]

# Med "hole" skapar du själva hålet i mitten
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.show()

plotly.offline.plot(fig, filename="TBE_topp_munk.html")
