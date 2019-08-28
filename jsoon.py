
# giriste soracaksin. Aktif bilgi toplamak mi istersin pasif bilgi toplamak mi cocuk adam diye?
# ona gore de gidis yolu cizeceksin aktif icin:9 pasif icin:5 daha sonrasinda listeleyerek devam edeceksin
import os
import subprocess
#from domaintools import API
import time
import json
import dns.resolver
import dns.reversename
import nmap


d4 = input("arguman gir ...")

# robots.txt dosyasi 200 -->OK
def robotbul():
    print ("ROBOTS.TXT dosyasi bulunuyor---------")
    result = os.popen("curl https://"+d4+"/robots.txt").read() #bu kisimla ben oynadum
    result_data_set = {"Disallowed":[], "Allowed":[]}
    print ("robots txt bulundu----------")
    print ("-----------------------------------")

    for line in result.split("\n"):
        if line.startswith('Allow'):    # this is for allowed url
            result_data_set["Allowed"].append(line.split(': ')[1].split(' ')[0])    
        elif line.startswith('Disallow'):    # this is for disallowed url
            result_data_set["Disallowed"].append(line.split(': ')[1].split(' ')[0])    

    print (result_data_set)
    print ("GERCEK ROBOTLAR BULUNDU")
    print ("------------------------")
# robotbul()
# time.sleep(7)



# api = Shodan('4uXvxzSWh9vOTKrv7jEb0Qt1EA8mwVrx')
# # Search for websites that have been "hacked"
# host_ismi = raw_input("host bilgisi girin...")
# for banner in api.search_cursor('hostname:'+host_ismi):
#     print(banner)


# SHODAN_API_KEY = "4uXvxzSWh9vOTKrv7jEb0Qt1EA8mwVrx"
# api = shodan.Shodan(SHODAN_API_KEY)
# host_ismi = raw_input("host bilgisi girin...")
# host = api.host(host_ismi)

# # Print general info
# print("""
#         IP: {}
#         Organization: {}
#         Operating System: {}
# """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

# # Print all banners
# for item in host['data']:
#         print("""
#                 Port: {}
#                 Banner: {}
#         """.format(item['port'], item['data']))



# Reverse IP Lookup bebegim 200 --> OK
def tersine_moah():
    # d3 = raw_input("enter IP adress...")
    os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d4 )
    os.system("clear")
    os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d4 )
    print("")
    print ("Reverse IP islemi bitti")
    print ("-------------------------------------------------------")
    # print("\033[91m\033[1mFile Saved On : ")
    # os.system("pwd")
    # print("File : index.html?q=" +d3)
    # print("\033[0m")
    # reverse_IP_jsoon = {
    #     "Taratilan_Host_Adi" : d4,
    #     "Reverse_Ciktisi" :  os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d4 ),
    #     "diger_ciktisi" : os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d4 )
    # }
    # with open("hadibakim.txt", "w") as dosyacik2:
    #     json.dump(reverse_IP_jsoon,dosyacik2)
tersine_moah()
time.sleep(7)



# #dirhunt calisiyor bebeim 200 -->OK
def dirhunt():
    print ("dirhunt taramasi basliyor..")
    print ("--------------------------------------")
    # girdi = raw_input("domain gir ayi...")
# dirhunt()
# time.sleep(7)

#     dirhunt_cikti_jsoon = {
#     "Girilen_Host_Adi" : d4,
#     "Robots_Dosyalari" : cikis
#     }
#     with open ('hadibakim.txt', 'w') as dosyacik:
#         json.dump(dirhunt_cikti_jsoon, dosyacik)

# dirhunt()
# print "dirhunt taramasi bitti"
# print "----------------------"
# time.sleep(7)



# #dnsrecon calisiyor 200 -->OK
def dnsrecon():
    print ("dnsreceon basliyor")
    print ("------------------")
    time.sleep(3)
    dnsistek = "-d"
    sonuc = subprocess.call(['dnsrecon',dnsistek+d4])
    print ("dns recon taramasi tamamlandi...")
    print ("---------------------------------")
    print (sonuc)
dnsrecon()
time.sleep(4)


# traceroute OK -->200
def traceroute():
    print ("tracerouter basliyor...")
    time.sleep(2)
    tracetarama = subprocess.call(["traceroute", d4])
    print (tracetarama)
# traceroute()
print ("traceroute bitti")
print ("-----------------")
time.sleep(5)


#Whois sorgusu OK -->200
def whois_sorgusu():
    print ("whois sorgusu basliyor..")
    time.sleep(2)
    whoistarama = subprocess.call(["whois", d4])
    print (whoistarama)
whois_sorgusu()
print ("whois sorgusu bitti...")
print ("----------------------")
time.sleep(7)




#dnsenum Eklendi OK -->200
def dnsenum():
        arg = "--enum"
        dnstarama = subprocess.call(['dnsenum',arg,d4])
        print (dnstarama)
dnsenum()

#geolookup OK -->200
def geolookup():
    print ("geolookup basliyor")
    print ("-------------------")
    os.system("curl http://api.hackertarget.com/geoip/?q=" + d4 )
    print ("")
geolookup()
print ("geolooup bitti...")
print ("------------------")
time.sleep(5)


#dmitry tarama OK -->200
# def dmitry():
#     print ("dmitry taramasi basliyor...")
#     dmitry_arguman = '-winse'
#     subprocess.call(['dmitry',dmitry_arguman,d4])
# dmitry()
# print ("dmitry taramasi bitti...")
# print ("------------------------")
# time.sleep(5)


#nmap tarama OK --> 200
# def nmap_tarama():
#     print ("nmap taramasi basliyor...")
#     nm = nmap.PortScanner()
#     nm.scan()
#     nm.scan(d4,'21,22,67,68,80,143,443','-sS -sV -Pn')
#     nm.scaninfo()
#     nm.csv()
#     print (nm.csv())
# nmap_tarama()
# print ("nmap taramasi bitti...")
# print ("-----------------------")
# time.sleep(5)


#DIRB istek OK -->200
def dirb_istek():
    print ("dirb taramasi basliyor....")
    sertifika = "https://"
    subprocess.call(["dirb",sertifika+d4])

