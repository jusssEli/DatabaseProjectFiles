from flask import Flask,render_template, request, redirect, url_for
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'eroger25'
app.config['MYSQL_PASSWORD'] = 'Rangoisntacolor12!'
app.config['MYSQL_DB'] = 'Eli'
 
mysql = MySQL(app)
 
@app.route('/form')

def form():
    return render_template('form.html')
 
@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == 'GET':
        return "Fill out the Search Form"

    if request.method == 'POST':
        name = request.form['name']
        emp_id = request.form['emp_id']
        cursor = mysql.connection.cursor()
        if name:
            cursor.execute("SELECT * from employee where name = %s",[name])
        if emp_id:
            cursor.execute("SELECT * from employee where emp_id = %s",[emp_id])
        mysql.connection.commit()
        data = cursor.fetchall()
        cursor.close()
        print(data)
        #return f"Done!! Query Result is {data}"
        return render_template('results.html', data=data)

@app.route('/meetings')
def meetings():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM meeting")
    meeting_data = cursor.fetchall()
    cursor.close()
    return render_template('meetings.html', meetings=meeting_data)

@app.route('/remove_meeting/<int:meeting_id>', methods=['POST'])
def remove_meeting(meeting_id):
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM meeting WHERE meeting_id = %s", [meeting_id])
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('meetings'))

@app.route('/listing')
def listing():
    cursor = mysql.connection.cursor()
    # Execute a query to fetch data
    cursor.execute("SELECT * FROM employee")
    # Fetch all rows from the result set
    mysql.connection.commit()
    data = cursor.fetchall()
    cursor.close()
    print(data)
    #return f"Done!! Query Result is {data}"
    return render_template('listing.html', data=data)
app.run(host='localhost', port=5000)
