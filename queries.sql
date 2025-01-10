select sub_category, sum(revenue) as total_revenue from order_details2 group by sub_category
order by total_revenue desc limit 10;


select city, sum(p1.profit) as total_profit from order_details1 c1 join order_details2 p1 on
c1.order_id = p1.order_id group by c1.city order by total_profit desc limit 5;

select category, sum(d1.discount) as total_discount from order_details1 c2 join order_details2 d1 on
c2.order_id = d1.order_id group by c2.category order by total_discount desc;

select category, avg(s1.sales_price) as average_sales_price from order_details1 c3 join order_details2 s1
on c3.order_id = s1.order_id group by c3.category order by average_sales_price desc;

select region, avg(s2.sales_price) as average_sales_price from order_details1 r1 join order_details2 s2
on r1.order_id = s2.order_id group by r1.region order by average_sales_price desc limit 1;

select category, sum(p2.profit) as total_profit from order_details1 c4 join order_details2 p2
on c4.order_id = p2.order_id group by c4.category order by total_profit desc;

select segment, sum(q1.quantity) as total_quantity from order_details1 s1 join order_details2 q1
on s1.order_id = q1.order_id group by s1.segment order by total_quantity desc limit 3;

select region, avg(d1.discount_percent) as average_discount_price from order_details1 r2 join order_details2 d1
on r2.order_id = d1.order_id group by r2.region order by average_discount_price desc;

select category, sum(p2.profit) as total_profit from order_details1 c3 join order_details2 p2
on c3.order_id = p2.order_id group by c3.category order by total_profit desc limit 1;

select extract(year from order_date) as year, sum(r3.revenue) as total_revenue from order_details1 y1 join order_details2 r3
on y1.order_id = r3.order_id group by y1.order_date order by year;

select sub_category, sum(profit) as total_profit from order_details2 group by sub_category order by total_profit desc
limit 10;

select sub_category, sum(profit) as total_profit from order_details2 group by sub_category order by total_profit 
limit 10;

select city, sum(p1.profit) as total_profit from order_details1 c1 join order_details2 p1 on
c1.order_id = p1.order_id group by c1.city having sum(p1.profit) > 10000;

select category, sum(revenue) as total_revenue from order_details1 c5 join order_details2 r3 on 
c5.order_id = r3.order_id group by c5.category order by total_revenue limit 5;

select date_part('month', order_date) as month, sum(p2.profit) as total_profit from order_details1 m1 join order_details2 p2
on m1.order_id = p2.order_id group by date_part('month', order_date) order by total_profit desc;

select sub_category, sum(b.quantity) as total_quantity from order_details1 a join order_details2 b on 
a.order_id = b.order_id group by sub_category order by total_quantity desc limit 10;

select sm.ship_mode, sum(r4.revenue) as total_revenue, (sum(r4.revenue) * 100.0 / sum(sum(r4.revenue)) over()) as
revenue_percentage from order_details1 sm join order_details2 r4 on sm.order_id = r4.order_id group by 
sm.ship_mode order by total_revenue desc limit 3;


select state, sum(r5.revenue) as total_revenue from order_details1 s3 join order_details2 r5 on
s3.order_id = r5.order_id group by state order by total_revenue desc limit 5;

select to_char(s2.order_date, 'YYYY-MM') as month, s2.segment, sum(r6.revenue) as total_revenue from order_details1 
s2 join order_details2 r6 on s2.order_id = r6.order_id group by to_char(s2.order_date, 'YYYY-MM'), s2.segment order by
total_revenue desc;

select sum (case when discount_percent > 0 then revenue else 0 end) as discounted_revenue, 
sum (case when discount_percent = 0 then revenue else 0 end) as non_discounted_revenue from order_details2;






