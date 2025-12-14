CREATE DATABASE  Retaill_DB ;

USE Retaill_DB




--Brands
CREATE TABLE Brands (

brand_id INT PRIMARY KEY  , 
brand_name VARCHAR(150) 
);



--Categories
CREATE TABLE Categories (

category_id INT PRIMARY KEY  , 
category_name VARCHAR(150) 
);




--Customers
CREATE TABLE Customers (

customer_id INT PRIMARY KEY  , 
first_name VARCHAR(150) ,
last_name VARCHAR(150) ,
phone VARCHAR(150) ,
email VARCHAR(150) ,  
street VARCHAR(150) ,
city VARCHAR(150) ,
state VARCHAR(150) ,
zip_code INT  ,
full_name VARCHAR(150)

);




 
-- Stores
CREATE TABLE Stores (

store_id INT PRIMARY KEY  , 

store_name VARCHAR(150) ,
phone VARCHAR(150) ,
email VARCHAR(150) , 
street VARCHAR(150) ,
city VARCHAR(150) ,
state VARCHAR(150) ,
zip_code INT    

);



-- Staffs
CREATE TABLE Staffs (

staff_id INT PRIMARY KEY  , 

first_name VARCHAR(150) ,
last_name VARCHAR(150) ,
active BIT ,
phone VARCHAR(150) ,
email VARCHAR(150) , 

store_id INT NULL FOREIGN KEY REFERENCES  Stores(store_id),

manager_id INT NULL  FOREIGN KEY REFERENCES  Staffs(staff_id),
full_name VARCHAR(150)

);




 -- Products
CREATE TABLE Products (

product_id INT PRIMARY KEY  , 

product_name VARCHAR(150) ,
 
brand_id INT FOREIGN KEY REFERENCES  Brands(brand_id),

category_id INT FOREIGN KEY REFERENCES  Categories(category_id),

model_year INT ,

list_price DECIMAL(10,2),
brand_name VARCHAR(100),
category_name VARCHAR(100),


);



-- Orders
CREATE TABLE Orders (

order_id INT PRIMARY KEY   , 
customer_id INT FOREIGN KEY REFERENCES  Customers(customer_id)  ,
order_status TINYINT ,
order_date DATETIME ,
required_date DATETIME ,
shipped_date DATETIME ,

store_id INT FOREIGN KEY REFERENCES  Stores(store_id)  ,
staff_id INT FOREIGN KEY REFERENCES  Staffs(staff_id)  

);


       

-- OrderItems
CREATE TABLE OrderItems (

order_id INT FOREIGN KEY REFERENCES  Orders(order_id)    ,
item_id VARCHAR(40), 
product_id INT FOREIGN KEY REFERENCES  Products(product_id),
quantity INT ,
list_price DECIMAL(10,2) , 
discount DECIMAL(10,2) , 
total_price DECIMAL(10,2)

PRIMARY KEY(order_id , item_id)
);

-- Stocks
CREATE TABLE Stocks (

store_id INT FOREIGN KEY REFERENCES  Stores(store_id),

product_id INT FOREIGN KEY REFERENCES  Products(product_id),
quantity INT , 

PRIMARY KEY(store_id , product_id)

);

--OrderTotals
CREATE TABLE OrderTotals (
    order_id INT PRIMARY KEY,
    counts_items INT,
    sums_money DECIMAL(10,2),
    CONSTRAINT FK_OrderTotals_Orders FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);








