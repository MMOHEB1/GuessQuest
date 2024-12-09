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

@app.route("/<int:number>")
def too_low(number):
    return (f"""
        <div style="
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        ">
            <h1 style="text-align: center;">your number: {number}</h1>
            <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnZsY3VjMnNjcWZxMTg4dnE0cnk1anhndnl1Y2t1c3V5aW9odmg5aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IQYfvE9kIIFCiRweFa/giphy.gif" width="500" alt="Guessing Game GIF">
        </div>
        """)

if __name__ == "__main__":
    app.run(debug=True)