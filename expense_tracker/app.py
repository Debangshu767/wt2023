from flask import Flask, request
from uuid import uuid1, uuid4
import os, json, pytz
from datetime import date, datetime

db = {}
db_filename = "db.json"

# Check whether db.json exists in the directory or not
if os.path.exists(db_filename):
    with open(db_filename, 'r') as f:
        db = json.load(f)
else:
    accessKey = str(uuid1())
    secretKey = str(uuid4())

    item_types = [
        "Food", "Beverages", "Clothing", "Stationaries", 
        "Wearables", "Electronics Accessories"
    ]

    db = {
        "accessKey": accessKey,
        "secretKey": secretKey,
        "item_type": item_types,
        "users": []
    }

    with open(db_filename, "w+") as f:
        json.dump(db, f, indent=4)

app = Flask(__name__)

# User sign up
@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

        userDict = {
            "name": name,
            "email": email,
            "password": password,
            "username": username,
            "purchases": {}
        }

        email_list = []
        for element in db["users"]:
            email_list.append(element["email"])
        
        if len(db["users"]) == 0 or userDict["email"] not in email_list:
            db["users"].append(userDict)
            with open(db_filename, "r+") as f:
                f.seek(0)
                json.dump(db, f, indent=4)

            return "User added successfully"
        else:
            return "User already exists"
    return "Error: Trying to access endpoint with wrong method"

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    user_idx = None
    for user in db["users"]:
        if user["email"] == email and user["password"] == password:
            user_idx = db["users"].index(user)

            response = {
                "message": "logged in successfully",
                "user_index": user_idx
            }
            return response
        else:
            continue
    return "Wrong email or password!! Please try again"

@app.route("/add_purchase", methods=["POST"])
def add_purchase():
    user_idx = int(request.form["user_index"])
    item_name = request.form["item_name"]
    item_price = request.form["item_price"]
    item_type = request.form["item_type"]

    curr_date = str(date.today())
    curr_time = str(datetime.now(pytz.timezone("Asia/Kolkata")))

    print(curr_date, curr_time)

    itemDict = {
        "item_name": item_name,
        "item_type": item_type,
        "item_price": item_price,
        "purchase_time": curr_time
    }

    existing_dates = list(db["users"][user_idx]["purchases"].keys())
    print(existing_dates)
    if len(db["users"][user_idx]["purchases"]) == 0 or curr_date not in existing_dates:
        # If ther are no purchases user has done for the day
        db["users"][user_idx]["purchases"][curr_date] = []
        db["users"][user_idx]["purchases"][curr_date].append(itemDict)
        with open(db_filename, "r+") as f:
            f.seek(0)
            json.dump(db, f, indent=4)
        return "item added successfully"
    else:
        db["users"][user_idx]["purchases"][curr_date].append(itemDict)
        with open(db_filename, "r+") as f:
            f.seek(0)
            json.dump(db, f, indent=4)
        return "item added successfully"
    # return "Some error ocurred! Unable to add items"

    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="6000", debug=True)