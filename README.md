**Table of Contents**
1. Introduction
2. Features
3. Technologies Used
4. Installation
5. Usage
6. Data
7. Examples
8. Contributors

**Introduction**
The Retail Order Data Analysis project is designed to analyze and visualize retail order data, 
providing insights into profits, revenues, and sales trends. This project helps businesses understand their performance metrics and make data-driven decisions. It includes features for revenue analysis, profit margin calculations, and sales trend visualizations.

**Features**
To analyze and optimize sales performance by identifying key trends, top-performing products, and growth opportunities using a dataset of sales transactions.

**Technologies Used**
* Programming Language: Python
* Libraries:
  * Pandas (Data manipulation and analysis)
  * pyscopg2 (to connect with postgres SQL)
* Tools:
  * Jupyter Notebook (for interactive analysis)
* Softwares used:
  * Visual studio code
  * postgres SQL (if querying a database)
* Deployement
  * streamlit

**Usage**
Prepare Data: Ensure your retail data file (e.g., CSV) is in the correct directory.

-->Run the Script: Execute the main analysis script:

streamlit run analysis.py

**Explore Results**: View the generated outputs.

**Data**
This project uses retail order data, which includes fields like:
order_iD, product_id, category, ship_mode, sub_category, region, sales, profit, quantity, segment, discount_percent, discount, profit, revenue.
Data preprocessing steps include handling missing values and standardising the column names  

**Examples**
The total discount given for each category

![image](https://github.com/user-attachments/assets/cd448b6a-9734-48d5-8515-def9c3ce8534)



