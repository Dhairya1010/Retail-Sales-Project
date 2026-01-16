# Retail Sales Analytics & Profitability Prediction

## Project Overview
This project analyzes retail sales transaction data to uncover business insights and predict whether an order will be **profitable or loss-making**.  
It demonstrates an **end-to-end data analytics workflow**, combining data cleaning, business intelligence, and machine learning.

The project is designed to mirror **real-world analyst and data science tasks**, with a strong focus on explainability and business value.

---

## Business Problem
Retail companies often face challenges such as:
- Understanding profitability across regions and product categories
- Measuring the impact of discounts on profit
- Preventing loss-making orders caused by excessive discounting

This project aims to:
1. Explore sales and profit patterns using **Power BI**
2. Build a machine learning model to **classify orders as profitable or not**

---

## Dataset
- Source: Superstore retail sales dataset
- Size: ~10,000 transaction records
- Key features:
  - Sales, Profit, Discount, Quantity
  - Order Date, Ship Date
  - Category, Sub-Category, Region

---

## Tools & Technologies
- **Python**: pandas, scikit-learn
- **Power BI**: Interactive dashboards and exploratory analysis
- **Machine Learning Models**:
  - Logistic Regression
  - Decision Tree Classifier
  - Random Forest Classifier

---

## Exploratory Data Analysis (Power BI)
Exploratory analysis was conducted in **Power BI** to ensure insights were clear and accessible to business stakeholders.

### Key Visuals:
- Sales by Category
- Profit by Region
- Discount vs Profit (scatter and aggregated views)
- KPI Cards (Total Sales, Total Profit, Average Discount)

### Key Insights:
- Higher discounts are strongly associated with negative profit
- Some categories generate high sales but lower margins
- Profitability varies significantly across regions

---

## Machine Learning Approach

### Initial Attempt: Sales Prediction (Regression)
Regression models (Linear Regression, Decision Tree, Random Forest) were initially tested to predict sales values.  
Performance was poor due to limited explanatory features, such as missing product price information.

### Problem Reframing
To better align with the data and business goals, the task was reframed as a **classification problem**:

> Predict whether an order is profitable or not.

---

## Profitability Classification

### Target Variable
- `Is_Profitable = 1` if Profit > 0  
- `Is_Profitable = 0` if Profit ≤ 0

### Features Used
- Quantity
- Discount
- Delivery Days

### Models Evaluated
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

---

## Model Performance Summary
- Overall accuracy of approximately **93%**
- Decision Tree achieved the **highest recall for loss-making orders (~70%)**
- Decision Tree was selected due to its **interpretability and business usability**

This model can help identify orders likely to result in losses, supporting better discount and pricing strategies.

---

## Project Structure
Project Structure

retail_sales_project
- data/

&emsp;&emsp;superstore.csv
- src/

&emsp;&emsp;1_load_and_clean.py

&emsp;&emsp;2_feature_engineering.py

&emsp;&emsp;3a_model_training.py

&emsp;&emsp;3b_profitability_classification.py

- output/

&emsp;&emsp;cleaned_data.csv

&emsp;&emsp;X.csv

&emsp;&emsp;y.csv

- power bi/

&emsp;&emsp;retail_sales_dashboard.pbix

-README.md

---

## Key Takeaways
- Data limitations can significantly impact model performance
- Reframing the problem led to a more actionable and accurate solution
- Combining **Power BI** with **Python** enables both strong business insights and predictive analytics

---

## Future Improvements
- Include product price or cost data for improved regression modeling
- Perform hyperparameter tuning
- Add model explainability (feature importance, SHAP values)

---

## Author
**Dhairya Patel**  
Computer Science (Data Science & AI)  
Aspiring Data Analyst / Data Scientist