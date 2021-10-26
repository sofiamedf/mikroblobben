### brucella.py ###
import pandas as pd
import plotly
import plotly.express as px

df = pd.DataFrame({"Year":["2010", "2011", 
   "2012", "2013", "2014", "2015", "2016", 
   "2017", "2018", "2019"],
   "Cases":[12, 11, 13, 10, 16, 13, 19, 15, 11, 14]
})

fig = px.line(df, x="Year", y="Cases", 
    title="Antal fall av Brucella i Sverige 2010-2019")

fig.show()
