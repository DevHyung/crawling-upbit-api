import requests
import json

excelHeader = ['코인명','현재가','전일대비','거래대금']
def get_symbol_list():
    KRW_File = open("KRW_LIST.txt",'w')
    BTC_File = open("BTC_LIST.txt",'w')
    ETH_File = open("ETH_LIST.txt",'w')
    USDT_File = open("USDT_LIST.txt",'w')
    url = "https://api.upbit.com/v1/market/all"
    response = requests.request("GET", url)
    jsonStr = json.loads(response.text)
    for coin in jsonStr:
        print(coin['market'])
        if 'BTC-' in coin['market']:
            BTC_File.write(coin['market']+'\n')
        elif 'KRW-' in coin['market']:
            KRW_File.write(coin['market']+'\n')
        elif 'ETH-' in coin['market']:
            ETH_File.write(coin['market']+'\n')
        else:
            USDT_File.write(coin['market']+'\n')
    USDT_File.close()
    BTC_File.close()
    ETH_File.close()
    USDT_File.close()
def get_KRW_ticker():
    url = "https://api.upbit.com/v1/ticker"
    KRW_File = open("KRW_LIST.txt", 'r')
    lines = KRW_File.readlines()
    print(lines)
    for line in lines:
        querystring = {"markets": line.strip()}
        response = requests.request("GET", url, params=querystring)
        jsonStr = json.loads(response.text)
        print(line.strip(),jsonStr[0]['trade_price'],round(jsonStr[0]['acc_trade_price_24h']),round(jsonStr[0]['signed_change_rate']*100,2))
if __name__ == "__main__":
    #get_symbol_list()
    get_KRW_ticker()
