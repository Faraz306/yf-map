import streamlit as st
import plotly.graph_objects as go

st.title("Yamaan Faraz YF Official Earth view")
# 1. Define your data points (coordinates for Iran)
trace = go.Scattermapbox(
    lat=[32.4279],
    lon=[53.6880],
    mode='markers',
    marker=dict(size=12, color='red'),
    text=['Iran'],
)
# 2. Create the figure
fig = go.Figure(data=[trace])

# 3. Setup the layout (dimensions and style)
fig.update_layout(
    mapbox_style="carto-positron",  # This adds the automatic labels
    mapbox=dict(
        center=dict(lat=32, lon=53), # Center the map on Iran
        zoom=3                       # Set initial zoom level
    ),
    height=800,                      # Make it big
    width=1000,
    margin={"r":0,"t":0,"l":0,"b":0} # Remove white space
)

trace_states = go.Choropleth(
    locations=["AZ", "CA", "NY"],
    locationmode="USA-states",
    colorscale='Rainbow',
    z=[1.0, 2.0, 3.0],
    colorbar={'title': "Value"},
    name="US Data"
)

# 2. Create the figure
fig1 = go.Figure(data=[trace_states])
col1, col2 = st.columns(2)
with col1:
    st.image("img.png")
    b1 = st.button("Show choropleth map.", width=150)
with col2:
    st.image("choropleth.png")
    b2 = st.button("Show carto positron map.")
if b1:
    st.plotly_chart(fig)
elif b2:
    st.plotly_chart(fig1)