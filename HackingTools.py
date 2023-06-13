import requests
import json
import colorama
from colorama import Fore, Style, init
init(autoreset=True)


print(f"""
Hacking Tools



{Fore.WHITE}[ {Fore.YELLOW}1 {Fore.WHITE}] {Fore.RESET}IP-Lookout      
""")

program = int(input(
    f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.RESET}Input the number of the program to run: "))


def iplookout():
    print(f"""
 _  ___       _    ___  ___  _ __ ___  _ _  ___ 
| || . \ ___ | |  | . || . || / /| . || | ||_ _|
| ||  _/|___|| |_ | | || | ||  \ | | || ' | | | 
|_||_|       |___|`___'`___'|_\_\`___'`___' |_| 
    """)

    ip = input(
        f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.RESET}IP-Adress: ")
    link = f"http://ip-api.com/json/{ip}?fields=17559551"

    try:
        response = requests.get(link)

    except:
        print(
            f"{Fore.WHITE}[ {Fore.YELLOW}! {Fore.WHITE}] {Fore.RESET}No connection.")

    if response.status_code == 200:
        data = json.loads(response.text)
        print(f"""
        country: {data['country']}
    countrycode: {data['countryCode']}
         region: {data['region']}
     regionName: {data['regionName']}
           city: {data['city']}
       district: {data['district']}
            zip: {data['zip']}
            lat: {data['lat']}
            lon: {data['lon']}
       timezone: {data['timezone']}
            isp: {data['isp']}
            org: {data['org']}
             as: {data['as']}
         mobile: {data['mobile']}
          proxy: {data['proxy']}
        hosting: {data['hosting']}
        """)
    else:
        print(
            f"{Fore.WHITE}[ {Fore.YELLOW}! {Fore.WHITE}] {Fore.RESET}Error: {response.status_code}.")


if program == 1:
    iplookout()

else:
    print(
        f"{Fore.WHITE}[ {Fore.YELLOW}! {Fore.WHITE}] {Fore.RESET}Somethiong went wrong.")
