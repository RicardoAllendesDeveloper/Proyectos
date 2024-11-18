from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    result = None
    if request.method == 'POST':
        try:
            # Recoge las notas y la asistencia del formulario
            note1 = float(request.form['note1'])
            note2 = float(request.form['note2'])
            note3 = float(request.form['note3'])
            attendance = float(request.form['attendance'])

            # Calcula el promedio
            average = (note1 + note2 + note3) / 3

            # Determina el estado
            if average >= 40 and attendance >= 75:
                status = "Aprobado"
            else:
                status = "Reprobado"

            result = {
                'average': round(average, 2),
                'attendance': attendance,
                'status': status
            }
        except ValueError:
            result = "Error: Ingrese valores numéricos válidos."

    return render_template('ejercicio1.html', result=result)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    result = None
    if request.method == 'POST':
        # Recoge los nombres del formulario
        names = [
            request.form['name1'],
            request.form['name2'],
            request.form['name3']
        ]
        # Encuentra el nombre más largo
        longest_name = max(names, key=len)
        result = {
            'longest_name': longest_name,
            'length': len(longest_name)
        }

    return render_template('ejercicio2.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
