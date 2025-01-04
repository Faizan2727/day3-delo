from flask import Flask, render_template_string
import random

app = Flask(__name__)

# List of Santa-Banta jokes in Hinglish
jokes = [
    "Santa: Jab mobile girta hai toh sabse pehle kya toot'ta hai? Banta: Dil!",
    "Banta: Santa, tu apni wife ko kya gift de raha hai anniversary pe? Santa: Silence... woh priceless hai!",
    "Santa: Exam ke time padhai kyu nahi karta? Banta: Kyunki pen hi chhup jata hai... Destiny hai yaar!",
    "Santa: Mere phone ka Wi-Fi kaam nahi kar raha. Banta: Shaadi ke baad ka pyaar aur phone ka Wi-Fi kabhi perfect nahi hota.",
    "Banta: Agar log gyaan baant'te hain toh woh khud ameer kyu nahi ban jaate? Santa: Kya kare, free gyaan aur free Wi-Fi, dono me signal kam hota hai!",
]

# HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Santa-Banta Jokes</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 20%;
            background-color: #f9f9f9;
        }
        .joke-box {
            background: #fff;
            padding: 20px;
            margin: auto;
            width: 50%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 10px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            background: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #218838;
        }
    </style>
</head>
<body>
    <div class="joke-box">
        <h2>Santa-Banta Joke</h2>
        <p>{{ joke }}</p>
        <form action="/" method="get">
            <button type="submit">Show Another Joke</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Select a random joke
    random_joke = random.choice(jokes)
    return render_template_string(html_template, joke=random_joke)

if __name__ == '__main__':
    app.run(host="0.0.0.0")

