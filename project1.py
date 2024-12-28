import streamlit as st
import pandas as pd
import psycopg2



queries = {
    "Top 10 highest revenue generating products": """
    select sub_category, sum(revenue) as total_revenue from purchase_details2 group by sub_category
    order by total_revenue desc limit 10;
    """,    
    "Top 5 cities with the highest profit margins": """
    select city, sum(p1.profit) as total_profit from purchase_details1 c1 join purchase_details2 p1 on
    c1.order_id = p1.order_id group by c1.city order by total_profit desc limit 5;
    """, 
    "The total discount given for each category": """
    select category, sum(d1.discount) as total_discount from purchase_details1 c2 join purchase_details2 d1 on
    c2.order_id = d1.order_id group by c2.category order by total_discount desc;
    """,
    "The average sale price per product category": """
    select category, avg(s1.sales_price) as average_sales_price from purchase_details1 c3 join purchase_details2 s1
    on c3.order_id = s1.order_id group by c3.category order by average_sales_price desc;
    """,
    "The region with the highest average sale price": """
    select region, avg(s2.sales_price) as average_sales_price from purchase_details1 r1 join purchase_details2 s2
    on r1.order_id = s2.order_id group by r1.region order by average_sales_price desc limit 1;
    """,
    "The total profit per category": """
    select category, sum(p2.profit) as total_profit from purchase_details1 c4 join purchase_details2 p2
    on c4.order_id = p2.order_id group by c4.category order by total_profit desc;
    """,
    "The top 3 segments with the highest quantity of orders": """
    select segment, sum(q1.quantity) as total_quantity from purchase_details1 s1 join purchase_details2 q1
    on s1.order_id = q1.order_id group by s1.segment order by total_quantity desc limit 3;
    """,
    "The average discount percentage given per region": """
    select region, avg(d1.discount_percent) as average_discount_price from purchase_details1 r2 join purchase_details2 d1
    on r2.order_id = d1.order_id group by r2.region order by average_discount_price desc;
    """,
    "The product category with the highest total profit": """
    select category, sum(p2.profit) as total_profit from purchase_details1 c3 join purchase_details2 p2
    on c3.order_id = p2.order_id group by c3.category order by total_profit desc limit 1;
    """,
    "The total revenue generated per year": """
    select extract(year from order_date) as year, sum(r3.revenue) as total_revenue from purchase_details1 y1 join purchase_details2 r3
    on y1.order_id = r3.order_id group by y1.order_date order by y1.order_date;
    """,
    "The top 10 subcategories with highest profit": """
    select sub_category, sum(profit) as total_profit from purchase_details2 group by sub_category order by total_profit desc
    limit 10;
    """,
    "The top 10 subcategories with lowest profit": """
    select sub_category, sum(profit) as total_profit from purchase_details2 group by sub_category order by total_profit 
    limit 10;
    """,
    "The top cites generating higest profit": """
    select city, sum(p1.profit) as total_profit from purchase_details1 c1 join purchase_details2 p1 on
    c1.order_id = p1.order_id group by c1.city having sum(p1.profit) > 10000;
    """,
    "The top 3 categories that generating lowest revenue": """
    select category, sum(revenue) as total_revenue from purchase_details1 c5 join purchase_details2 r3 on 
    c5.order_id = r3.order_id group by c5.category order by total_revenue limit 5;
    """
}


def run_query(query):
    try:
        conn = psycopg2.connect(
            host="localhost", database="Retail", user="postgres", password="Kalaiprithivi"
        )
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return pd.DataFrame()
    
st.title("Retail order analysis ")

tab_names = list(queries.keys())
tabs = st.tabs(tab_names)

for i, tab_name in enumerate(tab_names):
    with tabs[i]:
        st.subheader(tab_name)
        query = queries[tab_name]
        df = run_query(query)  
        if not df.empty:
            st.dataframe(df)  
        else:
            st.warning("No data available for this query.")




