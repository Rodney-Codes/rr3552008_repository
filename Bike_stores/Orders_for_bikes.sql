
/*
Find the number of customers for each brand and category of bike sold. Order the results in descending order of orders placed for bikes
*/

select brands.brand_name, categories.category_name, count(customers.customer_id) as Count_of_customers
from orders
join customers on orders.customer_id=customers.customer_id
join order_items on orders.order_id=order_items.order_id
join products on order_items.product_id=products.product_id
join brands on products.brand_id=brands.brand_id
join categories on products.category_id=categories.category_id
group by brands.brand_name, categories.category_name
order by brands.brand_name, Count_of_customers desc
