from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "<h1>homepage</h1>"


@app.route('/formpage', methods=['GET'])
def my_form_page():
    return render_template("formpage.html")


@app.route('/feedback', methods=['POST'])
def feedback():
    result=request.form
    mycolour="style= &quot; background-color: {} ; &quot; ".format(request.form["favcolor"])
    return render_template("feedback.html", result=result, mycolour = mycolour)


if __name__ == "__main__":
    app.run(debug = True)