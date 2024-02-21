import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
from PIL import Image

  
  
st.set_page_config(page_title="CRS",page_icon = "🫰")





st.markdown("<h1 style='text-align: Left ; color: white;'>  COURSE RECOMMENDATION SYSTEM </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center ; color: violet;'> Discover a plethora of courses at your fingertips!</h4>", unsafe_allow_html=True)

  
#To load image
img = Image.open('images.png')
image_bytes = img.resize((700,400))


co_1, co_2, co_3 = st.columns(3)
with co_1:
    st.image(image_bytes, use_column_width=False)


  
  
# Raining Emoji
  
rain(
    emoji="🕮",
    font_size=50,  # the size of emoji
    falling_speed=3,  # speed of raining
    animation_length="infinite",  # for how much time the animation will happen
)


#sc = st.sidebar.columns(2)
#sc[0].image(r'C:\Users\Yuva\.vscode\Streamlit dev\images.png', width=150)
#sc[1].write("  ")



st.subheader(":blue[Discover your perfect course - click here to explore! :point_down:]")
want_to_contribute = st.button("click here")
if want_to_contribute:
    switch_page("recommend")
