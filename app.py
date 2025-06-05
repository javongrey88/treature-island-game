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

@app.route('/game_over')
def game_over():
    reason = request.args.get('reason', default='unknown')
    return render_template('game_over.html', reason=reason)

@app.route('/you_win')
def you_win():
    # If you generate an image named 'treasure_chest.png', put it in static/images/.
    treasure_image = 'treasure_chest.png'
    return render_template('you_win.html', treasure_image=treasure_image)

if __name__ == '__main__':
    app.run(debug=True)
