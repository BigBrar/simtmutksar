import requests
from bs4 import BeautifulSoup as bs
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache

class mrsptu_details:

    def __init__(self, username, password):
        self.marks_url = 'https://www.mrsstuexam.com/Home.aspx?ReturnUrl=%2fStudent%2fviewResult.aspx'
        self.headers = {'Accept-Encoding': 'gzip'}
        self.session = CacheControl(requests.Session(), cache=FileCache('.web_cache'))
        self.username = username
        self.password = password
        self.data = {'__EVENTTARGET':'ctl00$ContentPlaceHolder1$ctrlFacultyLogin1$lnkLogin',
                    '__EVENTARGUMENT':'',
                    '__VIEWSTATE':'/wEPDwUKMjExNzkwMDY2MA9kFgJmD2QWAgIDD2QWAmYPZBYGZg9kFgICBQ9kFgQCAQ8PZBYCHgpvbktleVByZXNzBWpqYXZhc2NyaXB0OmlmIChldmVudC5rZXlDb2RlID09IDEzKSBfX2RvUG9zdEJhY2soJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RyU3R1ZGVudExvZ2luMSRsbmtMb2dpbicsJycpZAIFDw9kFgIfAAVqamF2YXNjcmlwdDppZiAoZXZlbnQua2V5Q29kZSA9PSAxMykgX19kb1Bvc3RCYWNrKCdjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGN0clN0dWRlbnRMb2dpbjEkbG5rTG9naW4nLCcnKWQCAQ8PFgIeBFRleHQFciwgMTE3LjIxNC4yMjkuMTUgLS1TU1NTU1MtLSAsIDExNy4yMTQuMjI5LjE1IC0tWlpaWlpaWlotLSAsIDo6MSwgMTAzLjcuNjQuMjMxLCAxMDMuNy42NC42NCAtLVRUVFRULS0gLCAxMDMuNy42NC42NGRkAgIPZBYGAgUPDxYCHgdWaXNpYmxlaGRkAgcPD2QWAh8ABWtqYXZhc2NyaXB0OmlmIChldmVudC5rZXlDb2RlID09IDEzKSBfX2RvUG9zdEJhY2soJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RybEZhY3VsdHlMb2dpbjEkbG5rTG9naW4nLCcnKWQCCw8PZBYCHwAFa2phdmFzY3JpcHQ6aWYgKGV2ZW50LmtleUNvZGUgPT0gMTMpIF9fZG9Qb3N0QmFjaygnY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRjdHJsRmFjdWx0eUxvZ2luMSRsbmtMb2dpbicsJycpZGRCOaWAw62ieT149F/AwH+/Y2NjYA==',
                    '__VIEWSTATEGENERATOR':'8D0E13E6',
                    '__EVENTVALIDATION':'/wEWBAK28cTJDgLrs5HbAwKr6dWMAwLDl4uCCSvm3yi5Qp7yjohnDX9C1/Phh20t',
                    'ctl00$ContentPlaceHolder1$ctrlFacultyLogin1$txtUserID':self.username,
                    'ctl00$ContentPlaceHolder1$ctrlFacultyLogin1$txtPassword':self.password}
        self.profile_url = 'https://www.mrsstuexam.com/Home.aspx?ReturnUrl=%2fStudent%2fProfile.aspx'
        self.get_payment_history = 'https://www.mrsstuexam.com/Home.aspx?ReturnUrl=%2fStudent%2fFeeVerfiiedStatus.aspx'


    def get_marks_table(self):
        response = self.session.post(self.marks_url,data=self.data)
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
            return ['<h2>This marksheet is not yet available</h2>','not available']
        # student_details.append(soup.find('span',{'id':'ctl00_ContentPlaceHolder1_ctrlStudentResult1_lblStudent'}).text)#student name
        # student_details.append(soup.find('span',{'id':'ctl00_ContentPlaceHolder1_ctrlStudentResult1_lblRollNumber'}).text)#student's roll number
        # student_details.append(soup.find('span',{'id':'ctl00_ContentPlaceHolder1_ctrlStudentResult1_lblCollege'}).text)#student's college name
        # student_details.append(soup.fi/nd('span',{'id':'ctl00_ContentPlaceHolder1_ctrlStudentResult1_lblBranch'}).text)#student's college branch
        # student_details.append(soup.find('span',{'id':'ctl00_ContentPlaceHolder1_ctrlStudentResult1_lblBatch'}).text)#student's batch(year of admission)
        return [student_details,mark_percentage]

    def get_student_profile(self):
        response = self.session.post(self.profile_url,data=self.data)
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







# get_marks('220540683','SIMT212*')
