from preswald import text, plotly, connect, get_df, table, query, slider
import pandas as pd
import plotly.express as px

text("# Welcome to Preswald!")
text("This is your first app. 🎉")

# Load the CSV
connect()
#df = get_df('student_depression')
df = pd.DataFrame({
    'id': [2, 33, 91, 8, 59],
    'Gender': ['Male', 'Male', 'Male', 'Female', 'Male'],
    'Age': [33.0, 29.0, 33.0, 24.0, 28.0],
    'Academic Pressure': [5.0, 2.0, 3.0, 2.0, 3.0],
    'Work Pressure': [0.0, 0.0, 0.0, 0.0, 0.0],
    'CGPA': [8.97, 5.7, 7.03, 5.9, 9.79]
})
sql = "SELECT * FROM student_depression"
filtered_df=query(sql,"student_depression")

text("#My data analysis app")
table(filtered_df, title="Student Depression Analysis")

threshold=slider("CGPA Threshold",min_val=0, max_val=10,default=6)
table(df[df["CGPA"]>threshold], title="Dynamic data view")

# Create a scatter plot
fig = px.scatter(df, x='Academic Pressure', y='CGPA', 
                 title='Academic pressure vs. CGPA',
                 labels={'Academic Pressure': 'Academic Pressure', 'CGPA': 'CGPA'})

# Add labels for each point
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))

# Style the plot
fig.update_layout(template='plotly_white')

# Show the plot
plotly(fig)

# Show the data
table(df)