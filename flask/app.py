from flask import Flask,request
from uuid import uuid1,uuid4
import os,json,pytz
from datetime import date,datetime
password_list=[]
email_list=[]
db={}
db_filename="db.json"
#check whether db.json exist or not
if os.path.exists(db_filename):
    print("DB EXISTS")
    with open(db_filename,'r')as f:
        db=json.load(f)
else :
    print("DB DOESNOT EXISTS")
    accessKey=str(uuid1())
    secretKey=str(uuid4())
    item_type=["Food","Beverages","Clothing","Stationaries","Wearable","Electronic Accesories"]

    db={
        "accessKey":accessKey,
        "secretKey":secretKey,
        "item_type":item_type,
        "users":[]

    }
    with open(db_filename,"w") as f:
        json.dump(db,f,indent=4)
app=Flask(__name__)
#User sign up
@app.route('/signup',methods=['POST'])
def signup():
    if request.method=='POST':
        
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        username=request.form['username']
        userDict= {
            "name":name,
            "email":email,
            "password":password,
            "username":username,
            "purchases":{}
        }
     
        for i in db["users"]:
            email_list.append(i["email"])
      
        for i in db["users"]:
            password_list.append(i["password"])

        if len(db["users"])==0 or userDict["email"] not in email_list:
            db["users"].append(userDict)
            with open(db_filename,"r+") as f:
                f.seek(0)
                json.dump(db,f,indent=4)
            return "User added suucessfully"
        else:
            return "User already exists"
    return "Error:Trying to access endpoint with wrong method"
#user signin
@app.route('/signin',methods=['POST'])
def signin():
    if request.method=='POST':
        
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        username=request.form['username']
        userDict= {
            "name":name,
            "email":email,
            "password":password,
            "username":username,
            "purchases":{}
        }
        for i in password_list:

            if username==userDict["username"] and password == userDict["password"]:
                  with open(db_filename,"w") as f:
                     json.dump(db,f,indent=4) 
            else:
                print("Wrong USername and password")
 
if __name__=="__main__":
    app.run(host='0.0.0.0',port="5000",debug=True)

  
