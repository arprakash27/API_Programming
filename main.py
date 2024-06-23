from flask import Flask, request, jsonify

app = Flask(__name__)

userdata_list = []


@app.route("/")
def home():
    return ('<a href="/next">'
            '<h1>Home</h1>'
            '</a>'
            '<a href="/get_user"'
            '<h1>get_user</h1>'
            '</a>')


@app.route("/next")
def power():
    return ('<a href="../">'
            '<h4>powered by python and Flash</h4>'
            '</a>')


@app.route("/create_user", methods=["POST"])
def create_user():
    if request.method == "POST":
        data = request.get_json()
        unique_key = True
        for userdata in userdata_list:
            if userdata['user_id'] == data['user_id']:
                unique_key = False
        if unique_key:
            userdata_list.append(data)
            response = data
            response_id = 201
            print(userdata_list)
        else:
            response = "User Data already exists"
            response_id = 0
            print(response)
        print('userdata_list' + str(len(userdata_list)))
        return jsonify(response), response_id


@app.route("/get_user")
def get_user():
    return jsonify(userdata_list), 200


if __name__ == "__main__":
    app.run(debug=True)
