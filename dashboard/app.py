# Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 MOOC Interactive EDA Dashboard")

# Load Data 
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_data.csv')
    df['start_time_DI'] = pd.to_datetime(df['start_time_DI'], errors='coerce')
    df['last_event_DI'] = pd.to_datetime(df['last_event_DI'], errors='coerce')
    df['age'] = df['start_time_DI'].dt.year - df['YoB']
    df['certified'] = df['certified'].astype(int)

    # Fill missing values
    df['LoE_DI'] = df['LoE_DI'].fillna('Unknown')
    df['gender'] = df['gender'].fillna('Unknown')
    df['grade'] = df['grade'].fillna(-1)
    engagement_cols = ['nevents', 'ndays_act', 'nchapters']
    df[engagement_cols] = df[engagement_cols].fillna(0)

    # Categorize grade into letter grades
    def grade_category(g):
        if g < 0:
            return 'Not Graded'
        elif g >= 0.9:
            return 'A'
        elif g >= 0.8:
            return 'B'
        elif g >= 0.7:
            return 'C'
        elif g >= 0.6:
            return 'D'
        else:
            return 'F'

    df['grade_category'] = df['grade'].apply(grade_category)

    # Bin ndays_act
    bins = [0, 1, 3, 7, 14, 30, 60, 90, np.inf]
    labels = ['0', '1-2', '3-6', '7-13', '14-29', '30-59', '60-89', '90+']
    df['ndays_act_binned'] = pd.cut(df['ndays_act'], bins=bins, labels=labels, right=False)

    return df

df = load_data()
st.write(df.head())

# Exploratory Data Analysis

### Engagement Funnel
funnel_counts = {
    'Registered': len(df),
    'Viewed': df['viewed'].sum(),
    'Explored': df['explored'].sum(),
    'Certified': df['certified'].sum()
}
st.subheader("User Engagement Funnel")
fig = px.funnel(x=list(funnel_counts.values()), y=list(funnel_counts.keys()), orientation='h')
st.plotly_chart(fig)

### Certification by Education Level
st.subheader("Certification by Education Level")
edu_cert = pd.crosstab(df['LoE_DI'], df['certified'], normalize='index') * 100
edu_cert.columns = ['No', 'Yes']
fig, ax = plt.subplots()
edu_cert.plot(kind='bar', stacked=True, ax=ax, color=['#FF9999','#66B3FF'])
plt.ylabel("Percentage")
plt.title("Certification by Education Level")
st.pyplot(fig)

## Engagement vs Grade 

### Grade vs Days Active
st.subheader("Grade vs Days Active")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='ndays_act', y='grade', hue=df['certified'].astype(str), ax=ax)
plt.title("Grade vs Days Active")
st.pyplot(fig)

### Pairplot
st.subheader("Engagement vs Grade (Pairplot)")
plot_df = df[['grade', 'nevents', 'ndays_act', 'nchapters', 'certified']].dropna()
plot_df['certified'] = plot_df['certified'].astype(str)
fig = sns.pairplot(plot_df, hue='certified')
st.pyplot(fig)

## Time based Behavior
st.subheader("User Activity Duration")
df['duration_days'] = (df['last_event_DI'] - df['start_time_DI']).dt.days
fig, ax = plt.subplots()
sns.histplot(df['duration_days'].dropna(), bins=50, ax=ax)
plt.title("Distribution of User Activity Duration")
st.pyplot(fig)

## Statistical Testing sing T-test
from scipy.stats import ttest_ind

st.subheader("Statistical Testing: Grade by Certification")
certified_grades = df[df['certified'] == 1]['grade'].dropna()
non_certified_grades = df[df['certified'] == 0]['grade'].dropna()
t_stat, p_val = ttest_ind(certified_grades, non_certified_grades, equal_var=False)

st.write(f"T-test result: t = {t_stat:.3f}, p = {p_val:.3f}")
if p_val < 0.05:
    st.success("Statistically significant difference in grade based on certification")
else:
    st.info("No statistically significant difference")
    
## Wrap Up