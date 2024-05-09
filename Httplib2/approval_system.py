"""
coded by : Tanim hossain
"""
import os,time
import uuid
try:import httplib2
except ModuleNotFoundError:os.system('pip install httplib2')
import httplib2
os.system('clear')
logo = f"""
{50*'-'}
 @written_by : Tanim hossain
 @github     : Txt-Xd
{50*'-'}"""
class Approval:
    def __init__(self):
        self.uuid = str(os.geteuid())
        self.key = "".join(self.uuid)
        try:
            self.http = httplib2.Http()
            self.url = "#####"# your approval server link 
            self.response = self.http.request(self.url, 'GET')
        except httplib2.error.ServerNotFoundError:exit(' internet error!')
        self.line= 50*'-'
        self.apv()
    def send(self):
        print(f" sending approval request to a server");time.sleep(2)
        print(f" approval request sent successfully");time.sleep(2)
        os.system('clear')
        print(logo)
    def apv(self):
        try:
            os.system('clear')
            print(logo)
            self.send()
            if self.key in str(self.response):
                print(f" approval successful")
            else:
                print(f" your key not approved\n key : {self.key}\n{self.line}")
        except Exception as e:exit(' error!')
Approval()
