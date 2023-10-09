from flask import Flask, request, redirect, render_template, url_for, session
from itsdangerous import URLSafeTimedSerializer
from datetime import timedelta
import send_input
import get_another_marksheet

app = Flask(__name__)
app.secret_key = 'dw@G*YmrDat'
app.permanent_session_lifetime = timedelta(minutes=10)

serializer = URLSafeTimedSerializer('dw@G*YmrDat')

def generate_token(user_id,password):
    data = {'id':user_id,'password':password}
    return serializer.dumps(data)

def decode_token(token):
    try:
        data = serializer.loads(token,max_age=600)
        return data
    except:
        return None


@app.route('/',methods=['POST','GET'])
def main_page():
    if request.method == 'POST':
        try:
            id = request.form['id']
            password = request.form['password']
            session['token'] = generate_token(id,password) 
            session.permanent = True
            return redirect('/')
        except:
            return "Either the credentials are incorrect or not filled properly!!!"

    elif 'token' in session:
            token_data = decode_token(session['token'])
            id = token_data['id']
            password = token_data['password']
            print(f'Username and password are {id}, {password}')
            # return redirect('/details')
            return render_template('home_page.html',id=id)
    return render_template('index.html')

@app.route('/details',methods=['GET','POST'])
def student_details():
    if 'token' in session:
        token_data = decode_token(session['token'])
        # if token_data:
        id = token_data['id']
        password = token_data['password']
        object = send_input.mrsptu_details(id,password)
        student_details = object.get_student_profile()
        if student_details:
            return render_template('details.html',first_name=student_details[1],last_name=student_details[2],roll_no=student_details[0],DOB=student_details[3],father_name=student_details[4],mother_name=student_details[5],address=student_details[6],email=student_details[7],mobile=student_details[8],HOD=student_details[9].split('(')[1].split(')')[0],profile_picture=student_details[10])
        return render_template('error.html')
    else:
        return 'something went wrong !!!!'
    # re    urn "You are not supposed to be here "

@app.route('/marksheet',methods=['GET','POST'])
def marksheet_redirecter():
    id = ''
    password = ''
    print(type(request.form.get('marsheet')))
    print(f"Number - {request.form.get('marksheet')}")

    if 'marksheet' in request.form:
        if 'token' in session:
            token_data = decode_token(session['token'])
            # if token_data:
            id = token_data['id']
            password = token_data['password']
            html_code = get_another_marksheet.get_mark(id,password,request.form.get('marksheet'))
            return render_template('show_result.html',marksheet=html_code[0],percentage=html_code[1])
    
    object = send_input.mrsptu_details(id,password)
    html_table = object.get_marks_table()
    return render_template('show_result.html',marksheet=html_table[0],percentage=html_table[1])

@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
