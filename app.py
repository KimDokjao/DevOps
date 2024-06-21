from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Conversion factors
conversion_factors = {
    'meters': 1,
    'kilometers': 0.001,
    'centimeters': 100,
    'millimeters': 1000,
    'miles': 0.000621371,
    'yards': 1.09361,
    'feet': 3.28084,
    'inches': 39.3701
}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']

            if from_unit not in conversion_factors or \
                    to_unit not in conversion_factors:
                return render_template('index.html',
                                       error="Invalid unit entered.")

            result = (value * conversion_factors[to_unit] /
                      conversion_factors[from_unit])
            return render_template('index.html', result=result)
        except ValueError:
            return render_template('index.html', error="Invalid input.")
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    try:
        value = float(data['value'])
        from_unit = data['from_unit']
        to_unit = data['to_unit']

        if from_unit not in conversion_factors or \
                to_unit not in conversion_factors:
            return jsonify({'error': 'Invalid unit entered.'}), 400

        result = (value * conversion_factors[to_unit] /
                  conversion_factors[from_unit])
        return jsonify({'result': result}), 200

    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input.'}), 400


if __name__ == '__main__':
    app.run(debug=True)
