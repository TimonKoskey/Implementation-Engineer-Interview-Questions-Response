from flask import Flask, jsonify

app = Flask(__name__)

colors = [
	{
		'color': "red",
		'value': "#f00"
	},
	{
		'color': "green",
		'value': "#0f0"
	},
	{
		'color': "blue",
		'value': "#00f"
	},
	{
		'color': "cyan",
		'value': "#0ff"
	},
	{
		'color': "magenta",
		'value': "#f0f"
	},
	{
		'color': "yellow",
		'value': "#ff0"
	},
	{
		'color': "black",
		'value': "#000"
	}
]

@app.route("/")
def home_page():
    return 'This is an example of API integration in Python using Flask'

@app.route("/colors/all", methods=['GET'])
def get_colors():
    return jsonify(colors)



if __name__ == '__main__':
    app.run(debug=True)
