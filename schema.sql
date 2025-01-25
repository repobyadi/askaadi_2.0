-- Create Suppliers Table
CREATE TABLE Suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_info TEXT NOT NULL,
    categories TEXT NOT NULL
);

-- Create Products Table
CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    supplier_id INT REFERENCES Suppliers(id)
);

-- Insert Sample Data for Suppliers
INSERT INTO Suppliers (name, contact_info, categories) VALUES
('Tech Supplies Inc.', 'contact@askaadi.com', 'Electronics, Laptops'),
('Gadget World', 'info@askaadi.com', 'Mobile, Accessories');

-- Insert Sample Data for Products
INSERT INTO Products (name, brand, price, category, description, supplier_id) VALUES
('Laptop Pro 15', 'BrandX', 1200.00, 'Laptops', 'A high-end laptop with 16GB RAM.', 1),
('Smartphone Y', 'BrandY', 699.99, 'Mobile', 'A smartphone with excellent camera.', 2);
