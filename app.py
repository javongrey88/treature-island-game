from flask import Flask, render_template, request

app = Flask(__name__)

# ---- CHOICE ROUTES (each returns its own image name) ----

@app.route('/')
@app.route('/choice1')
def choice1():
    # Pass 'choice1.jpg' to the template as choice_image
    return render_template('choice1.html', choice_image='choice1.jpg')

@app.route('/choice2')
def choice2():
    # Pass 'choice2.jpg' to the template as choice_image
    return render_template('choice2.html', choice_image='choice2.jpg')

@app.route('/choice3')
def choice3():
    # Pass 'choice3.jpg' to the template as choice_image
    return render_template('choice3.html', choice_image='choice3.jpg')


# ---- GAME OVER ROUTE (maps each failure reason to its image) ----

@app.route('/game_over')
def game_over():
    """
    Show Game Over page with a large "Game Over" heading,
    an image depicting the defeat, and a reason text.
    Expects a query parameter 'reason', e.g.: /game_over?reason=hole
    """
    reason = request.args.get('reason', default='unknown').lower()

    # Map each failure reason to its corresponding image filename
    image_map = {
        'hole':   'hole_defeat.jpg',
        'trout':  'trout_defeat.jpg',
        'fire':   'fire_defeat.jpg',
        'beasts': 'beasts_defeat.jpg'
    }

    # Lookup defeat_image from the map (or None if not found)
    defeat_image = image_map.get(reason)

    return render_template(
        'game_over.html',
        reason=reason,
        defeat_image=defeat_image
    )


# ---- YOU WIN ROUTE (always shows treasure_chest.jpg) ----

@app.route('/you_win')
def you_win():
    treasure_image = 'treasure_chest.jpg'
    return render_template('you_win.html', treasure_image=treasure_image)


if __name__ == '__main__':
    app.run(debug=True)
