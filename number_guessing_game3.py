from flask import Flask, request
from random import randint

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reverse Number Guessing Game</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container text-center mt-5">
    <h1>Reverse Number Guessing Game</h1>
    {message_section}
    {game_section}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def guess_number():
    if request.method == "POST":
        min_val = int(request.form["min"])
        max_val = int(request.form["max"])

        if "too_small" in request.form:
            min_val = int(request.form["guess"]) + 1
        elif "too_big" in request.form:
            max_val = int(request.form["guess"]) - 1
        elif "correct" in request.form:
            return html_template.format(
                message_section="<h2 class='mt-3'>I guessed it!</h2><a href='/' class='btn btn-primary mt-3'>Play Again</a>",
                game_section=""
            )
        
        if min_val > max_val:
            return html_template.format(
                message_section="<h2 class='mt-3'>Something went wrong! Try again.</h2>",
                game_section=""
            )
        guess = (min_val + max_val) // 2
    else:
        min_val, max_val = 1, 100
        guess = randint(min_val, max_val)

    game_section = f"""
        <h2 class='mt-3'>Is it {guess}?</h2>
        <form method='post'>
            <input type='hidden' name='min' value='{min_val}'>
            <input type='hidden' name='max' value='{max_val}'>
            <input type='hidden' name='guess' value='{guess}'>
            <button type='submit' name='too_small' class='btn-warning'>Too small</button>
            <button type='submit' name='too_big' class='btn btn-danger'>Too big</button>
            <button type='submit' name='correct' class='btn btn-success'>You win</button>
        </form>
    """
    return html_template.format(message_section="", game_section=game_section)

if __name__ == "__main__":
    app.run(debug=True)