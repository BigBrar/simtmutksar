from bs4 import BeautifulSoup


def extract_table(response):
    soup = BeautifulSoup(response.content,'html.parser')
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
    return [str(student_details),mark_percentage]
