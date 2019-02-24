from flask import Flask, render_template, request
from process import do_process

app = Flask(__name__)

@app.route("/")
def home():
    #return "Hello, World!"
	return render_template("base.html")

@app.route("/process", methods=['GET'])
def process_get():
    return do_process(request.get_data())

if __name__ == "__main__":
    app.run(debug=True)