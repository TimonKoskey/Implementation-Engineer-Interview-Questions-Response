from flask import Flask, request, json

app = Flask(__name__)

@app.route("/")
def home_page():
    return 'This is an example of Webhook integration in Python using Flask and github'

@app.route("/github", methods=['POST'])
def data_from_github():
    if request.headers['Content-Type'] == 'application/json':
        my_data = json.dumps(request.json)
        print(my_data)
        return my_data

if __name__ == '__main__':
    app.run(debug=True)
