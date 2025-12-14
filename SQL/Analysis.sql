
USE Retaill_DB
--Sales Analysis 

-- ● Top 10 best-selling products  

SELECT TOP(10) OI.product_id ,P.product_name , SUM(OI.quantity) AS quantity_product
FROM OrderItems AS OI

JOIN Products AS P
ON P.product_id = OI.product_id

GROUP BY OI.product_id ,P.product_name

ORDER BY quantity_product  DESC;




--● Top 5 customers by spending  

SELECT TOP(5) O.customer_id ,C.full_name, SUM(OT.sums_money) AS spending

FROM OrderTotals AS OT
JOIN Orders AS O
ON  O.order_id = OT.order_id
JOIN Customers AS C
ON C.customer_id = O.customer_id
GROUP BY  O.customer_id , C.full_name
ORDER BY spending DESC ;


---● Revenue per store  
SELECT O.store_id, S.store_name ,SUM(OT.sums_money) AS Revenue 

FROM OrderTotals AS OT
JOIN Orders AS O
ON  O.order_id = OT.order_id
JOIN Stores AS S
ON S.store_id = O.store_id 
GROUP BY   O.store_id , S.store_name
ORDER BY Revenue DESC ;

--● Revenue per category  
SELECT P.category_id, P.category_name ,SUM(OI.total_price) AS Revenue_Category 

FROM OrderItems AS OI
JOIN Products AS P
ON  P.product_id = OI.product_id
GROUP BY  P.category_id, P.category_name
ORDER BY Revenue_Category DESC ;


--●  Monthly sales trend  

SELECT   YEAR(O.order_date) AS years ,  MONTH(O.order_date) AS months ,
ROUND(SUM(OT.sums_money),0) AS Revenue_Month
FROM OrderTotals AS OT
JOIN Orders AS O
ON  O.order_id = OT.order_id
WHERE O.order_date IS NOT NULL
GROUP BY  MONTH(O.order_date) , YEAR(O.order_date)
ORDER BY years , months ;


---  Inventory Analysis 

-- Products with low stock  

SELECT TOP(15) S.product_id ,P.product_name , SUM(S.quantity) AS quantity_product
FROM Stocks AS S

JOIN Products AS P
ON P.product_id = S.product_id

GROUP BY S.product_id ,P.product_name

ORDER BY quantity_product  ;



---. Stores with the highest inventory levels 
SELECT TOP(15)  S.store_id ,ST.store_name , SUM(S.quantity) AS quantity_product
FROM Stocks AS S

JOIN Stores AS ST
ON ST.store_id = S.store_id

GROUP BY  S.store_id ,ST.store_name

ORDER BY quantity_product DESC ;


-- Staff Performance  

SELECT  O.staff_id ,S.full_name , COUNT(O.order_id) AS Count_order
FROM Staffs AS S

JOIN Orders AS O
ON O.staff_id = S.staff_id

GROUP BY O.staff_id ,S.full_name

ORDER BY Count_order DESC ;

-- Best-performing staff member by total sales

SELECT TOP(1) O.staff_id , S.full_name , SUM(OT.sums_money) AS total_sales
FROM OrderTotals AS OT
JOIN Orders AS O 
ON O.order_id = OT.order_id
JOIN Staffs AS S
ON S.staff_id = O.staff_id
GROUP BY O.staff_id , S.full_name
ORDER BY total_sales DESC


-- Customer Insights  

-- Customers with no orders  

SELECT  C.full_name , O.order_id

FROM Customers AS C
LEFT JOIN Orders AS O
ON  C.customer_id = O.customer_id
WHERE O.order_id IS NULL 


--- Average spending per customer  


SELECT  O.customer_id ,C.full_name, SUM(OT.sums_money) AS avg_spending

FROM OrderTotals AS OT
JOIN Orders AS O
ON  O.order_id = OT.order_id
JOIN Customers AS C 
ON C.customer_id = O.customer_id

GROUP BY  O.customer_id , C.full_name
ORDER BY avg_spending DESC ;

