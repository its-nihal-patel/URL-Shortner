from flask import Flask, render_template, request, flash, redirect, abort
from inputform import InputForm
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = "j34D^$hIh%i7utv0"

shortened_urls = []

@app.route("/", methods=["GET", "POST"])
def index():
    form = InputForm()
    if request.method == "POST":
        if form.validate_on_submit():
            destination_url = form.url_input.data
            id = secrets.token_urlsafe(8)

            shortened_urls.append({"destination-url": destination_url, "id": id})

            form.url_input.data = ""

            flash(f"Success! Your Shortened URL: {request.base_url + id}", category="success message")
        else:
            flash("Invalid URL!", category="error message")
    return render_template("index.html", form=form)

@app.route("/<id>")
def redirect_user(id):
    for shortened_url in shortened_urls:
        if id == shortened_url["id"]:
            return redirect(shortened_url["destination-url"])

    return abort(404)

if __name__ == "__main__":
    app.run(port=5000, debug=True)