-- Criação da tabela de produtos (bicicletas)
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(100),
    price NUMERIC(10, 2) NOT NULL
);

-- Criação da tabela de clientes
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE
);

-- Criação da tabela de vendas
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    product_id INT REFERENCES products(product_id),
    sale_date DATE NOT NULL,
    quantity INT NOT NULL
);

-- Inserindo alguns dados de exemplo
INSERT INTO products (name, brand, price) VALUES
('Mountain Bike Pro', 'Caloi', 3500.00),
('Speed Demon', 'Specialized', 7200.50),
('City Cruiser', 'Trek', 2100.75),
('BMX Freestyle', 'GT', 1800.00);

INSERT INTO customers (name, email) VALUES
('João Silva', 'joao.silva@example.com'),
('Maria Oliveira', 'maria.o@example.com'),
('Carlos Pereira', 'carlos.p@example.com');

INSERT INTO sales (customer_id, product_id, sale_date, quantity) VALUES
(1, 1, '2024-07-10', 1),
(2, 3, '2024-07-12', 2),
(1, 2, '2024-07-15', 1),
(3, 1, '2024-07-20', 1),
(2, 4, '2024-07-22', 1);
