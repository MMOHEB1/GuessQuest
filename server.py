from flask import Flask, render_template
import random
app = Flask(__name__)


# randnum = random.randint(0, 20)
# def number_check(func):
#     def wrapper():


@app.route("/")
def hello_world():
    return ("""
    <div style="
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
    ">
        <h1 style="text-align: center;">Guess a number between 0 and 20</h1>
        <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTA4aGk1amppYzUxa2FwdWg3ZWdnN25idWFpb2NvMnlpc2RxZ3FyOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nTZt1E0IM8sKSEVirG/giphy.gif" width="500" alt="Guessing Game GIF">
    </div>
    """)

@app.route("/<4>")
def too_low(*args, **kwargs):
    return ("""
        <div style="
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        ">
            <h1 style="text-align: center;">Guess a number between 0 and 20</h1>
            <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTA4aGk1amppYzUxa2FwdWg3ZWdnN25idWFpb2NvMnlpc2RxZ3FyOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nTZt1E0IM8sKSEVirG/giphy.gif" width="500" alt="Guessing Game GIF">
        </div>
        """)

if __name__ == "__main__":
    app.run(debug=True)