from flask import Flask, request, jsonify
import generate_series
import pocker

app = Flask(__name__)


@app.route('/series')
def genSeries():
    n = int(request.args.get('n'))
    output = generate_series.Func(n)
    return str(output)


@app.route('/pocker', methods=['GET', 'POST'])
def genPoker():
    if request.method == 'GET':
        outStr = """
            <html>
                <head>
                    <title>poker</title>
                </head>
                <body>
                    <h1>How many players?</h1>
                    <form action="/pocker" method="post">
                        <input type="textbox" name="players">
                        <button type="submit">Submit</button>
                    </form>
                </body>
            </html>
            """
        return outStr
    elif request.method == 'POST':
        players = request.form.get('players')
        cards = pocker.poker(int(players))
        return jsonify(cards)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
