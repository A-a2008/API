from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world"

@app.route('/add/<string:email>/')
def add(email):
    row = [email, True]
    with open("./data.csv", 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)
        print("Added to file")
    result = {
        "email": email,
        "allowed": True
    }
    return jsonify(result)

@app.route('/deny/<string:email>/')
def deny(email):
    rows = []
    with open("./data.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    for row in rows:
        if row[0] == email:
            rows[rows.index(row)][1] = False
            print("Tried to deny")
        # if row[0] == email:
        #     print(row[0], email)
        #     row[1] == False
        #     print(row, row[1])
        #     print("Edited")
    with open("./data.csv", 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(rows)
    result = {
        "email": email,
        "allowed": False
    }
    return jsonify(result)

@app.route('/allow/<string:email>/')
def allow(email):
    rows = []
    with open("./data.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    for row in rows:
        if row[0] == email:
            rows[rows.index(row)][1] = True
            print("Tried to deny")
        # if row[0] == email:
        #     print(row[0], email)
        #     row[1] == False
        #     print(row, row[1])
        #     print("Edited")
    with open("./data.csv", 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(rows)
    result = {
        "email": email,
        "allowed": True
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
