import sqlite3


def init_db():
    conn = sqlite3.connect('llmbase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products (
  	        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
  	        product_name VARCHAR(255) NOT NULL,
  	        price DECIMAL(10, 2) NOT NULL);
            ''')
    conn.commit()

    c.execute('''CREATE TABLE IF NOT EXISTS staff (
            staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL);
            ''')
    conn.commit()

    c.execute('''CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name VARCHAR(255) NOT NULL,
            staff_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            FOREIGN KEY (staff_id) REFERENCES staff (staff_id),
            FOREIGN KEY (product_id) REFERENCES products (product_id));
            ''')
    conn.commit()
    conn.close()
    print('Database created successfully')


def insert_data():
    conn = sqlite3.connect('llmbase.db')
    c = conn.cursor()
    c.execute("""
        INSERT INTO products (product_name, price) VALUES
        ('Laptop', 799.99),
        ('Keyboard', 129.99),
        ('Mouse', 29.99)
    """)
    conn.commit()

    c.execute("""
        INSERT INTO staff (first_name, last_name) VALUES
        ('John', 'Doe'),
        ('Jane', 'Smith'),
        ('Bob', 'Johnson')
    """)
    conn.commit()
    c.execute("""
        INSERT INTO orders (customer_name, staff_id, product_id) VALUES
        ('John Doe', 1, 1),
        ('Jane Smith', 2, 2),
        ('Bob Johnson', 3, 3)
    """)
    conn.commit()
    conn.close()
    print('Data inserted successfully')
