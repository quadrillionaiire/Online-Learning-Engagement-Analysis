# 📊 Optimizing Online Learning: Analyzing Student Engagement & Performance

This project uses a rich EdTech dataset from Kaggle to explore how engagement, demographics, and behavior affect online course outcomes. The analysis covers key insights into student behavior, certification rates, and engagement patterns across different demographics. It includes:
- A full exploratory data analysis (EDA) with univariate, bivariate, and multivariate exploration
- Cleaned and preprocessed student-level data
- Visualizations of key performance indicators
- A Streamlit dashboard for interactive insight-sharing

## 📈 Key Findings:
1. **Demographics and Engagement**:
   - Most users are between 20 and 40 years old, with fewer older learners enrolling.
   - The majority of users (over 600,000) do not earn certifications, while fewer than 100,000 users get certified.
   - Most learners have a bachelor's degree or some secondary education; education level alone doesn’t strongly predict certification.

2. **Bivariate Analysis**:
   - Certification rates are low across all genders, but females have a slightly higher rate (0.03) than males (0.025), with many users’ gender marked as unknown (certification rate 0.04).
   - Students with more active days generally achieved higher grades, suggesting consistent participation is linked to better performance.
   - Users with master’s degrees have a relatively higher chance of certification, but most users—regardless of education—remain uncertified.

3. **Multivariate Analysis**:
   - Females aged 25–34 are most likely to get certified; among males, those aged 65+ have a surprisingly higher rate.
   - Certified users tend to have higher grades and more engagement (e.g., events, chapters, and active days) compared to non-certified users, showing a positive relationship between effort and course completion.
   - Out of over 600k registered users, fewer than 50k complete and earn certificates, though over 400k view course materials.
   - Spain, Poland, and Greece show the highest certification rates, while Brazil has the lowest.
   - There is a clear and statistically significant difference in average grades between users who earned a certificate and those who didn’t.
   - Most users have zero active days, indicating drop-off after registration; negative values may indicate incorrect date data or data entry issues.
   - User activity appears to vary by the day the course was started, with certain start days showing higher engagement, possibly due to weekly schedules or motivation patterns.

## 🧰 Tools Used
- Python (Pandas, NumPy)
- Matplotlib & Seaborn for Visualization
- Streamlit for Dashboard
- Jupyter Notebook for analysis

## 🚀 Getting Started
1. Clone the repo:
   ```bash
   git clone https://github.com/quadrillionaiire/Online-Learning-Engagement-Analysis.git
   cd Online-Learning-Engagement-Analysis
   ```
2. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run dashboard/app.py
   ```

## 🌐 Access the Streamlit Dashboard
For an interactive experience and visual exploration of the findings, visit the live Streamlit dashboard: [Streamlit Dashboard Link]([https://share.streamlit.io/yourusername/repo-name/dashboard/app.py](https://dashboard-wsse6xhqsbtzquevmsw9zs.streamlit.app/))

## 📊 Visualizations
- User Engagement Funnel
- Certification Rates by Education Level
- Grade vs. Days Active
- User Activity Duration Distribution
- Statistical Testing: Grade by Certification


