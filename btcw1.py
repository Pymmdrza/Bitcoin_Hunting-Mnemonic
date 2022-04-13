from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import BitcoinMainnet as Cryptocurrency
from hdwallet.utils import generate_mnemonic, is_mnemonic
from lxml import html
import requests
from mnemonic import Mnemonic
import random
from colorama import Fore, Style
from multiprocessing import Process


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

def xBal3(addr3):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr3
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def xBal4(addr4):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr4
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def xBal5(addr5):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr5
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def xBal6(addr6):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr6
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
b = 0
while z <= 1000:
    listen = [x,y]
    rnds = random.choice(listen)
    STRENGTH: int = rnds
    langlist = ["english","french","italian","spanish"]
    rndlang = random.choice(langlist)
    LANGUAGE: str = rndlang
    
    MNEMONIC: str = generate_mnemonic(language=LANGUAGE, strength=STRENGTH)
    PASSPHRASE: str = "meherett"
    assert is_mnemonic(mnemonic=MNEMONIC, language=LANGUAGE)
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=Cryptocurrency, account=0, change=False, address=0)
    bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE)
    addr = bip44_hdwallet.p2pkh_address()
    addr2 = bip44_hdwallet.p2sh_address()
    addr3 = bip44_hdwallet.p2wpkh_address()
    addr4 = bip44_hdwallet.p2wsh_address()
    addr5 = bip44_hdwallet.p2wpkh_in_p2sh_address()
    addr6 = bip44_hdwallet.p2wsh_in_p2sh_address()
    priv = bip44_hdwallet.private_key()
    xpriv = bip44_hdwallet.xprivate_key()
    xrootpriv = bip44_hdwallet.root_xprivate_key()
    bal = xBal(addr)
    bal2 = xBal2(addr2)
    bal3 = xBal3(addr3)
    bal4 = xBal4(addr4)
    bal5 = xBal5(addr5)
    bal6 = xBal6(addr6)
    print(Fore.RED + '[ Scan Number : ' + str(z) + '      Reaming: ' + str(b) + ' ]' + Style.RESET_ALL)
    print(Fore.RED + '[*]' + Fore.YELLOW + ' P2PKH: ' + str(addr) +    Fore.MAGENTA + ' >> ' + Fore.WHITE + ' Tx: ' + Fore.GREEN + str(bal))
    print(Fore.RED + '[*]' + Fore.YELLOW + ' P2SH: ' + str(addr2) +    Fore.MAGENTA + ' >> ' + Fore.WHITE + ' Tx: ' + Fore.GREEN + str(bal2))
    print(Fore.RED + '[*]' + Fore.YELLOW + ' P2wPKH: ' + str(addr3) +  Fore.MAGENTA + ' >> ' + Fore.WHITE + ' Tx: ' + Fore.GREEN + str(bal3))
    print(Fore.RED + '[*]' + Fore.YELLOW + ' P2wsh: ' + str(addr4) +   Fore.MAGENTA + ' >> ' + Fore.WHITE + ' Tx: ' + Fore.GREEN + str(bal4))
    print(Fore.RED + '[*]' + Fore.YELLOW + ' iP2wPKH: ' + str(addr5) + Fore.MAGENTA + ' >> ' + Fore.WHITE + ' Tx: ' + Fore.GREEN + str(bal5))
    print(Fore.RED + '[*]' + Fore.YELLOW + ' iP2wSH: ' + str(addr6) +  Fore.MAGENTA + ' >> ' + Fore.WHITE + ' Tx: ' + Fore.GREEN + str(bal6))
    print(Fore.RED + "[*]" + Fore.YELLOW + " Private Key" + Fore.WHITE + " ====> " + Fore.RED + str(priv))
    print(Fore.RED + "[*]" + Fore.YELLOW + " Mnemonicx64" + Fore.WHITE + " ====> " + Fore.RED + str(MNEMONIC)[:64]  + "..." + Fore.BLUE + "  (LANGUAGE: " + str(rndlang) + " )")
    print(Fore.MAGENTA + "------------------------>"+ Fore.BLUE + "[ MMDRZA.CoM ]" + Fore.MAGENTA + "<----------------------")
    print(Fore.WHITE + "------->> Donate For Programmer ("+Fore.RED+"BTC address:"+Fore.CYAN+" 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8"+Fore.WHITE+") <<-------")
    z += 1
    b += 6
    if int(bal) > 0 or int(bal2) > 0 or int(bal3) > 0 or int(bal4) > 0 or int(bal5) > 0 or int(bal6) > 0:
        print("=====================[Winner Wallet Details Saved On Text File]=====================")
        print("------------------------[ Programmer Mmdrza.Com ]-----------------------------")
        f = open("BTCDetails_____WalletWin.txt", "a")
        f.write("\n Address =====> " + str(addr)  + " TotalTX => " + str(bal))
        f.write("\n Address =====> " + str(addr2) + " TotalTX => " + str(bal2))
        f.write("\n Address =====> " + str(addr3) + " TotalTX => " + str(bal3))
        f.write("\n Address =====> " + str(addr4) + " TotalTX => " + str(bal4))
        f.write("\n Address =====> " + str(addr5) + " TotalTX => " + str(bal5))
        f.write("\n Address =====> " + str(addr6) + " TotalTX => " + str(bal6))
        f.write("\nPrivate Key ======> " + str(priv))
        f.write("\nxPub =============> " + str(xpriv))
        f.write("\nRootPrivate ======> " + str(xrootpriv))
        f.write("\n\n================> PROGRAMMING WiTH MMDRZA.CoM <==================\n")
        f.close()
        
        continue
        
if __name__ == '__main__':
    p1: Process = Process(target=xBal, args=("p1",))
    p2: Process = Process(target=xBal2, args=("p2",))
    p3: Process = Process(target=xBal3, args=("p3",))
    p4: Process = Process(target=xBal4, args=("p4",))
    p5: Process = Process(target=xBal5, args=("p5",))
    p6: Process = Process(target=xBal6, args=("p6",))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()