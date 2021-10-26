# imports
import pandas as pd
import plotly
import plotly.express as px

# data
df = pd.read_excel("./data/TB_bubbles.xlsx")

# plotly express-diagram
fig = px.scatter(df, x="aar", y="incidens", 
    title="Incidens av tuberkulos i Sveriges 
    regioner 2010-2019",
    animation_frame="aar", color="region", 
    range_x=[2010,2019], range_y=[0,16], size="pop")

# bakgrundsfärg
fig.layout.plot_bgcolor = "#FFFFFF"

# sakta i backarna (millisekunder)
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]
    ["duration"] = 2500
fig.layout.updatemenus[0].buttons[0].args[1]["transition"]
    ["duration"] = 2500

# visa figuren
fig.show()

# gör html-fil
plotly.offline.plot(fig, filename='./html/tb_inc.html')
