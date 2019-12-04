
# giriste soracaksin. Aktif bilgi toplamak mi istersin pasif bilgi toplamak mi cocuk adam diye?
# ona gore de gidis yolu cizeceksin aktif icin:9 pasif icin:5 daha sonrasinda listeleyerek devam edeceksin
#Bu first kızım olup kod "200" olanlar belirtilmistir
import os
import subprocess
#from domaintools import API
import time
import json
import dns.resolver
import dns.reversename
import nmap
import whois
import socket

d4 = input("arguman gir ...")
data={"robots.txt path":[],"a_records":[],"traceroute":[],"whois":[],"geo_lookup":[],"nmap_sonuc":[]}



# robots.txt dosyasi 200 -->OK
def robotbul():
        print ("ROBOTS.TXT dosyasi bulunuyor---------")
        result = os.popen("curl https://"+d4+"/robots.txt").read() #bu kisimla ben oynadum
        #   print "BASLIYOR\n"+result
        result2=result.split("\n")
        
        for i in result2:
                if i.startswith("Allow:"):
                        i=i.split(":")[1]
                        data["robots.txt path"].append({
                "Status": "Allowed",
                "Path":i
                })
                elif i.startswith("Disallow:"):
                        i=i.split(":")[1]
                        data["robots.txt path"].append({
               "Status": "Disallowed",
               "Path":i
                })

        
#robotbul()




# Reverse IP Lookup bebegim 200 --> OK
def tersine_moah():
    os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d4 )
    os.system("clear")    
    print("HTML dosyasi indirildi!!!")
    reverse_data = os.popen("curl http://api.hackertarget.com/reverseiplookup/?q="+d4).read()
    result=reverse_data.split("\n")
    for i in result:
        data["a_records"].append({
            "Reverse IP Result":i
        })

    print ("Reverse IP islemi bitti")
    print ("-------------------------------------------------------")
#tersine_moah()
#time.sleep(3)


###############################################################################################
# dirhunt hata verdigi icin atlandi
###############################################################################################




###############################################################################################
# dnsreon hata verdigi icin atlandi
###############################################################################################

# traceroute OK -->200
def traceroute():
    print("tracerouter basliyor...")
    time.sleep(2)
    tracetarama = os.popen("traceroute "+d4).read()
    
    print("\n\ntracetaramaaaaaa\n\n"+str(tracetarama))
    tracetarama=tracetarama.split("\n")
    kontrol=0
    for i in tracetarama:
        if kontrol==0:
                kontrol=1
        else:
                data["traceroute"].append({
                        "Gateway IP":i
                })

#traceroute()
print ("traceroute bitti")
print ("-----------------")
#time.sleep(2)


#timeour hatası veriyor düzeltilmedi




###############################################################################################
#whois sorgusunda, json formatini hatali veriyor, cok ugrastim ama yapamadim :(( 
###############################################################################################
#Whois sorgusu OK -->200
def whois_sorgusu():
    
    print ("whois sorgusu basliyor..")
    time.sleep(1)
    sorgu_sonuc=whois.whois(d4)
    sorgu_sonuc=str(whois.whois(d4))
    data["whois"].append(sorgu_sonuc)
    
#whois_sorgusu()
print ("whois sorgusu bitti...")
print ("----------------------")
#time.sleep(3)


#geolookup OK -->200
def geolookup():
    print ("geolookup basliyor")
    print ("-------------------")
    geo_sonuc=os.popen("curl http://api.hackertarget.com/geoip/?q=" + d4 ).read()
    geo_sonuc=geo_sonuc.split("\n")
    
    for i in geo_sonuc:
        v1=i.split(":")[0]
        v2=i.split(":")[1]   

        data["geo_lookup"].append({
               v1:v2
        })
        
#geolookup()
print ("geolooup bitti...")
print ("------------------")
#time.sleep(2)



###############################################################################################
#dmitry komutu ne buradan, ne direk terminalden calisiyor. Kalide' de denedim calismiyor. Mert' de denedi calismiyor!!!!!!!
###############################################################################################
"""
#dmitry tarama OK -->200

def dmitry():
    print ('dmitry taramasi basliyor...')
    dmitry_arguman = ('-winse')
    dmitry_sonuc = os.popen("dmitry -winse "+d4).read()
    print(dmitry_sonuc)
    #subprocess.call(['dmitry',dmitry_arguman,' ',d4])

dmitry()
print ("dmitry taramasi bitti...")
print ("------------------------")
time.sleep(2)
"""




#nmap tarama OK --> 200
def nmap_tarama():
    print ("nmap taramasi basliyor...")
    nm = nmap.PortScanner()
    nm.scan(hosts=d4, ports='21,22,23,25,53,67,68,80,143,443', arguments='-sS -sV -Pn -O')
    #nm.scan(d4,'21,22,23,25,53,67,68,80,143,443','-sS -sV -Pn -O')
    nm.scaninfo()
    nm.csv()
    print("\nsonucusuususucuuc\n\n")
    print(nm._scan_result)
    data["nmap_sonuc"].append(nm._scan_result)
    #print (nm.csv())

#nmap_tarama()
print ("nmap taramasi bitti...")
print ("-----------------------")





with open('data.json','w') as outfile:
        json.dump(data,outfile)


print("\ndata.json dosyasi olusturuldu")
