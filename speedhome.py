import requests, os, json
from sys import stdout
from colorama import Fore, Style

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def dirdar():
    if not os.path.exists('Results'):
        os.mkdir('Results')

def banners():
    clear()
    stdout.write("                                                                                            \n")
    stdout.write(""+Fore.LIGHTRED_EX +"███████╗██████╗ ███████╗███████╗██████╗ ██╗  ██╗ ██████╗ ███╗   ███╗███████╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██║  ██║██╔═══██╗████╗ ████║██╔════╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"███████╗██████╔╝█████╗  █████╗  ██║  ██║███████║██║   ██║██╔████╔██║█████╗  \n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  \n")
    stdout.write(""+Fore.LIGHTRED_EX +"███████║██║     ███████╗███████╗██████╔╝██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝\n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦══════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"Description     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   AUTOMATED WEB SCRAPPING & CRAWLER                "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"Github     "+Fore.RED+"         |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/PARI-MALAM                            "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n\n")
banners()

LOCATION = input(f"{Fore.GREEN}Location: {Fore.WHITE}")
RENT = f"https://speedhome.com/_next/data/Pk0NVCwkVV2EcAxIys6O6/en/rent{LOCATION}"
BUY = f"https://speedhome.com/_next/data/Pk0NVCwkVV2EcAxIys6O6/en/buy/{LOCATION}"
OPTIONAL = f"https://speedhome.com/_next/data/Pk0NVCwkVV2EcAxIys6O6/en/rent/{LOCATION}.json?loc={LOCATION}"

def speed_home_rent():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Baggage": "sentry-environment=production,sentry-release=Pk0NVCwkVV2EcAxIys6O6,sentry-transaction=%2Frent,sentry-public_key=9b8b980ce5914b5ab63ce7607cb49df0,sentry-trace_id=071a828bf08c48e6bc8e12090ca3a668,sentry-sample_rate=0",
            "Referer": "https://speedhome.com/rent",
            "Purpose": "prefetch",
            "Sentry-Trace": "071a828bf08c48e6bc8e12090ca3a668-a6a1de051810667f-0",
            "X-Nextjs-Data": "1"
        }
        response = requests.get(RENT, headers=headers)
        if response.status_code == 200:
            data = response.json()

            output_file = f"{LOCATION}_rent_data.json"
            with open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)

            print(f"{Fore.GREEN}Data saved successfully to {output_file}")
        else:
            print(f"{Fore.RED}Something went wrong in APIs")
            print(response.text)
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")

def speed_home_buy():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Baggage": "sentry-environment=production,sentry-release=Pk0NVCwkVV2EcAxIys6O6,sentry-transaction=%2Frent,sentry-public_key=9b8b980ce5914b5ab63ce7607cb49df0,sentry-trace_id=071a828bf08c48e6bc8e12090ca3a668,sentry-sample_rate=0",
            "Referer": "https://speedhome.com/buy",
            "Purpose": "prefetch",
            "Sentry-Trace": "071a828bf08c48e6bc8e12090ca3a668-a6a1de051810667f-0",
            "X-Nextjs-Data": "1"
        }
        response = requests.get(BUY, headers=headers)
        if response.status_code == 200:
            data = response.json()

            output_file = f"{LOCATION}_buy_data.json"
            with open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)

            print(f"{Fore.GREEN}Data saved successfully to {output_file}")
        else:
            print(f"{Fore.RED}Something went wrong in APIs")
            print(response.text)
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")

if __name__ == "__main__":
    speed_home_rent()
    speed_home_buy()
