import streamlit as st
import streamlit.components.v1 as components

#----------------------Hide Streamlit footer----------------------------
hide_st_style = """
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
#--------------------------------------------------------------------
st.set_page_config(layout="wide")


COL1 = st.columns([1, 2],gap='large')
with st.container():

    with COL1[0]:
        st.image("https://scontent.futp1-1.fna.fbcdn.net/v/t1.18169-9/12509205_1115890215118598_6893646435576532264_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFzBUKxhJqztWryUeipMZy8UDI0_LwGGFVQMjT8vAYYVRLxOuUeOvNv8OUKdoo69akEHTybjy3JuOugDvqdV9QZ&_nc_ohc=i_MYnGfYpCMAX_EsYFW&_nc_ht=scontent.futp1-1.fna&oh=00_AfDRXfP4nDA_SesqcblfoilRLVgNuk8w5MNKnViEjdYQyw&oe=662412C7",use_column_width='always')

    with COL1[1]:
        # st.title("Phawit Boonrat")
        st.header("Phawit Boonrat")
        st.write("Hi! I am passionate about robotics and autonomous systems. Ten years ago, during my bachelor's degree studies, I built a robot from scratch using the ROS system. At that time, there weren't as many tutorials available as there are today, so I relied heavily on documentation from the ROS website. My passion drove me to pursue this project independently, and I successfully completed it as part of my research in Electrical Engineering for my bachelor's degree.")
        st.write("Following that, I pursued further studies in AI and machine learning at the master's level. I developed a keen interest in deep learning, especially reinforcement learning. I achieved an A grade in all subjects related to AI and machine learning during my master's studies.")
        col11,col12 = st.columns([2, 3],gap='small')
        with col11:
            st.subheader("Interests")
            st.markdown("- ##### Machine Learning \n - ##### Deep Learning \n - ##### Computer Vision \n - ##### Robotics")
        with col12:
            st.subheader("Education")
            st.markdown("- ##### Bachelor's degree \n  - ##### Electrical Communication Engineering,Chulachomklao Royal Military Academy \n - ##### Master's degree \n   - ##### Artificial Intelligence And Machine Learning,National Institute of Development Administration")
        # st.markdown("- ##### Deep Learning")
        # st.markdown("- ##### Computer Vision")
        # st.markdown("- ##### Robotics")

        # st.markdown("- Machine Learning")

# Deep Learning
# Computer Vision
# Robotics")
        # st.header("Phawit Boonrat")
        # st.header("Phawit Boonrat")
st.markdown("""---""")
COL2 = st.columns([1, 2],gap='small')
with st.container():
    with COL2[0]:
        st.header("Experience")
    with COL2[1]:
        st.markdown("- ##### 2016-2020 : Signal Company Commander  \n - ##### 2020-2013 : Operations Staff Officer \n - ##### 2023-2024 : Lecturer at Chulachomklao Royal Military Academy")
        # st.image("https://static.streamlit.io/examples/cat.jpg",use_column_width='always')
        # st.video("https://www.youtube.com/watch?v=oqt_T0Da7OA")

st.markdown("""---""")

with st.container():
    st.header("Projects")

#project1,2
COL3 = st.columns([1, 1],gap='small')
with st.container():
    with COL3[0]:
        st.markdown("##### Autonomous Mobile Robot and Intelligent Systems")
        st.markdown("""I have built a custom 2-wheels robot from scratch :red[(using an Kinect+Arduino+Rotary Eecoders+IMU)], which can navigate a predefined map autonomously, and also follow a person depending on the color of shirt he/she is wearing. For state estimation (odometry) of the robot, we used rotary encoders found on the wheels. We then integrated an IMU to get more accurate state estimation. For path planning, we used the A* algorithm to find the shortest path between the initial position and the goal. For path tracking, we used a PID controller.
We mounted a Kinect camera on the robot for get enviromment data. We used :red[Robot Operating System (ROS)] for communication between all the parts of the project.
This project was part of my Bachelor's degree research at Chulachomklao Royal Military Academy""")
        st.video("https://www.youtube.com/watch?v=oqt_T0Da7OA")
    with COL3[1]:
        st.markdown("##### Rubik")
        st.markdown("I created an algorithm capable of solving the Rubik's Cube problem using :red[IDA*] and applied my custom algorithm wuth machine learning :red[regression model.]")
        # st.video("AiRubrick_fixed.mp4")
        st.video("https://youtu.be/H9LnXKCRwQs")

st.markdown("""---""")
#project3,4
COL3 = st.columns([1, 1],gap='small')
with st.container():
    with COL3[0]:
        st.markdown("##### AI-powered Retail POS Systems for Smartstore")
        st.markdown("""I createed Retail POS Systems for Smartstore using :red[Object Detection with Convolutional Neural Networks], I retrained yolov5 object detector on images of some customized Thai product in supermarket,200 items in which I manually gathered, performed image processing, and annotated. And I intergrade with my AI-powered Retail POS Systems for smartstore.
This work was done as part of my Master's degree in Image Processing course at at National Institute of Development Administration.""")
        st.image("store0.jpg")
        # st.video("SmartStore.mp4")
        st.video("https://youtu.be/OVC_JKqEn4w")
    with COL3[1]:
        st.markdown("##### Traffic Light Control System using Deep Reinforcement Learning")
        st.markdown("""Trained a Traffic Light Control System how to Find the best strategy for optimising the average sum waiting time of traffic, in simulation, in an SUMO environment using a :red[Deep Q-Network(DQN) and Double Deep Q-Network(DDQN)]. I Used :red[Pytorch] in Python to train the agent, and used SUMO package as a simulation environment. This work was done as part of my Master's degree research at National Institute of Development Administration.""")
        #https://www.youtube.com/watch?v=oir0fEyvOyE
        components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRUQaxjCtRwAOyK3aTJuDUcJi69p5Ght2xDZGmS7NbIqAEKFyvKCN8Np0h9mDTw3Mtfyq4PbfnPHLJc/embed?start=false&loop=false&delayms=3000", height=480)
       
        
        # st.video("sumo.mp4")
        st.video("https://youtu.be/Q0dV2F0qEzs")

st.markdown("""---""")
#project3,4
COL3 = st.columns([1, 1],gap='small')
with st.container():
    with COL3[0]:
        st.markdown("##### Face Recognition")
        st.markdown("####### Thid vsdjbvsjdfvnd sdfbn dnvd cjdnf dfn  dnvsdf jndfkjvdn")
        st.video("https://www.youtube.com/watch?v=oqt_T0Da7OA")
    with COL3[1]:
        st.markdown("##### Target-Tracking")
        st.markdown("I developed a target tracking system to track people and identify a specific target person in videos. I retrained the :red[Object Detection] and :red[DeepSORT] model for tracking people in videos and utilized image similarity techniques to identify the target person.")
        # st.video("deepsort.mp4")
        st.video("https://youtu.be/gIvHAsaPw7I")

        
# #project3
# COL3 = st.columns([1, 2],gap='small')
# with st.container():
#     with COL3[0]:
#         st.markdown("##### Robot Automation")
#         st.markdown("####### Thid vsdjbvsjdfvnd sdfbn dnvd cjdnf dfn  dnvsdf jndfkjvdn")
#     with COL3[1]:
#         # st.image("https://static.streamlit.io/examples/cat.jpg",use_column_width='always')
#         st.video("https://www.youtube.com/watch?v=oqt_T0Da7OA")

# #project4
# COL3 = st.columns([1, 2],gap='small')
# with st.container():
#     with COL3[0]:
#         st.markdown("##### Robot Automation")
#         st.markdown("####### Thid vsdjbvsjdfvnd sdfbn dnvd cjdnf dfn  dnvsdf jndfkjvdn")
#     with COL3[1]:
#         # st.image("https://static.streamlit.io/examples/cat.jpg",use_column_width='always')
#         st.video("https://www.youtube.com/watch?v=oqt_T0Da7OA")

# #project5
# COL3 = st.columns([1, 2],gap='small')
# with st.container():
#     with COL3[0]:
#         st.markdown("##### Robot Automation")
#         st.markdown("####### Thid vsdjbvsjdfvnd sdfbn dnvd cjdnf dfn  dnvsdf jndfkjvdn")
#     with COL3[1]:
#         # st.image("https://static.streamlit.io/examples/cat.jpg",use_column_width='always')
#         st.video("https://www.youtube.com/watch?v=oqt_T0Da7OA")
