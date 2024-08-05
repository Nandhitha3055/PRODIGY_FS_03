from flask import *
from flask_session import Session
from hash import Pass_hashing
from database import UserClass
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
hp = Pass_hashing()
db = UserClass()
UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SESSION_COOKIE_NAME'] = 'my_session'
app.config['SESSION_COOKIE_SECURE'] = True
Session(app)

@app.route('/')  #login page
def home():
    return render_template("home.html", name ="")


@app.route('/index')
def index():
    # products = db.get_all_products()
    # return render_template("ecom.html", products = products)
    return render_template("ecom-index.html")

@app.route('/category')
def category():
    products = db.get_all_products()
    return render_template("ecom.html", products = products)

@app.route('/fruits')
def fruits():
    products = db.fruits()
    return render_template("ecom.html", products = products)

@app.route('/vegetables')
def vegetables():
    products = db.vegetables()
    return render_template("ecom.html", products = products)
    # return render_template("ecom-index.html")



@app.route("/signup") #signup page
def signup():
    return render_template("home.html", name="signup")

@app.route('/get', methods=['POST']) #login verification and admin or user 
def get():
    email = request.form['email']
    password = request.form['Password']
    hashed = db.get_user(email)
    if hashed != None:
        if hp.verify_pass(hashed,password):
            session["name"] = email
            session["user_type"] = db.get_user_type(email)
            return redirect(url_for("index"))   
    return render_template("home.html", name ="Email or Password is not a match")


@app.route('/verify', methods=['POST']) #signup page string data in database
def verify():
    if request.method == "POST":
        first = request.form["FirstName"]
        last = request.form["LastName"]
        phone = request.form["PhoneNumber"]
        email = request.form["email"]
        password = hp.hashing_pass(request.form["Password"])
        # print(password)
        file = request.files['file']
        if file:
            original_filename = secure_filename(file.filename)
            new_filename = email+'.png'
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
            file.save(file_path)
        if not db.existing_User(email):
            db.insert_user(first,last,phone,email,file_path,password,"User")
            return render_template("user.html",name = "Account Successfully Created",page = "login")
        else:
            return render_template("user.html",name = "User Already Exists",page = "login")
    return render_template("home.html",name ="Sign in")


@app.route('/add_to_cart', methods=["POST"])
def add_to_cart():
    productID = request.form["productId"]
    quantity = request.form["quantity"]
    quantity = int(quantity)    
    product = db.get_product(productID)
    db.change_quantity(productID,quantity)
    db.add_cart(session["name"],product[0],productID,product[2],product[4],product[5],quantity)
    return redirect(url_for("index"))

@app.route('/cart')
def cart():
    cus = session["name"]
    carts = db.get_cart(cus)
    getQuant = db.get_quant(cus)
    total = int(sum(quantity * price for quantity, price in getQuant))
    print(total)
    return render_template("cart.html",carts = carts,total = total)

# Product_Name,ProductId,Category,Price,Image,Quantity


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080,debug = True)