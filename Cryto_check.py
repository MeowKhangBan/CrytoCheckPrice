from colorama import Fore,init,Style
import pandas
from tabulate import tabulate
from bs4 import BeautifulSoup
import requests
from datetime import datetime

init(autoreset=True) #If you didn't do this your terminal maybe change to other color too.

def main(name = '',do_csv = ''): #We need do_csv because we have to get 2 data, 1 for show in terminal and 1 for write to csv.
    url = f'https://coinmarketcap.com/th/currencies/{name.strip()}/'
    callweb = requests.get(url)  
    web_status = callweb.status_code
    if web_status == 200:
        data = BeautifulSoup(callweb.text,'html.parser')
        price_data = data.find('div',{'class':'priceValue'})
        cryto_data = data.find('span',{'class':'sc-1eb5slv-0 sc-1308828-0 bwAAhr'})
        status_data = data.find('span',{'class':'sc-15yy2pl-0 feeyND'})
        if status_data == None: #status up and down of cryto is not a same class 
            status_data = data.find('span',{'class':'sc-15yy2pl-0 kAXKAX'})
        price = price_data.text
        cryto = cryto_data.text.strip()
        if do_csv == 'no': #This if logic is important because we can't adding color for any text and symbol in csv.
            if 'icon-Caret-down' in str(status_data):
                status = (Fore.LIGHTRED_EX + f'↓{status_data.text}'+ Style.RESET_ALL)
                #In colorama library we have Fore to add color for text. 
                #And we have to put Style.RESET_ALL , if you don't do this. 
                #Everything after that text you just add color will have same color like you text
            else:
                status = (Fore.LIGHTGREEN_EX + f'↑{status_data.text}'+ Style.RESET_ALL)
            return cryto,price,status
        if do_csv == 'yes':
            if 'icon-Caret-down' in str(status_data):
                status = ( f'↓{status_data.text}')
            else:
                status = (f'↑{status_data.text}')
            return cryto,price,status #return value to function 

    elif web_status == 404:
        return '404 not found'
    else:
        return False

#You see 'cryto_eth,price_eth,status_eth = main('ethereum','no')'
#But computer see "cryto_eth , price_eth , status_eth = cryto , price , status (from return)
#And then cryto_eth = cryto  price_eth = price  status_eth = status

cryto_eth,price_eth,status_eth = main('ethereum','no')
cryto_btc,price_btc,status_btc = main('bitcoin','no')
cryto_usdt,price_usdt,status_usdt = main('tether','no')
cryto_bnb,price_bnb,status_bnb = main('bnb','no')
cryto_usdc,price_usdc,status_usdc = main('usd-coin','no')
cryto_xrp,price_xrp,status_xrp = main('xrp','no')
cryto_sol,price_sol,status_sol = main('solana','no')
cryto_ada,price_ada,status_ada = main('cardano','no')
cryto_luna,price_luna,status_luna = main('terra-luna','no')
cryto_doge,price_doge,status_doge = main('dogecoin','no')


data = [[1,cryto_eth,price_eth,status_eth],[2,cryto_btc,price_btc,status_btc] 
,[3,cryto_usdt,price_usdt,status_usdt],[4,cryto_bnb,price_bnb,status_bnb],
[5,cryto_usdc,price_usdc,status_usdc],[6,cryto_xrp,price_xrp,status_xrp],
[7,cryto_sol,price_sol,status_sol],[8,cryto_ada,price_ada,status_ada],
[9,cryto_luna,price_luna,status_luna],[10,cryto_doge,price_doge,status_doge]]

print(tabulate(data,headers=['No.','Coin','Price(THB)','Status'])) #Tabulate is a library to create table
print('-'*35)

#After we print data in terminal . we will reset variable for write a csv.
#Because csv is a pure data format so it doesn't allow to adding color.

cryto_eth,price_eth,status_eth = main('ethereum','yes')
cryto_btc,price_btc,status_btc = main('bitcoin','yes')
cryto_usdt,price_usdt,status_usdt = main('tether','yes')
cryto_bnb,price_bnb,status_bnb = main('bnb','yes')
cryto_usdc,price_usdc,status_usdc = main('usd-coin','yes')
cryto_xrp,price_xrp,status_xrp = main('xrp','yes')
cryto_sol,price_sol,status_sol = main('solana','yes')
cryto_ada,price_ada,status_ada = main('cardano','yes')
cryto_luna,price_luna,status_luna = main('terra-luna','yes')
cryto_doge,price_doge,status_doge = main('dogecoin','yes')

data2 = [[cryto_eth,price_eth,status_eth],[cryto_btc,price_btc,status_btc] 
,[cryto_usdt,price_usdt,status_usdt],[cryto_bnb,price_bnb,status_bnb],
[cryto_usdc,price_usdc,status_usdc],[cryto_xrp,price_xrp,status_xrp],
[cryto_sol,price_sol,status_sol],[cryto_ada,price_ada,status_ada],
[cryto_luna,price_luna,status_luna],[cryto_doge,price_doge,status_doge]]

Order_number = [] #Number of cryto.
for i in range(1,11):
    Order_number.append(f'No.{i}') #I'm lazy to write No.1-10 with myself

headers=['Coin','Price(THB)','Status'] 

table = pandas.DataFrame(data2,Order_number,headers) #Pandas is a library to create table 
date = datetime.now().strftime('%Y-%m-%d')
table.to_csv(f'Coin_data_{date}.csv',index=False) #Change pandas to csv 
