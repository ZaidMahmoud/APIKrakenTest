#imported libraries
import requests
import datetime

# collecting parameters inserted by  the user with a message of the options
print('Please have a look at the supported currencies https://support.kraken.com/hc/en-us/articles/227876608-Margin-trading-pairs-and-their-maximum-leverage')

curr1=input("Enter first currency, please ex. ADA; XXBT: ")
curr2=input("Enter second currency, please ex. XETH; ZUSD: ")

pair=input("Enter pair, please ex. ADAETH; XBTUSD: ")
#asset=input("Enter asset, please ex. ADA,ETH; XBT,USD: ")

rescur=input("Enter what element in result, please ex. ADAETH; XXBTZUSD: ")

def get_asset(pair):
    f=pair[:3]
    s=pair[3:]
    asset=f+","+s
    return(asset)


# URLs
baseurl1='https://api.kraken.com/0/public/Trades'
baseurl2='https://api.kraken.com/0/public/Assets'

#Sets of parameters
params1={'pair':pair, 'count':100}
params2={'asset':get_asset(pair), 'aclass':'currency'}

# Getting requests in JSON
resp1 = requests.get(baseurl1,params1)
r1 = resp1.json()
resp2 = requests.get(baseurl2,params2)
r2 = resp2.json()

# if condition of handling errors for the trades request. for loop iterates through the elements of the Trades
if resp1.status_code == 200:
    for item in r1['result'][rescur]:
        print (item[0]+ " USD")
        print(item[1] + " USD")
        print(item[2] )
        print(item[3] )
        print(item[4] )
        print(item[5])
        print(item[6])
        print("End of the transaction")
        print("*********")
else:
    print(f"Error: {resp1.status_code}")

# if condition of handling errors for the assets request. for loop iterates through the elements of the Assets
if resp2.status_code == 200:
    print (r2['result'][curr1])
    print("*******")
    print(r2['result'][curr2])
    print("*******")
else:
    print(f"Error: {resp2.status_code}")



# function lstmntunix() to return last minute in unix to use it as a parameter for since
# Kraken unix How to retrieve historical time and sales https://support.kraken.com/hc/en-us/articles/218198197-How-to-retrieve-historical-time-and-sales-trading-history-using-the-REST-API-Trades-endpoint-
def lstmntunix():
    lstmintdate = datetime.datetime.now() - datetime.timedelta(minutes=1)
    unixclstmint = datetime.datetime.timestamp(lstmintdate) * 1000000000
    return (unixclstmint)
    lstmntunix()

# Ask about the desire of the user to get the last minute trades
OptionLstMnt=input("Do you want the get the last minute trades Y/N:")
if OptionLstMnt in ('Y','y','Yes','yes'):
    params3 = {'pair': pair, 'since': lstmntunix()}
    resp3 = requests.get(baseurl1, params3)
    r3 = resp3.json()
    if resp3.status_code == 200:
        for item in r3['result'][rescur]:
            print(item[0] + " USD")
            print(item[1] + " USD")
            print(item[2])
            print(item[3])
            print(item[4])
            print(item[5])
            print(item[6])
            print("End of the transaction")
            print("*********")
    else:
        print(f"Error: {resp3.status_code}")
else:
    print("Thanks for your answer")
