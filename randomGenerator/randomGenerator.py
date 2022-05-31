import time
from telethon.sync import TelegramClient
from telethon import functions, types
import random

listCoin = ["BTC","ETH","BCH","XRP","EOS","LTC","TRX","ETC","LINK","XLM","ADA","XMR","DASH","ZEC","XTZ","BNB","ATOM","ONT","IOTA","BAT","VET","NEO","QTUM","IOST","THETA","ALGO","ZIL","KNC","ZRX","COMP","OMG","DOGE","SXP","KAVA","BAND","RLC","WAVES","MKR","SNX","DOT","DEFI","YFI","BAL","CRV","TRB","YFII","RUNE","SUSHI","SRM","BZRX","EGLD","SOL","ICX","STORJ","BLZ","UNI","AVAX","FTM","HNT","ENJ","FLM","TOMO","REN","KSM","NEAR","AAVE","FIL","RSR","LRC","MATIC","OCEAN","CVC","BEL","CTK","AXS","ALPHA","ZEN","SKL","GRT","1INCH","AKRO","CHZ","SAND","ANKR","LUNA","BTS","LIT","UNFI","DODO","REEF","RVN","SFP","XEM","COTI","CHR","MANA","ALICE","BTC","ETH","HBAR","ONE","LINA","STMX","DENT","CELR","HOT"]
coin = random.choice(listCoin)

listSide = ["L", "S"]
side = random.choice(listSide)

listGroup = ["high", "low"]
listHighStakesLeverage = ["8","9","10"]
listLowStakesLeverage = ["5","6","7"]
groupSelect = random.choice(listGroup)

if (groupSelect == "high"):
    leverage = random.choice(listHighStakesLeverage)
    str = coin+" "+side+" "+leverage
    with TelegramClient('name',12816134, "3d6a556a840789d09ec6753b5cd7b7c7") as client:
        client.parse_mode = 'html'
        result = client(functions.messages.SendMessageRequest(
            peer='highrollertrader',
            message='🔥 NEW SIGNAL IS BEING DROPPED IN 3 MINS! 🔥 \n\n Get ready premium members ✅ \n\n Message @highrollertraders now to enroll in premium before it is too late',
            no_webpage=True
        ))
    time.sleep(180)
    with TelegramClient('name',12816134, "3d6a556a840789d09ec6753b5cd7b7c7") as client:
        client.parse_mode = 'html'
        result = client(functions.messages.SendMessageRequest(
            peer='highstakes21',
            message=str,
            no_webpage=True
        ))
else:
    leverage = random.choice(listLowStakesLeverage)
    str = coin+" "+side+" "+leverage
    with TelegramClient('name',12816134, "3d6a556a840789d09ec6753b5cd7b7c7") as client:
        client.parse_mode = 'html'
        result = client(functions.messages.SendMessageRequest(
            peer='highrollertrader',
            message='🔥 NEW SIGNAL IS BEING DROPPED IN 3 MINS! 🔥 \n\n Get ready premium members ✅ \n\n Message @highrollertraders now to enroll in premium before it is too late',
            no_webpage=True
        ))
    time.sleep(180)
    with TelegramClient('name',12816134, "3d6a556a840789d09ec6753b5cd7b7c7") as client:
        client.parse_mode = 'html'
        result = client(functions.messages.SendMessageRequest(
            peer='lowstakes',
            message=str,
            no_webpage=True
        ))