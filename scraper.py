import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.pwcs.edu/leadership/school_board/index")

soup = BeautifulSoup(req.content, "html.parser")

# print(soup.prettify())
# print(soup.get_text())
res = soup.table

# print(res.get_text())

with open('data_pwcs.csv', 'w') as file:
    file.write(res.get_text())

req = requests.get("https://alveyes.pwcs.edu/directory/staff_email_list")

soup = BeautifulSoup(req.content, "html.parser")
res = soup.table
with open('data_alveyes.csv', 'w') as file:
    file.write(res.get_text())

