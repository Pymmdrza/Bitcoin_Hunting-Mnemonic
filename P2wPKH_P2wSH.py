from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import BitcoinMainnet as Cryptocurrency
from hdwallet.utils import generate_mnemonic, is_mnemonic
from lxml import html
import requests
from mnemonic import Mnemonic
import random
from colorama import Fore, Style

from threading import *


def xBal(addr):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def xBal2(addr2):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr2
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


x = 128
y = 256

z = 0
while True:
    listen = [x, y]
    rnds = random.choice(listen)
    STRENGTH: int = rnds
    langlist = ["english", "french", "italian", "spanish"]
    rndlang = random.choice(langlist)
    LANGUAGE: str = rndlang
    
    MNEMONIC: str = generate_mnemonic(language=LANGUAGE, strength=STRENGTH)
    PASSPHRASE: str = "meherett"
    assert is_mnemonic(mnemonic=MNEMONIC, language=LANGUAGE)
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=Cryptocurrency, account=0, change=False, address=0)
    bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE)
    addr = bip44_hdwallet.p2wpkh_address()
    addr2 = bip44_hdwallet.p2wsh_address()
    priv = bip44_hdwallet.private_key()
    xpriv = bip44_hdwallet.xprivate_key()
    xrootpriv = bip44_hdwallet.root_xprivate_key()
    bal = xBal(addr)
    bal2 = xBal2(addr2)
    print(str(z) + ' ' + Fore.RED + str(addr) + ' ' + Fore.YELLOW + str(bal))
    z += 1
    print(Fore.WHITE + str(z) + ' ' + Fore.YELLOW + str(addr2) + ' ' + Fore.RED + str(bal2))
    print(str(MNEMONIC)[:84])
    z += 1
    
    if int(bal) > 0 or int(bal2) > 0:
        print("=====================[Winner Wallet Details Saved On Text File]=====================")
        print("------------------------[ Programmer Mmdrza.Com ]-----------------------------")
        f = open("BTCDetails__Single___WalletWin.txt", "a")
        f.write("\nAddress =====> " + str(addr) + " TotalTX => " + str(bal))
        f.write("\nAddress =====> " + str(addr2) + " TotalTX => " + str(bal2))
        f.write("\nPrivate Key ======> " + str(priv))
        f.write("\nxPub =============> " + str(xpriv))
        f.write("\nRootPrivate ======> " + str(xrootpriv))
        f.write("\n\n================> PROGRAMMING WiTH MMDRZA.CoM <==================\n")
        f.close()
        
        t1 = Thread(target=xBal2, args=[])
        t2 = Thread(target=xBal, args=[])
        t1.start()
        t2.start()
        t1.join()
        t2.join()


