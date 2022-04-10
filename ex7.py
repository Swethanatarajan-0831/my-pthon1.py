import requests
from bs4 import BeautifulSoup
import pandas
import connect
import ex7(2)
url="https://www.careerindia.com/colleges/colleges-in-chennai/"
parser.add_argument("--dbname",help="Enter the number of pages to parse",type=int)

info=[]

connect.connect(args.dbname)
for page in range(1,4):
    request_ = requests.get(url)
    content=request_.content
    soup=BeautifulSoup(content,"html.parser")
    
    colleges=soup.find_all("div",{"class":"edu-detlist-container"})

    for college in colleges:
        college_dictionary={}
        college_dictionary["name"]=college.find("h2",{"class":"edu-det-heading"}).text
        college_dictionary["address"]=college.find("div",{"class":"edu-det-subhead"}).text
        try:
            college_dictionary["contact"]=college.find("div",{"class":"edu-det-lable"}).text
        except AttributeError:
                pass
        info.append(college_dictionary)
        connect.inserting(agrs.dbname,college_dictionary.values())
dataframe=pandas.DataFrame(info)
dataframe.to_csv("college.csv")
connect.information(args.dbname)
