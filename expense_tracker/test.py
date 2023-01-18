from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    print("I am in the /hello enpoint")
    return "hello"

users = [
    {
        "user_id": 1,
        "username": "user1"
    },
    {
        "user_id": 2,
        "username": "user2"
    }
]

# Create an endpoint to fetch all the user ids
@app.route('/fetch_user_ids')
def fetch_user_ids():
    user_ids = {"ids": []}
    for user in users:
        user_ids["ids"].append(user["user_id"])
    
    return user_ids

# Create an endpoint to fetch all the usernames


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)