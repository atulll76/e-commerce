show databases;
CREATE DATABASE e_commerce;
USE e_commerce;
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(15),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

drop table user;
show tables;

CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15),
    date_of_birth DATE,
    disabled BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO User(first_name, last_name, username, email, password, phone_number, date_of_birth, disabled)
VALUES
('Atul', 'Chauhan', 'atul01', 'atul01@gmail.com', 'Atul@123', '9876543210', '2002-05-15', FALSE),
('Rahul', 'Sharma', 'rahul_s', 'rahul.sharma@gmail.com', 'Rahul@123', '9876543211', '1999-08-21', FALSE),
('Priya', 'Verma', 'priya_v', 'priya.verma@gmail.com', 'Priya@123', '9876543212', '2001-03-12', FALSE),
('Aman', 'Gupta', 'aman_g', 'aman.gupta@gmail.com', 'Aman@123', '9876543213', '1998-11-09', FALSE),
('Sneha', 'Patel', 'sneha_p', 'sneha.patel@gmail.com', 'Sneha@123', '9876543214', '2000-07-18', FALSE),
('Rohan', 'Mehta', 'rohan_m', 'rohan.mehta@gmail.com', 'Rohan@123', '9876543215', '1997-12-30', FALSE),
('Anjali', 'Reddy', 'anjali_r', 'anjali.reddy@gmail.com', 'Anjali@123', '9876543216', '2002-01-25', FALSE),
('Vikram', 'Singh', 'vikram_s', 'vikram.singh@gmail.com', 'Vikram@123', '9876543217', '1996-09-14', TRUE),
('Neha', 'Joshi', 'neha_j', 'neha.joshi@gmail.com', 'Neha@123', '9876543218', '2003-04-05', FALSE),
('Karan', 'Malhotra', 'karan_m', 'karan.malhotra@gmail.com', 'Karan@123', '9876543219', '1995-06-28', FALSE);

select * from user;



CREATE TABLE Address (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    add_line_one VARCHAR(50) NOT NULL,
    add_line_two VARCHAR(100),
    landmark VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'India',
    postal_code VARCHAR(10) NOT NULL,
    address_type ENUM('Home', 'Office', 'Other') DEFAULT 'Home',
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_address_user
        FOREIGN KEY (user_id)
        REFERENCES User(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO Address(user_id, add_line_one, add_line_two, landmark, city, state, country, postal_code, address_type, is_default)
VALUES
(1, 'House No. 12', 'Green Park Colony', 'Near City Mall', 'Delhi', 'Delhi', 'India', '110016', 'Home', TRUE),
(2, 'Flat 304', 'Sunshine Apartments', 'Opp. Central Park', 'Jaipur', 'Rajasthan', 'India', '302001', 'Home', TRUE),
(3, '45 MG Road', 'Sector 18', 'Near Metro Station', 'Noida', 'Uttar Pradesh', 'India', '201301', 'Office', TRUE),
(4, '221 Baker Street', 'Civil Lines', 'Near Railway Station', 'Lucknow', 'Uttar Pradesh', 'India', '226001', 'Home', TRUE),
(5, '78 Lake View', 'Phase 2', 'Near City Hospital', 'Bhopal', 'Madhya Pradesh', 'India', '462001', 'Other', FALSE),
(6, '19 Palm Avenue', 'Whitefield', 'Near Tech Park', 'Bengaluru', 'Karnataka', 'India', '560066', 'Office', TRUE),
(7, '88 Rose Villa', 'Baner Road', 'Near Balewadi Stadium', 'Pune', 'Maharashtra', 'India', '411045', 'Home', TRUE),
(8, '16 Beach Road', 'Anna Nagar', 'Near Marina Beach', 'Chennai', 'Tamil Nadu', 'India', '600040', 'Home', TRUE),
(9, '55 Ring Road', 'Satellite', 'Near ISKCON Temple', 'Ahmedabad', 'Gujarat', 'India', '380015', 'Other', FALSE),
(10, '32 Hill View', 'Banjara Hills', 'Near GVK Mall', 'Hyderabad', 'Telangana', 'India', '500034', 'Home', TRUE);

select * from Address ;

CREATE TABLE Manufacturer (
    manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
    manufacturer_name VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    website VARCHAR(255),
    address VARCHAR(255),
    country VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO Manufacturer (manufacturer_name, email, phone_number, website, address, country, is_active)
VALUES
('Nike', 'contact@nike.com', '+1-800-111-0001', 'https://www.nike.com', 'One Bowerman Dr, Beaverton, Oregon', 'USA', TRUE),
('Adidas', 'info@adidas.com', '+49-9132-111111', 'https://www.adidas.com', 'Adi-Dassler-Strasse 1, Herzogenaurach', 'Germany', TRUE),
('Puma', 'support@puma.com', '+49-9132-810', 'https://www.puma.com', 'Puma Way 1, Herzogenaurach', 'Germany', TRUE),
('Reebok', 'info@reebok.com', '+1-800-111-0002', 'https://www.reebok.com', 'Boston, Massachusetts', 'USA', TRUE),
('New Balance', 'support@newbalance.com', '+1-800-111-0003', 'https://www.newbalance.com', 'Boston, Massachusetts', 'USA', TRUE),
('ASICS', 'contact@asics.com', '+81-78-303-2231', 'https://www.asics.com', 'Kobe', 'Japan', TRUE),
('Skechers', 'info@skechers.com', '+1-800-111-0004', 'https://www.skechers.com', 'Manhattan Beach, California', 'USA', TRUE),
('Under Armour', 'support@underarmour.com', '+1-800-111-0005', 'https://www.underarmour.com', 'Baltimore, Maryland', 'USA', TRUE),
('Fila', 'contact@fila.com', '+82-2-1234-5678', 'https://www.fila.com', 'Seoul', 'South Korea', TRUE),
('Converse', 'info@converse.com', '+1-800-111-0006', 'https://www.converse.com', 'Boston, Massachusetts', 'USA', TRUE);

select * from Manufacturer;

CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    category_description VARCHAR(255),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Category
(category_name, category_description)
VALUES
('Men''s Shoes', 'Footwear for men'),
('Women''s Shoes', 'Footwear for women'),
('Kids'' Shoes', 'Footwear for children'),
('Sports Shoes', 'Running, training and sports footwear'),
('Running Shoes', 'Shoes designed for running'),
('Casual Shoes', 'Daily wear casual footwear'),
('Formal Shoes', 'Office and business footwear'),
('Sneakers', 'Fashion sneakers'),
('Boots', 'Ankle and long boots'),
('Sandals', 'Open footwear'),
('Slippers', 'Indoor and outdoor slippers'),
('Flip Flops', 'Beach and casual flip flops'),
('Loafers', 'Slip-on loafers'),
('Heels', 'Women''s heels'),
('Ethnic Footwear', 'Traditional footwear'),
('Leather Shoes', 'Genuine leather footwear'),
('Walking Shoes', 'Shoes for walking'),
('Hiking Shoes', 'Outdoor trekking shoes'),
('Basketball Shoes', 'Basketball footwear'),
('Football Shoes', 'Football studs and boots'),
('Tennis Shoes', 'Tennis footwear'),
('Gym Shoes', 'Workout and training shoes'),
('Safety Shoes', 'Industrial safety footwear'),
('Accessories', 'Socks, insoles, laces and shoe care'),
('Sale', 'Discounted products');

CREATE TABLE Product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    manufacturer_id INT NOT NULL,
    category_id INT NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    product_description TEXT,
    color VARCHAR(50),
    size VARCHAR(20),
    material VARCHAR(100),
    gender ENUM('Men', 'Women', 'Kids', 'Unisex') DEFAULT 'Unisex',
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    image_url VARCHAR(255),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product_manufacturer
        FOREIGN KEY (manufacturer_id)
        REFERENCES Manufacturer(manufacturer_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_product_category
        FOREIGN KEY (category_id)
        REFERENCES Category(category_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

INSERT INTO Product (manufacturer_id, category_id, product_name, product_description, color, size, material, gender, price, stock_quantity, image_url, is_active)
VALUES
(1, 4, 'Nike Air Zoom Pegasus 40', 'Lightweight running shoes with responsive cushioning.', 'Black', '9', 'Mesh', 'Men', 6999.00, 50, 'nike_pegasus40.jpg', TRUE),
(2, 8, 'Adidas Superstar', 'Classic leather sneakers for everyday wear.', 'White', '8', 'Leather', 'Unisex', 5999.00, 35, 'adidas_superstar.jpg', TRUE),
(3, 6, 'Puma Smash V2', 'Comfortable casual sneakers.', 'Blue', '10', 'Canvas', 'Men', 4499.00, 60, 'puma_smash_v2.jpg', TRUE),
(4, 7, 'Reebok Classic Leather', 'Premium leather casual shoes.', 'Brown', '9', 'Leather', 'Men', 5499.00, 30, 'reebok_classic.jpg', TRUE),
(5, 5, 'New Balance Fresh Foam', 'High-performance running shoes.', 'Grey', '8', 'Mesh', 'Women', 7499.00, 40, 'newbalance_freshfoam.jpg', TRUE),
(6, 4, 'ASICS Gel Nimbus 27', 'Comfortable running shoes with GEL cushioning.', 'Navy Blue', '9', 'Mesh', 'Men', 8999.00, 25, 'asics_gelnimbus.jpg', TRUE),
(7, 6, 'Skechers Go Walk', 'Lightweight walking shoes.', 'Black', '7', 'Fabric', 'Women', 4999.00, 55, 'skechers_gowalk.jpg', TRUE),
(8, 4, 'Under Armour Charged Assert', 'Training shoes for gym and running.', 'Red', '10', 'Synthetic', 'Men', 6499.00, 45, 'ua_charged_assert.jpg', TRUE),
(9, 8, 'Fila Disruptor II', 'Chunky fashion sneakers.', 'Pink', '6', 'Leather', 'Women', 3999.00, 20, 'fila_disruptor.jpg', TRUE),
(10, 8, 'Converse Chuck Taylor All Star', 'Iconic high-top canvas sneakers.', 'White', '9', 'Canvas', 'Unisex', 5299.00, 70, 'converse_chuck_taylor.jpg', TRUE);

select * from Product;

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    address_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2) NOT NULL,
    order_status ENUM(
        'Pending',
        'Confirmed',
        'Packed',
        'Shipped',
        'Out for Delivery',
        'Delivered',
        'Cancelled',
        'Returned'
    ) DEFAULT 'Pending',
    payment_status ENUM(
        'Pending',
        'Paid',
        'Failed',
        'Refunded'
    ) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_order_user
        FOREIGN KEY (user_id)
        REFERENCES User(user_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_order_address
        FOREIGN KEY (address_id)
        REFERENCES Address(address_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
INSERT INTO Orders
(user_id, address_id, order_date, total_amount, order_status, payment_status)
VALUES
(1, 1, '2026-06-01 10:15:30', 6999.00, 'Delivered', 'Paid'),
(2, 2, '2026-06-02 14:25:10', 5999.00, 'Shipped', 'Paid'),
(3, 3, '2026-06-03 09:45:20', 8998.00, 'Pending', 'Pending'),
(4, 4, '2026-06-04 16:30:45', 5499.00, 'Delivered', 'Paid'),
(5, 5, '2026-06-05 11:20:15', 7499.00, 'Confirmed', 'Paid'),
(6, 6, '2026-06-06 18:10:50', 4999.00, 'Packed', 'Paid'),
(7, 7, '2026-06-07 13:40:35', 6499.00, 'Out for Delivery', 'Paid'),
(8, 8, '2026-06-08 15:55:40', 3999.00, 'Cancelled', 'Refunded'),
(9, 9, '2026-06-09 12:05:25', 5299.00, 'Returned', 'Refunded'),
(10, 10, '2026-06-10 17:45:55', 11498.00, 'Delivered', 'Paid');
select * from Orders;

CREATE TABLE Order_Product (
    order_product_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_orderproduct_order
        FOREIGN KEY (order_id)
        REFERENCES Orders(order_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_orderproduct_product
        FOREIGN KEY (product_id)
        REFERENCES Product(product_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

INSERT INTO Order_Product
(order_id, product_id, quantity, unit_price, subtotal)
VALUES
(1, 1, 1, 6999.00, 6999.00),
(2, 2, 1, 5999.00, 5999.00),
(3, 3, 2, 4499.00, 8998.00),
(4, 4, 1, 5499.00, 5499.00),
(5, 5, 1, 7499.00, 7499.00),
(6, 6, 1, 8999.00, 8999.00),
(7, 7, 2, 4999.00, 9998.00),
(8, 8, 1, 6499.00, 6499.00),
(9, 9, 3, 3999.00, 11997.00),
(10, 10, 2, 5299.00, 10598.00);

CREATE TABLE Review (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    rating INT NOT NULL,
    review_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_rating
        CHECK (rating BETWEEN 1 AND 5),
    CONSTRAINT fk_review_user
        FOREIGN KEY (user_id)
        REFERENCES User(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_review_product
        FOREIGN KEY (product_id)
        REFERENCES Product(product_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO Review (user_id, product_id, rating, review_description)
VALUES
(1, 1, 5, 'Excellent quality and very comfortable for daily running.'),
(2, 2, 4, 'Stylish sneakers with good comfort, but slightly expensive.'),
(3, 3, 5, 'Perfect fit and lightweight. Highly recommended.'),
(4, 4, 3, 'Good product, but the size runs a little small.'),
(5, 5, 5, 'Amazing cushioning and premium build quality.'),
(6, 6, 4, 'Very comfortable for long walks and workouts.'),
(7, 7, 5, 'Worth every penny. Great grip and durability.'),
(8, 8, 2, 'Product quality was average and delivery was delayed.'),
(9, 9, 4, 'Looks exactly as shown and fits perfectly.'),
(10, 10, 5, 'Fantastic shoes with excellent comfort and style.');

select * from Review;

CREATE TABLE Cart (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_cart_user
        FOREIGN KEY (user_id)
        REFERENCES User(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_cart_product
        FOREIGN KEY (product_id)
        REFERENCES Product(product_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO Cart
(user_id, product_id, quantity)
VALUES
(1, 2, 1),
(2, 5, 2),
(3, 1, 1),
(4, 7, 3),
(5, 4, 1),
(6, 10, 2),
(7, 6, 1),
(8, 3, 2),
(9, 8, 1),
(10, 9, 4);
CREATE TABLE Wishlist (
    wishlist_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_wishlist_user
        FOREIGN KEY (user_id)
        REFERENCES User(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_wishlist_product
        FOREIGN KEY (product_id)
        REFERENCES Product(product_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT uq_wishlist UNIQUE (user_id, product_id)
);
INSERT INTO Wishlist (user_id, product_id)
VALUES
(1, 5),
(2, 3),
(3, 8),
(4, 1),
(5, 10),
(6, 7),
(7, 2),
(8, 9),
(9, 4),
(10, 6);
 
 show tables;