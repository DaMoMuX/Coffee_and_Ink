from db.connection import get_connection

def create_table_products():
    conn = get_connection()

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY,
                    barcode VARCHAR(50) NOT NULL,
                    name VARCHAR(50) UNIQUE NOT NULL,
                    brand VARCHAR(50),
                    cost NUMERIC(10, 2) NOT NULL,
                    price NUMERIC(10, 2) NOT NULL,
                    profit NUMERIC(10, 2) NOT NULL,
                    stock INT NOT NULL DEFAULT 1,
                    area VARCHAR(20),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
            )
            conn.commit()
            print("Table 'products' is ready...")
        except Exception as e:
            print("Error while creating: ", e)
        finally:
            cursor.close()
            conn.close()
            print("Connection closed succesfully...")
    else:
        print("Error while connecting...")