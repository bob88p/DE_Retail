CREATE DATABASE  Retail_DB ;

USE Retail_DB




--Brands
CREATE TABLE Brands (

brand_id INT PRIMARY KEY  , 
brand_name VARCHAR(40) 
);



--Categories
CREATE TABLE Categories (

category_id INT PRIMARY KEY  , 
category_name VARCHAR(40) 
);




--Customers
CREATE TABLE Customers (

customer_id INT PRIMARY KEY  , 
first_name VARCHAR(40) ,
last_name VARCHAR(40) ,
full_name AS (first_name + ' ' + last_name),
phone VARCHAR(40) ,
email VARCHAR(100) ,  
street VARCHAR(100) ,
city VARCHAR(40) ,
state VARCHAR(40) ,
zip_code INT    

);




 
-- Stores
CREATE TABLE Stores (

store_id INT PRIMARY KEY  , 

store_name VARCHAR(40) ,
phone VARCHAR(40) ,
email VARCHAR(100) , 
street VARCHAR(40) ,
city VARCHAR(40) ,
state VARCHAR(40) ,
zip_code INT    

);



-- Staffs
CREATE TABLE Staffs (

staff_id INT PRIMARY KEY  , 

first_name VARCHAR(40) ,
last_name VARCHAR(40) ,
full_name AS (first_name + ' ' + last_name),
active BIT ,
phone VARCHAR(40) ,
email VARCHAR(40) , 
store_id INT NULL FOREIGN KEY REFERENCES  Stores(store_id),

manager_id INT NULL  FOREIGN KEY REFERENCES  Staffs(staff_id)
);




 -- Products
CREATE TABLE Products (

product_id INT PRIMARY KEY  , 

product_name VARCHAR(40) ,
 
brand_id INT FOREIGN KEY REFERENCES  Brands(brand_id),

category_id INT FOREIGN KEY REFERENCES  Categories(category_id),

model_year INT ,

list_price DECIMAL(10,2)

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









