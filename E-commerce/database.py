import sqlite3
conn = sqlite3.connect("Users.db",check_same_thread=False)

c = conn.cursor()
class UserClass:
    def __init__(self):
        pass
    def create_table(self):
        with conn:
            c.execute('''CREATE TABLE IF NOT EXISTS users(First_Name TEXT,Last_Name TEXT,Phone_Number INTEGER ,Email TEXT PRIMARY KEY,Address TEXT,Image TEXT,Password TEXT,User_Type TEXT)''')

    def product_table(self):
        with conn:
            c.execute('''CREATE TABLE IF NOT EXISTS products(Product_Name TEXT,ProductId INTEGER PRIMARY KEY AUTOINCREMENT,Category TEXT,Quantity INTEGER,Price REAL,Image TEXT,Description TEXT)''')

    def cart_table(self):
        with conn:
            c.execute('''CREATE TABLE IF NOT EXISTS cart(Customer TEXT,Product_Name TEXT,ProductId INTEGER,Category TEXT,Price REAL,Image TEXT,Quantity INTEGER)''')


    def insert_user(self,first_name,last_name,phone_number,email,file_path,password,user_type):
        with conn:
            c.execute("INSERT INTO users(First_Name, Last_Name,Phone_Number, Email,Image, Password,User_Type) VALUES(?,?,?,?,?,?,?)",(first_name,last_name,phone_number,email,file_path,password,user_type))

    def delete_User(self,email):
        with conn:
            c.execute(f"DELETE FROM users WHERE Email = '{email}'")

    def existing_User(self,email):
        c.execute(f"SELECT * FROM users WHERE Email = '{email}'")
        if c.fetchone() is None:
            return False
        else:
            return True
            
    def get_user(self,email):
        c.execute(f"SELECT Password FROM users WHERE Email = '{email}'")
        result = c.fetchone()
        if result:
            return result[0]
        else:
            return None

    def get_user_details(self,email):
        c.execute(f"SELECT * FROM users WHERE Email = '{email}'")
        result = c.fetchone()
        return result

    def get_user_type(self,email):
        c.execute(f"SELECT User_Type FROM users WHERE Email = '{email}'")
        return c.fetchone()[0]

    def all_user(self):  
        c.execute("SELECT Email,First_Name FROM users WHERE User_Type = 'User'")
        result = c.fetchall()
        leng = len(result)  
        return [result,leng]  

    def get_user_img(self,email):
        c.execute(f"SELECT Image FROM users WHERE Email = '{email}'") 
        return c.fetchone()[0]

#table for products========================================
    def get_all_products(self):
        c.execute("SELECT * FROM products")
        return c.fetchall()
    def fruits(self):
        c.execute("SELECT * FROM products WHERE Category = 'Fruit'")
        return c.fetchall()
    def vegetables(self):
        c.execute("SELECT * FROM products WHERE Category = 'Vegetable'")
        return c.fetchall()

    def get_product(self,productId):
        c.execute(f"SELECT Product_Name,ProductId,Category,Quantity,Price,Image FROM products WHERE ProductId = {productId}")
        return c.fetchone()


#table for cart==============================================================================
    def add_cart(self,Customer,Product_Name,ProductId,Category,Price,Image,Quantity):
        with conn:
            c.execute("INSERT INTO cart(Customer,Product_Name,ProductId,Category,Price,Image,Quantity) VALUES(?,?,?,?,?,?,?)",(Customer,Product_Name,ProductId,Category,Price,Image,Quantity))

    def change_quantity(self,ProductId,quantity):
        c.execute(f"SELECT Quantity FROM products WHERE ProductId = {ProductId}")
        result = c.fetchone()[0]
        newQuant = result - int(quantity)
        with conn:
            c.execute(f"UPDATE products SET Quantity = {newQuant} WHERE ProductId = {ProductId}")

    def get_cart(self,Customer):
        c.execute("SELECT * FROM cart WHERE Customer = ?", (Customer,))
        return c.fetchall()

    def get_quant(self,Customer):
        c.execute("SELECT Price,Quantity FROM cart WHERE Customer = ?", (Customer,))
        return c.fetchall()    

        # (Product_Name,Category,Quantity,Price,Image,Description)
# data = [("Bananas","Fruit",500,10.50,"static/images/bananas.jpg","Fresh and sweet bananas, perfect for a quick snack or adding a touch of natural sweetness."),
#        ("Grapes","Fruit",500,15.20,"static/images/grapes.jpg","juicy grapes, a refreshing snack packed with antioxidants, vitamins, and hydration."),
#        ("Raspberries","Fruit",500,13.20,"static/images/raspberries.jpg","Vibrant and tangy raspberries, bursting with flavor and packed with antioxidants, vitamins, and dietary fiber."),
#        ("Strawberries","Fruit",500,13.60,"static/images/strawberries.jpg","Sweet and succulent strawberries, rich in antioxidants, vitamins, and fiber."),
#        ("Sugar-apple","Fruit",500,9.50,"static/images/sugar-apple.jpg","Sweet and creamy sugar-apples, known for their unique flavor and smooth texture."),
#        ("Beetroot","Vegetable",500,9.50,"static/images/beetroot.jpg","Earthy and vibrant beetroot, rich in essential nutrients like vitamins, minerals, and antioxidants. "),
#        ("Carrots","Vegetable",500,5.10,"static/images/carrots.jpg","Crunchy and sweet carrots, packed with beta-carotene, vitamins, and fiber."),
#        ("Cucumbers","Vegetable",500,8.90,"static/images/cucumbers.jpg","Refreshing and crisp cucumbers, low in calories and high in hydration."),
#        ("Onions","Vegetable",500,8.40,"static/images/onions.jpg","Flavorful and versatile onions, essential for adding depth to a wide range of dishes."),
#        ("Tomatoes","Vegetable",500,6.70,"static/images/tomatoes.jpg","Juicy and tangy tomatoes, packed with vitamins, antioxidants, and flavor.")]


# with conn:
#     c.executemany('''
#     INSERT INTO products(Product_Name,Category,Quantity,Price,Image,Description)
#     VALUES (?,?,?,?,?,?)
#     ''', data)
    

c.execute("SELECT * FROM products")
print(c.fetchall())
# c.execute("SELECT Quantity FROM products WHERE ProductId = 1")
# result = c.fetchone()[0]
# print(type(result))
# c.execute("DROP TABLE products")
