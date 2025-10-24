from models.product_model import Product 
from db.connection import get_connection

def create_product(product: Product ):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """INSERT INTO products(id, barcode, name, brand, cost, price, profit, stock, area, expiration_date, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id"""
        
        cursor.execute(query,
                        (product.id,
                        product.barcode,
                        product.name,
                        product.brand,
                        product.cost,
                        product.price,
                        product.profit,
                        product.stock,
                        product.area,
                        product.expiration_date,
                        product.created_at
                    ))
        new_id = cursor.fetchone()[0]
        conn.commit()
        print(f"producto '{product.name}' ingresado con éxito")
        return new_id
    
    except Exception as e:
        print(f"Error al ingresar el producto '{product.name}':", e)
    finally:
        cursor.close()
        conn.close()

def get_all_products():
    products = []
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM products"

        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            products.append(Product(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
                ))
        
    except Exception as e:
        print(f"Error al obtener la lista: ", e)
    finally:
        cursor.close()
        conn.close()

    return products 