from flask import Flask, request, redirect, render_template
import send_input

id = ''
password = ''

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/details',methods=['GET','POST'])
def student_details():
    global id
    global password
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        object = send_input.mrsptu_details(id,password)
        student_details = object.get_student_profile()
        print(student_details)
        return render_template('details.html',first_name=student_details[1],last_name=student_details[2],roll_no=student_details[0],DOB=student_details[3],father_name=student_details[4],mother_name=student_details[5],address=student_details[6],email=student_details[7],mobile=student_details[8],HOD=student_details[9].split('(')[1].split(')')[0],profile_picture=student_details[10])
    return "You are not supposed to be here "

@app.route('/marksheet',methods=['GET','POST'])
def marksheet_redirecter():
    global id
    global password
    print(id," v ",password)
    object = send_input.mrsptu_details(id,password)
    html_table = object.get_marks_table()
    return render_template('show_result.html',marksheet=html_table[0],percentage=html_table[1])

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
