from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/choice1')
def choice1():
    return render_template('choice1.html')

@app.route('/choice2')
def choice2():
    return render_template('choice2.html')

@app.route('/choice3')
def choice3():
    return render_template('choice3.html')

# ---- Modified game_over route ----
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
        'hole':   'hole_defeat.png',
        'trout':  'trout_defeat.png',
        'fire':   'fire_defeat.png',
        'beasts': 'beasts_defeat.png'
    }

    # Look up the correct image, or None if the reason is unexpected
    defeat_image = image_map.get(reason)  # e.g. 'hole_defeat.png'

    return render_template(
        'game_over.html',
        reason=reason,
        defeat_image=defeat_image
    )

@app.route('/you_win')
def you_win():
    # Example: Always show treasure_chest.png when you win
    treasure_image = 'treasure_chest.png'
    return render_template('you_win.html', treasure_image=treasure_image)

if __name__ == '__main__':
    app.run(debug=True)
