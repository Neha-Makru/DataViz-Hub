import streamlit as st 
from Learning_path import display_learning_path
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
from openpyxl import * 
import plotly.express as px

st.set_page_config(page_title='DataViz Hub', page_icon='📊', layout='wide')
st.title('Your Data, Your Way')


st.sidebar.title("Navigation")
option = st.sidebar.radio("Select a feature", 
                         ('Data Analysis 📈', 'Learning Path 📚'))


if option == 'Data Analysis 📈':
    uploaded_file = st.file_uploader("Upload your Excel or CSV file here please", type=['csv', 'xlsx'])

    def load_data(file):
        try: 
            if file.name.endswith('.csv'):
                df = pd.read_csv(file) 
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file, engine='openpyxl')
            else:
                st.error("Unsupported file type")
                return None
            return df
        except Exception as e:
            st.error(f"Error: {e}")
            return None

    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')
    
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        if df is not None: 
            st.subheader("Data Preview")
            st.dataframe(df) 

            st.subheader("Summary Statistics")
            st.write(df.describe())

            st.subheader("Correlation Heatmap")
            if st.button('Show Correlation Heatmap'):
                numeric_df = df.select_dtypes(include=[np.number])
                if numeric_df.empty:
                    st.error("No numeric columns to compute correlation.")
                else:
                    corr = numeric_df.corr()
                    plt.figure(figsize=(10,6))
                    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
                    st.pyplot(plt)

            csv = convert_df(df)
            st.download_button(
                label="Download filtered data as CSV", 
                data=csv, 
                file_name='Processed_data.csv', 
                mime='text/csv')

            st.subheader("Filter Data")
            for col in df.select_dtypes(include=['object']).columns: 
                unique_vals = df[col].unique()
                selected_vals = st.multiselect(f"Filter {col}", unique_vals)
                if selected_vals:
                    df = df[df[col].isin(selected_vals)]
                
            st.write('Filtered Data', df)

            st.subheader('Select columns for visualization')
            columns = df.columns.tolist()
            selected_columns = st.multiselect('Select Columns: ', columns)

            if selected_columns and len(selected_columns) >= 2:
                st.subheader('Visualization Options')
                plot_type = st.selectbox('Select type of plot', ['Bar Chart', 'Line Chart', 'Scatter Plot', 'Box Plot', 'Pie Chart'])

                st.subheader(f"{plot_type} of selected columns")
                x_col = st.selectbox('Select X-axis', selected_columns)
                y_col = st.multiselect('Select Y-axis', selected_columns)

                if x_col and y_col:
                    plt.figure(figsize=(10,6))

                    if plot_type == "Bar Chart":
                        sns.barplot(x=x_col, y=y_col[0], data=df)
                    elif plot_type == "Line Chart":
                        for y in y_col:
                            sns.lineplot(x=x_col, y=y, data=df, label=y)
                    elif plot_type == "Scatter Plot":
                        sns.scatterplot(x=x_col, y=y_col[0], data=df)
                    elif plot_type == "Box Plot":
                        sns.boxplot(x=x_col, y=y_col[0], data=df)
                    elif plot_type == "Pie Chart":
                        if df[y_col[0]].dtype == 'object':
                            pie_data = df[y_col[0]].value_counts()
                            plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
                        else:
                            plt.pie(df[y_col[0]], labels=df[x_col], autopct='%1.1f%%')
                        plt.axis('equal')  
                    st.pyplot(plt)

                st.subheader("Interactive Plot")
                if st.button("Show Interactive Plot"):
                    fig = px.scatter(df, x=x_col, y=y_col[0]) 
                    st.plotly_chart(fig)

            else:
                st.warning("Please select at least two columns for visualization.")

            if df.isnull().values.any(): 
                st.warning("Dataset contains missing values")
                missing_option = st.selectbox("How would you like to handle the missing values?", 
                                              ('Drop Rows', 'Fill With Mean', 'Fill With Median'))

                if missing_option == 'Drop Rows':
                    df = df.dropna() 
                elif missing_option == 'Fill With Mean':
                    df = df.fillna(df.mean())
                elif missing_option == 'Fill With Median':
                    df = df.fillna(df.median())

                st.write('Data after handling the missing values: ', df)

            st.subheader('Group Data And Aggregate')
            group_by_col = st.selectbox('Select column to group by', columns) 
            agg_col = st.selectbox('Select column to aggregate', df.select_dtypes(include=np.number).columns)
            agg_func = st.selectbox('Select aggregation function', ['sum', 'mean', 'max', 'min'])

            if group_by_col and agg_col and agg_func:
                grouped_df = df.groupby(group_by_col).agg({agg_col: agg_func})
                st.write(grouped_df)

    else: 
        st.write('Upload a CSV or Excel file to proceed.')

if option == 'Learning Path 📚':
    display_learning_path()