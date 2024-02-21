import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain

# Setting page config
st.set_page_config(page_title="CRS", page_icon="🫰")

# Title and subtitle
st.markdown("<h1 style='text-align: Left ; color: white;'>  COURSE RECOMMENDATION SYSTEM </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center ; color: violet;'> Discover a plethora of courses at your fingertips!</h4>", unsafe_allow_html=True)

# Load image
img_path = "path/to/your/image.png"  # Provide the correct path here
st.image(img_path, width=700, caption="Image Caption")

# Raining Emoji
rain(
    emoji="🕮",
    font_size=50,  # the size of emoji
    falling_speed=3,  # speed of raining
    animation_length="infinite",  # for how much time the animation will happen
)

# Subheader and button
st.subheader(":blue[Discover your perfect course - click here to explore! :point_down:]")
want_to_contribute = st.button("click here")
if want_to_contribute:
    switch_page("recommend")
