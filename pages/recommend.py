
import pickle
import streamlit as st
from streamlit_extras.let_it_rain import rain

import numpy as np
import pandas as pd



# <==== Code starts here ====>

courses_list = pickle.load(open('courses.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

rain(
    emoji="🕮",
    font_size=30,  # the size of emoji
    falling_speed=6,  # speed of raining
    animation_length= 2,  # for how much time the animation will happen
)

def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    dist1 = (similarity[index])
    distances = sorted(list(enumerate(dist1)), reverse=True, key=lambda x: x[1])
    dist = pd.DataFrame(dist1)
    
    for i in distances[1:5]:
        st.write("Name of the Course :memo: :  ", courses_list.iloc[i[0]].course_name.upper())
        st.write("Course URL	:link: :  ", courses_list.iloc[i[0]].course_url)
        st.write("Platform :medal: :  ", courses_list.iloc[i[0]].Platform.upper())
        #st.write("Score  :large_blue_diamond: :  ", dist.iloc[i[0]].to_string(index = False))
        st.write ("Reason for Recommendation (SKILLS YOU MAY GET) : ")
        st.write(courses_list.iloc[i[0]].Skills)  
        st.write("-"* 90)
        


def main():
    
    # To write title

    st.markdown("<h5 style = 'text-align: Left; color: white;'>Hello! I'm here to help you find the perfect course over 5000 courses from dataset. Let's get Started !🙂</h5>",unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: Left ; color: blue;'> What field or topic are you interested in? </h5>", unsafe_allow_html=True)
    
    course_list = courses_list['course_name'].values
    selected_course = st.selectbox("Select here :point_down:",
      
         courses_list
    )

    if st.button(' Recommend '):
        st.success("Recommending courses similar to " + selected_course)
        recommend(selected_course)


if __name__ == "__main__":
    main()















