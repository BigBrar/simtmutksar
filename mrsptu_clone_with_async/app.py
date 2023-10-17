from flask import Flask, request, redirect, render_template, url_for, session
from itsdangerous import URLSafeTimedSerializer
from datetime import timedelta
import send_input
import asyncio
from send_input_httpx import call_async
import get_another_marksheet

app = Flask(__name__)
app.secret_key = 'dW@G*YmrDat'
app.permanent_session_lifetime = timedelta(minutes=10)

serializer = URLSafeTimedSerializer('dw@G*YmrDat')

def generate_token(user_id,password,student_details,result_page,result_16,result_15):
    print("Writing data")
    data = {'id':user_id,'password':password,'student_details':student_details,'result_page':result_page,'result_16':result_16,'result_15':result_15}
    print("Wrote_data")
    return serializer.dumps(data)

def decode_token(token):
    try:
        data = serializer.loads(token,max_age=600)
        return data
    except:
        return None


@app.route('/',methods=['POST','GET'])
async def main_page():
    if request.method == 'POST':
        try:
            id = request.form['id']
            password = request.form['password']
            print("calling function")
            try:
                response = await call_async(id,password)
            except:
                return render_template('error.html')
            if response:
                # print("Response - ",response)
                session['token'] = generate_token(id,password,response[0],response[1],response[2],response[3])
                print('writing done ')
                session.permanent = True
                return redirect('/')
            else:
                return render_template('error.html')
        except Exception as e:
            # return "Either the credentials are incorrect or not filled properly!!!"
            return e

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
        student_details = token_data['student_details']
        print(student_details)
        # object = send_input.mrsptu_details(id,password)
        # student_details = object.get_student_profile()
        if student_details:
            return render_template('details.html',first_name=student_details[1],last_name=student_details[2],roll_no=student_details[0],DOB=student_details[3],father_name=student_details[4],mother_name=student_details[5],address=student_details[6],email=student_details[7],mobile=student_details[8],HOD=student_details[9].split('(')[1].split(')')[0],profile_picture=student_details[10])
        return render_template('error.html')
    else:
        return 'something went wrong !!!!'
    # re    urn "You are not supposed to be here "

@app.route('/marksheet',methods=['GET','POST'])
def marksheet_redirecter():
    print(type(request.form.get('marksheet')))
    print(f"Number - {request.form.get('marksheet')}")

    if 'marksheet' in request.form:
        if 'token' in session:
            token_data = decode_token(session['token'])
            # if token_data:
            result_16 = token_data['result_16']
            result_15 = token_data['result_15']
            if request.form.get('marksheet') == '16':
                result_16 = list(result_16)
                print('Type of the first result -   ',type(result_16))
                print(result_16)
                return render_template('show_result.html',marksheet=result_16[0],percentage=result_16[1])
            elif request.form.get('marksheet') == '15':
                result_15 = list(result_15)
                return render_template('show_result.html',marksheet=result_15[0],percentage=result_15[1])
            # html_code = get_another_marksheet.get_mark(id,password,request.form.get('marksheet'))
            else:
                return render_template('error.html')

    token_data = decode_token(session['token'])
    html_table = token_data['result_page']
    return render_template('show_result.html',marksheet=html_table)

@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
