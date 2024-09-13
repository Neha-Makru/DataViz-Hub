import streamlit as st

def display_learning_path():
    if 'step' not in st.session_state:
        st.session_state.step = 1
    
    if st.session_state.step == 1:
        st.title("Learning Path for Data Analysis")
        st.header("Step 1: Data Ingestion")
        st.write("The first step in any data analysis process is to import the data. We will work with CSV or Excel files, using Pandas to load them into a DataFrame.")
        st.image("data_ingestion.png", caption="Data Ingestion Process", use_column_width=True)
        if st.button("Next"):
            st.session_state.step += 1

    elif st.session_state.step == 2:
        st.header("Step 2: Data Cleaning")
        st.write("Once the data is loaded, it often contains missing values, duplicates, or other inconsistencies. Cleaning the data ensures that your analysis will be accurate and meaningful.")
        st.image("data_cleaning.png", caption="Data Cleaning Techniques", use_column_width=True)
        if st.button("Next"):
            st.session_state.step += 1

    elif st.session_state.step == 3:
        st.header("Step 3: Exploratory Data Analysis (EDA)")
        st.write("Exploratory Data Analysis (EDA) is the process of visually and statistically examining your dataset to discover patterns, outliers, and relationships.")
        st.image("eda.png", caption="Exploratory Data Analysis", use_column_width=True)
        if st.button("Next"):
            st.session_state.step += 1

    elif st.session_state.step == 4:
        st.header("Step 4: Data Visualization")
        st.write("Data visualization is the final step where we transform data into meaningful plots, charts, and graphs. This helps to communicate insights and trends effectively.")
        st.image("data_visualization.png", caption="Data Visualization Techniques", use_column_width=True)
        if st.button("Next"):
            st.session_state.step += 1

    elif st.session_state.step == 5:
        st.header("Step 5: Grouping and Aggregation")
        st.write("Grouping and aggregation allow you to summarize data by specific groups. For instance, you can find the average salary by department or total sales by region.")
        st.image("grouping_aggregation.png", caption="Grouping & Aggregation", use_column_width=True)
        if st.button("Finish"):
            st.session_state.step += 1

    elif st.session_state.step == 6:
        st.balloons()
        st.write("Congratulations! You've completed the learning path.")
