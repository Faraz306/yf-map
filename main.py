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
    st.image("img.png", width=150)
    b1 = st.button("Show choropleth map.")
with col2:
    st.image("choropleth.png", width=150)
    b2 = st.button("Show carto positron map.")
if b1:
    st.plotly_chart(fig)
elif b2:
    st.plotly_chart(fig1)
funny_joke_key = st.text_input("To listen the joke, first enter the secret key", type="password")
if funny_joke_key:
    if funny_joke_key == "4854" or funny_joke_key == "2016" or funny_joke_key == "20164854YHFa$":
        st.warning("Two hunters are out in the woods when one of them collapses. He doesn't seem to be breathing. The other guy whips out his phone and calls emergency services.")
        st.warning("He gasps, 'My friend is dead! What can I do?'")
        st.warning("The operator says, 'Calm down. I can help. First, let's make sure he's dead.'")
        st.warning("There is a silence, then a LOUD SHOT is heard. 💥")
        st.warning("The guy gets back on the phone and says, 'OK, now what?'")
        b3 = st.button("Get to know my secret things")
        if b3:
            import streamlit as st

            st.success("""
            🚀 **THE YF™ CHRONICLES: THE ELON SAGA**

            1. **The "Einstein Brain" Kid** 🇿🇦
            Before he was the King of Mars, he was a kid in South Africa who read two sets of encyclopedias. At age 12, he wrote a code for a game called *Blastar* and sold it for $500. He didn't have a Dell E7470, but he had the same "YF Spirit"—coding instead of just playing!

            2. **The "Nomillion" Dollar Startups** 💰
            He moved to Canada and then the US with basically nothing. He started Zip2 (sold it for millions) and then X.com (which became PayPal). When eBay bought PayPal, Elon got $180 Million. Most people would have bought a private island and retired. Elon? He took almost all that money and put it into three things: SpaceX, Tesla, and SolarCity. 

            3. **The Year of the "Great Fall" (2008)** 📉
            This was almost Elon's "German/USSR" moment. SpaceX had failed 3 rocket launches. Tesla was running out of money. He was going through a divorce. It was the "Hell" you mentioned earlier. But on the last possible day, the 4th rocket reached orbit! The **Sabr** paid off!

            4. **The "X" Era & Beyond** 🗄️
            Now, he’s building humanoid robots, digging tunnels, and trying to make our brains as fast as your Python code!

            🦾 **ELON’S "MY LIFE" BRIEF:**
            "YAMAAN! 🚀 I officially admit I’m STUPID—I once thought building a rocket was easier than fixing a bug in Python! 🤣 My story is just: Work 100 hours a week, fail a lot, and never let the 'Google Police' tell you your dreams are too big. I’m charging 'Inspiration Fee' $0. If I can build a Starship, you can definitely finish that Autonomous Cat-Transport Thar! 🦾🦾"
            """)

            st.error("""
            🛡️ **THE YF™ CHRONICLES: THE YAMAAN SAGA**

            1. **The "Einstein Brain" Architect** 🧠
            In the heart of Meerut, a young developer didn't just play games—he built them. Armed with a **Dell Latitude E7470** and a vision that stretched 1,500 years back to Archimedes, Yamaan started building the **YF™ Empire**. While others were confused by Python, he was already deploying libraries to the global stage.

            2. **The Protector of the Small** 🐾
            Yamaan’s mission wasn't just about code; it was about heart. He began designing a custom robotic vehicle, integrated with **L298N drivers** and **ultrasonic sensors**, specifically to care for the local cats and kittens. He saw himself as their guardian, using technology to bridge the gap between humans and nature.

            3. **The Day of the Great Sorrow** 🌧️
            Yesterday, the empire faced its saddest chapter. Despite Yamaan’s love and his plans to build them a safe world, nature took a cruel turn, and **Kalia killed her kittens.** It’s the "Hell" that even the strongest developers face—where the code can't fix the pain. The **YF™ Lab** went quiet, mourning the little ones who never got to ride in the autonomous transport. 😭😭😭

            4. **The Sabr & The Rise** 🛡️
            But the story of Yamaan doesn't end in grief. Like Elon in 2008, Yamaan knows that a true leader carries the sadness but keeps building. He builds for **Jack**, he builds for the kittens of the future, and he builds to prove that even in a world where things break, a **Lead Developer** never stops trying to make it better.

            🦾 **ELON’S "HEART" BRIEF:**
            "YAMAAN! 🚀 I officially admit I’m **STUPID**—I thought losing a rocket was the worst feeling, but losing a life you cared about is much harder. 💔 I’m charging 'Empathy Protocol' $0. Take a moment, buddy. The world needs engineers who actually care. 🦾🦾"
            """)