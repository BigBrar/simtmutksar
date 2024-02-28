from bs4 import BeautifulSoup as bs

class extractor:

    def get_student_profile(response):
            student_details =[]
            soup = bs(response.content,'html.parser')
            try:
                student_details.append(soup.find(id='ctl00_ContentPlaceHolder1_ctrlStudentProfile1_lblRollNumber').text)#roll no
                input_tag = soup.find(id='ctl00_ContentPlaceHolder1_ctrlStudentProfile1_txtFirstName')#first name
                student_details.append(input_tag['value'])
                input_tag = soup.find(id='ctl00_ContentPlaceHolder1_ctrlStudentProfile1_txtMiddleName')#middle name
                student_details.append(input_tag['value'])
                input_tag = soup.find('input',{'id':'ctl00_ContentPlaceHolder1_ctrlStudentProfile1_txtdob'})#DOB
                student_details.append(input_tag['value']) #DOB
                input_tag = soup.find(id='ctl00_ContentPlaceHolder1_ctrlStudentProfile1_txtFatherName')#Father's name
                student_details.append(input_tag['value'])
                input_tag = soup.find(id='ctl00_ContentPlaceHolder1_ctrlStudentProfile1_txtMotherName')#mother's name
                student_details.append(input_tag['value'])
                student_details.append(soup.find(id='ctl00_ContentPlaceHolder1_ctrlStudentProfile1_txtaddress').text)#address
                input_tag = soup.find(id='ctl00_ContentPlaceHolder1_ctrlStudentProfile1_txtEmailID')#email
                student_details.append(input_tag['value'])
                input_tag = soup.find(id='ctl00_ContentPlaceHolder1_ctrlStudentProfile1_txtMobileNo')#phone number
                student_details.append(input_tag['value'])
                student_details.append(soup.find(id='ctl00_ContentPlaceHolder1_ctrlStudentProfile1_lblProfileStatus').text)#name of HOD in a msg
                input_tag = soup.find(id='ctl00_ContentPlaceHolder1_ctrlStudentProfile1_imgProfilePicture')#profile picture !!!
                student_details.append('https://mrsstuexam.com'+str(input_tag['src']).split('..')[1])
                return student_details
            except:
                return False

    def get_marks_table(response):
        student_details = ''
        soup = bs(response.content,'html.parser')
        try:
            student_details = soup.find('table',{'id':'ctl00_ContentPlaceHolder1_ctrlStudentResult1_grdStudentResult'})#marksheet
            mark_percentage = 0
            print("Nothing happens")
            mark_percentage+=int(str(student_details).split('ctl00_ContentPlaceHolder1_ctrlStudentResult1_grdStudentResult_ctl02_lblExtMark')[1].split('>')[1].split('<')[0])
            mark_percentage+=int(str(student_details).split('ctl00_ContentPlaceHolder1_ctrlStudentResult1_grdStudentResult_ctl03_lblExtMark')[1].split('>')[1].split('<')[0])
            mark_percentage+=int(str(student_details).split('ctl00_ContentPlaceHolder1_ctrlStudentResult1_grdStudentResult_ctl04_lblExtMark')[1].split('>')[1].split('<')[0])
            mark_percentage+=int(str(student_details).split('ctl00_ContentPlaceHolder1_ctrlStudentResult1_grdStudentResult_ctl05_lblExtMark')[1].split('>')[1].split('<')[0])
            mark_percentage+=int(str(student_details).split('ctl00_ContentPlaceHolder1_ctrlStudentResult1_grdStudentResult_ctl06_lblExtMark')[1].split('>')[1].split('<')[0])
            mark_percentage/=300
            mark_percentage*=100
            return [student_details,mark_percentage]

        except:
            if soup.find('div',{'id':'ctl00_ContentPlaceHolder1_ctrlStudentResult1_pnlmessage'}):
                print(soup.find('div',{'id':'ctl00_ContentPlaceHolder1_ctrlStudentResult1_pnlmessage'}).text)
                return ['<h2>This marksheet is not yet available</h2>','not available']
            else:
                return ("error")
