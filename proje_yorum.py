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
def robotbul(): #robotbul metodumuzu olusturduk.
print ("ROBOTS.TXT dosyasi bulunuyor---------") 
result = os.popen("curl https://"+d4+"/robots.txt").read() 
result_data_set = {"Disallowed":[], "Allowed":[]} 
print ("robots txt bulundu----------")
print ("-----------------------------------")

for line in result.split("\n"): #bulunan sonucu sonuc sayısı kadar boluyoruz
	if line.startswith('Allow'):   
	result_data_set["Allowed"].append(line.split(': ')[1].split(' ')[0])  
	elif line.startswith('Disallow'):    
result_data_set["Disallowed"].append(line.split(': ')[1].split(' ')[0])     

print (result_data_set) 
print ("GERCEK ROBOTLAR BULUNDU")
print ("------------------------")
robotbul() 
time.sleep(7)


def dnsrecon(): 
print ("dnsreceon basliyor") #Programın calısma bilgisini kullanıcıya verdik
print ("------------------")
time.sleep(3) 
dnsistek = "-d" #dnsrecon aracında tarama parametresi "-d" olarak kullanılır. Program calisma sürecinde bir hata cikmasini engellemek için tanımlanmıştır.
sonuc = subprocess.call(['dnsreceon', dnsistek+d4]) 
print ("dns recon taramasi tamamlandi...") 
print ("---------------------------------")
print (sonuc) #sonucu ekrana yazdırdık.
dnsrecon()
time.sleep(4) 


# traceroute OK -->200
def traceroute(): #traceroute adında bir metod oluşturduk
print("tracerouter basliyor...") 
time.sleep(2) 
tracetarama = subprocess.call("traceroute "+d4).read() 
#traceroute()
print ("traceroute bitti") 
print ("-----------------")
time.sleep(5)



