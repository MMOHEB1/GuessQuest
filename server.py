from flask import Flask, render_template
import random
import gif_bank
app = Flask(__name__)
NUMBER = random.randint(0,20)




@app.route("/")
def hello_world():
    return (f"""
    <div style="
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
    ">
        <h1 style="text-align: center;">Guess a number between 0 and 20</h1>
        <img src={random.choice(gif_bank.default_gifs)} width="500" alt="Guessing Game GIF">
    </div>
    """)

@app.route("/<int:number>")
def too_low(number):
    if number > NUMBER:
        return (f"""
            <div style="
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
            ">
                <h1 style="text-align: center;">TOO HIGH! TRY AGAIN!</h1>
                <img src={random.choice(gif_bank.too_low_high)} width="500" alt="Guessing Game GIF">
            </div>
            """)
    elif number < NUMBER:
        return (f"""
                    <div style="
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    ">
                        <h1 style="text-align: center;">TOO LOW! TRY AGAIN!</h1>
                        <img src={random.choice(gif_bank.too_low_high)} width="500" alt="Guessing Game GIF">
                    </div>
                    """)
    else:
        return (f"""
                    <div style="
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    ">
                        <h1 style="text-align: center;">YOU GOT IT!!</h1>
                        <img src={random.choice(gif_bank.correct)} width="500" alt="Guessing Game GIF">
                    </div>
                    """)

if __name__ == "__main__":
    app.run(debug=True)