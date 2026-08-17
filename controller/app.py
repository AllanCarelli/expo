from flask import Flask, render_template

app = Flask(__name__,template_folder="../Template/",static_folder="../Static/")

@app.route("/")
def title_screen():
    return render_template("index.html")

@app.route("/game/")
def game():

    return render_template("game.html")



def main():
    app.run(debug=True)


if __name__  == "__main__":
    main()