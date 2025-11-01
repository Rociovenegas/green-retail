-- ==================================================
-- CREATE TABLES
-- ==================================================

-- Products table
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    stock INTEGER DEFAULT 0,
    keywords TEXT,
    pollution_score DECIMAL(10, 2),
    social_score DECIMAL(10, 2),
    economic_score DECIMAL(10, 2),
    sustainability_score DECIMAL(10, 2)
);

-- Stores table
CREATE TABLE IF NOT EXISTS stores (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT
);

-- Products per store (pricing and availability)
CREATE TABLE IF NOT EXISTS store_products (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    store_id INTEGER REFERENCES stores(id) ON DELETE CASCADE,
    price DECIMAL(10, 2) NOT NULL,
    stock INTEGER DEFAULT 0,
    UNIQUE(product_id, store_id)
);

-- ==================================================
-- CREATE INDEXES
-- ==================================================

CREATE INDEX IF NOT EXISTS idx_store_products ON store_products(product_id, store_id);
CREATE INDEX IF NOT EXISTS idx_products_name ON products(name);
CREATE INDEX IF NOT EXISTS idx_store_products_price ON store_products(price);
CREATE INDEX IF NOT EXISTS idx_store_products_stock ON store_products(stock);

-- ==================================================
-- INSERT SAMPLE DATA
-- ==================================================

-- Insert products
INSERT INTO products (name, stock, keywords, pollution_score, social_score, economic_score) VALUES
    ('Whole Wheat Bread', 50, 'bakery, cereals, grains', 0.5, 7.0, 8.0),
    ('Whole Milk 1L', 30, 'dairy, lactose, milk', 1.2, 6.5, 7.5),
    ('Eggs Dozen', 40, 'dairy, protein, eggs', 2.1, 7.5, 8.5),
    ('White Rice 1kg', 100, 'grains, carbohydrates, staple', 0.8, 6.0, 9.0),
    ('Apples 1kg', 60, 'fruits, healthy, organic', 0.3, 8.0, 7.0),
    ('Chicken Breast 1kg', 25, 'meat, protein, poultry', 6.5, 5.5, 6.0),
    ('Vegetable Oil 1L', 45, 'pantry, fats, cooking', 3.2, 6.0, 7.0),
    ('Pasta 500g', 80, 'grains, carbohydrates, italian', 1.1, 7.0, 8.5),
    ('Fresh Tomatoes 1kg', 70, 'vegetables, fresh, healthy', 0.4, 8.5, 6.5),
    ('Cheddar Cheese 500g', 35, 'dairy, cheese, protein', 2.8, 7.0, 5.5),
    ('Orange Juice 1L', 40, 'drinks, juice, vitamin-c', 1.5, 7.5, 6.0),
    ('Ground Beef 1kg', 20, 'meat, protein, beef', 8.5, 5.0, 5.5),
    ('Brown Sugar 1kg', 90, 'pantry, sweetener, baking', 0.6, 6.5, 8.0),
    ('Yogurt 1L', 55, 'dairy, probiotics, healthy', 1.0, 8.0, 7.5),
    ('Bananas 1kg', 75, 'fruits, potassium, energy', 0.2, 8.5, 8.5);

-- Insert stores
INSERT INTO stores (name, address) VALUES
    ('Super Saver Market', '123 Main Avenue'),
    ('Green Eco Store', '456 Ecology Street'),
    ('Quick Express Mart', '789 Mall Center');

-- Insert store products (product_id, store_id, price, stock)
INSERT INTO store_products (product_id, store_id, price, stock) VALUES
    -- Whole Wheat Bread
    (1, 1, 1200, 50), (1, 2, 1300, 40), (1, 3, 1150, 60),
    -- Whole Milk 1L
    (2, 1, 900, 30), (2, 2, 950, 25), (2, 3, 880, 35),
    -- Eggs Dozen
    (3, 1, 2500, 40), (3, 2, 2600, 30), (3, 3, 2450, 45),
    -- White Rice 1kg
    (4, 1, 1500, 100), (4, 2, 1450, 80), (4, 3, 1550, 90),
    -- Apples 1kg
    (5, 1, 1800, 60), (5, 2, 1750, 50), (5, 3, 1850, 70),
    -- Chicken Breast 1kg
    (6, 1, 4500, 25), (6, 2, 4600, 20), (6, 3, 4450, 30),
    -- Vegetable Oil 1L
    (7, 1, 3200, 45), (7, 2, 3100, 40), (7, 3, 3250, 50),
    -- Pasta 500g
    (8, 1, 800, 80), (8, 2, 850, 70), (8, 3, 780, 90),
    -- Fresh Tomatoes 1kg
    (9, 1, 1600, 70), (9, 2, 1550, 60), (9, 3, 1650, 80),
    -- Cheddar Cheese 500g
    (10, 1, 3500, 35), (10, 2, 3600, 30), (10, 3, 3450, 40),
    -- Orange Juice 1L
    (11, 1, 2200, 40), (11, 2, 2300, 35), (11, 3, 2150, 45),
    -- Ground Beef 1kg
    (12, 1, 5500, 20), (12, 2, 5600, 15), (12, 3, 5450, 25),
    -- Brown Sugar 1kg
    (13, 1, 1100, 90), (13, 2, 1050, 80), (13, 3, 1150, 95),
    -- Yogurt 1L
    (14, 1, 1400, 55), (14, 2, 1450, 50), (14, 3, 1350, 60),
    -- Bananas 1kg
    (15, 1, 1000, 75), (15, 2, 950, 70), (15, 3, 1050, 80);