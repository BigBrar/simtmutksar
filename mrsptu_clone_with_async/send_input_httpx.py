import httpx
import time
import asyncio
import html_data_extractor
from bs4 import BeautifulSoup
from marksheet_table_extractor import extract_table


async def fetch(username,password):
    print("its running")
    data = {'__EVENTTARGET':'ctl00$ContentPlaceHolder1$ctrlFacultyLogin1$lnkLogin',
                '__EVENTARGUMENT':'',
                '__VIEWSTATE':'/wEPDwUKMjExNzkwMDY2MA9kFgJmD2QWAgIDD2QWAmYPZBYGZg9kFgICBQ9kFgQCAQ8PZBYCHgpvbktleVByZXNzBWpqYXZhc2NyaXB0OmlmIChldmVudC5rZXlDb2RlID09IDEzKSBfX2RvUG9zdEJhY2soJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RyU3R1ZGVudExvZ2luMSRsbmtMb2dpbicsJycpZAIFDw9kFgIfAAVqamF2YXNjcmlwdDppZiAoZXZlbnQua2V5Q29kZSA9PSAxMykgX19kb1Bvc3RCYWNrKCdjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGN0clN0dWRlbnRMb2dpbjEkbG5rTG9naW4nLCcnKWQCAQ8PFgIeBFRleHQFciwgMTE3LjIxNC4yMjkuMTUgLS1TU1NTU1MtLSAsIDExNy4yMTQuMjI5LjE1IC0tWlpaWlpaWlotLSAsIDo6MSwgMTAzLjcuNjQuMjMxLCAxMDMuNy42NC42NCAtLVRUVFRULS0gLCAxMDMuNy42NC42NGRkAgIPZBYGAgUPDxYCHgdWaXNpYmxlaGRkAgcPD2QWAh8ABWtqYXZhc2NyaXB0OmlmIChldmVudC5rZXlDb2RlID09IDEzKSBfX2RvUG9zdEJhY2soJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RybEZhY3VsdHlMb2dpbjEkbG5rTG9naW4nLCcnKWQCCw8PZBYCHwAFa2phdmFzY3JpcHQ6aWYgKGV2ZW50LmtleUNvZGUgPT0gMTMpIF9fZG9Qb3N0QmFjaygnY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRjdHJsRmFjdWx0eUxvZ2luMSRsbmtMb2dpbicsJycpZGRCOaWAw62ieT149F/AwH+/Y2NjYA==',
                '__VIEWSTATEGENERATOR':'8D0E13E6',
                '__EVENTVALIDATION':'/wEWBAK28cTJDgLrs5HbAwKr6dWMAwLDl4uCCSvm3yi5Qp7yjohnDX9C1/Phh20t',
                'ctl00$ContentPlaceHolder1$ctrlFacultyLogin1$txtUserID':username,
                'ctl00$ContentPlaceHolder1$ctrlFacultyLogin1$txtPassword':password}


    url = ['https://www.mrsstuexam.com/Home.aspx?ReturnUrl=%2fStudent%2fDefault.aspx',
            'https://www.mrsstuexam.com/Student/Profile.aspx',
            'https://www.mrsstuexam.com/Student/viewResult.aspx']
    async with httpx.AsyncClient() as client:

        #starting the timer...
        start = time.perf_counter()

        #logging in with the credentials
        login_response = await client.post(url[0],data=data)
        print("Login response - ",login_response)

        #extracting the cookies from the login
        session_cookie = login_response.cookies.get("ASP.NET_SessionId")
        gzs_cookie = login_response.cookies.get('gzs')

        #sending the get request for the pages with the assigned cookeis
        profile_details = await client.get(url[1],cookies={"ASP.NET_SessionId": session_cookie, "gzs": gzs_cookie})
        result_page = await client.get(url[2],cookies={"ASP.NET_SessionId": session_cookie, "gzs": gzs_cookie})

        #extracting parameters from the result_page
        soup = BeautifulSoup(result_page.content,'html.parser')
        event_validation = str(soup.find('input',{'id':'__EVENTVALIDATION'})).split('value="')[1].split('"')[0]
        viewstate = str(soup.find('input',{'id':'__VIEWSTATE'})).split('value="')[1].split('"')[0]

        #send the request to get other pages

        #getting may result
        result_16 = await client.post(url[2],data={'__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ctrlStudentResult1$ddlExamSession','__EVENTARGUMENT':'','__LASTFOCUS':'','__VIEWSTATE': viewstate,'__VIEWSTATEGENERATOR': '44D45452','__EVENTVALIDATION': event_validation,'ctl00$ContentPlaceHolder1$ctrlStudentResult1$ddlExamSession': 16},cookies={"ASP.NET_SessionId": session_cookie, "gzs": gzs_cookie})
        table_16 = extract_table(result_16)
        # with open('index.html','w')as file:
            # file.write(result_16.text)

        #getting dec 2022 result
        # print(data2)
        result_15 = await client.post(url[2],data={'__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ctrlStudentResult1$ddlExamSession','__EVENTARGUMENT':'','__LASTFOCUS':'','__VIEWSTATE': viewstate,'__VIEWSTATEGENERATOR': '44D45452','__EVENTVALIDATION': event_validation,'ctl00$ContentPlaceHolder1$ctrlStudentResult1$ddlExamSession': 15},cookies={"ASP.NET_SessionId": session_cookie, "gzs": gzs_cookie})
        table_15 = extract_table(result_15)
        # with open('index.html','w')as file:
            # file.write(str(table_15[0]))

        end = time.perf_counter()#timer ends here
        student_details = html_data_extractor.extractor.get_student_profile(profile_details)
        # reqs.append( client.get(url[1]))
        # reqs.append( client.get(url[2]))
        # reqs.append( client.post(url[1],data=data))
        # results = await asyncio.gather(*reqs)
        print("Results for the async module are - ",profile_details.headers)
        print(f"\nExtracted student details are - {student_details}")
        print(f"Completed in - {start-end}")
        # with open('index.html','w')as file:
            # file.write(result_page.text)
        return [student_details,str(result_page),table_16,table_15]
    # return True
        # with open('index.html','w') as file:
        #     file.write(profile_details.text)

async def call_async(username,password):
    response = await fetch(username,password)
    return response

# asyncio.run(fetch('220540673','SIMT212/'))
