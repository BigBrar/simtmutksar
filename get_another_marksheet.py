import requests
from bs4 import BeautifulSoup

def get_mark(username,password,value):
    print(f"Parameters \n Username - {username}\nPassword - {password}\nValue - {value}")
    data = {'__EVENTTARGET':'ctl00$ContentPlaceHolder1$ctrlFacultyLogin1$lnkLogin',
            '__EVENTARGUMENT':'',
            '__VIEWSTATE':'/wEPDwUKMjExNzkwMDY2MA9kFgJmD2QWAgIDD2QWAmYPZBYGZg9kFgICBQ9kFgQCAQ8PZBYCHgpvbktleVByZXNzBWpqYXZhc2NyaXB0OmlmIChldmVudC5rZXlDb2RlID09IDEzKSBfX2RvUG9zdEJhY2soJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RyU3R1ZGVudExvZ2luMSRsbmtMb2dpbicsJycpZAIFDw9kFgIfAAVqamF2YXNjcmlwdDppZiAoZXZlbnQua2V5Q29kZSA9PSAxMykgX19kb1Bvc3RCYWNrKCdjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGN0clN0dWRlbnRMb2dpbjEkbG5rTG9naW4nLCcnKWQCAQ8PFgIeBFRleHQFciwgMTEwLjIyNC43Ni4yMTggLS1TU1NTU1MtLSAsIDExMC4yMjQuNzYuMjE4IC0tWlpaWlpaWlotLSAsIDo6MSwgMTAzLjcuNjQuMjMxLCAxMDMuNy42NC42NCAtLVRUVFRULS0gLCAxMDMuNy42NC42NGRkAgIPZBYGAgUPDxYCHgdWaXNpYmxlaGRkAgcPD2QWAh8ABWtqYXZhc2NyaXB0OmlmIChldmVudC5rZXlDb2RlID09IDEzKSBfX2RvUG9zdEJhY2soJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RybEZhY3VsdHlMb2dpbjEkbG5rTG9naW4nLCcnKWQCCw8PZBYCHwAFa2phdmFzY3JpcHQ6aWYgKGV2ZW50LmtleUNvZGUgPT0gMTMpIF9fZG9Qb3N0QmFjaygnY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRjdHJsRmFjdWx0eUxvZ2luMSRsbmtMb2dpbicsJycpZGSh4X7eM8lun3hi7T+DbVwQIotsfA==',
            '__VIEWSTATEGENERATOR':'8D0E13E6',
            '__EVENTVALIDATION':'/wEWBAK4j5aDCgLrs5HbAwKr6dWMAwLDl4uCCWaDuU5qw5W4DXcE1uymeDcU60mR',
            'ctl00$ContentPlaceHolder1$ctrlFacultyLogin1$txtUserID':username,
            'ctl00$ContentPlaceHolder1$ctrlStudentResult1$ddlExamSession': '16',
            'ctl00$ContentPlaceHolder1$ctrlFacultyLogin1$txtPassword':password}
            
#creating and sending the first request for login
    session = requests.Session()
    print("Sent the request !!!")
    response = session.post('https://www.mrsstuexam.com/Home.aspx?ReturnUrl=%2fStudent%2fviewResult.aspx',data=data)
    
    #extracting the eventvalidation and viewstate from the first login session request...
    soup = BeautifulSoup(response.content,'html.parser')
    event_validation = str(soup.find('input',{'id':'__EVENTVALIDATION'})).split('value="')[1].split('"')[0]
    viewstate = str(soup.find('input',{'id':'__VIEWSTATE'})).split('value="')[1].split('"')[0]
    print(f'Event Validation - check!!!')
    print(f'View State - check!!!')
    
    data2 = {'__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ctrlStudentResult1$ddlExamSession',
            '__EVENTARGUMENT':'', 
            '__LASTFOCUS':'',
            '__VIEWSTATE': viewstate,
            '__VIEWSTATEGENERATOR': '44D45452',
            '__EVENTVALIDATION': event_validation,
            'ctl00$ContentPlaceHolder1$ctrlStudentResult1$ddlExamSession': value}


    response2=session.post('https://www.mrsstuexam.com/Student/viewResult.aspx',data=data2)
    print("Got the response ..")
    soup = BeautifulSoup(response2.content,'html.parser')
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
