import os #os modülü programa eklendi
import subprocess #subprocess modülü programa eklendi
#from domaintools import API
import time #time modülü programa eklendi
import json #json modülü programa eklendi
import dns.resolver #dns.resolver modülü programa eklendi
import dns.reversename #dns.reversename modülü programa eklendi
import nmap #nmap modülü programa eklendi


d4 = input("arguman gir ...") #kullanıcıdan taramak istediği hedefi girmesini istedik

# robots.txt dosyasi 200 -->OK
def robotbul(): #robotbul metodumuzu oluşturduk.
print ("ROBOTS.TXT dosyasi bulunuyor---------") #programın çıktıları daha rahat okunsun diye ekledik.
result = os.popen("curl https://"+d4+"/robots.txt").read() #sistemde bulunan "curl" aracı programa eklendi. Bununla birlikte curl ile hedef verdiğimiz sitenin "robotx.txt" dosyasının içerisind bulunan satırları çekmeye başlıyoruz.
result_data_set = {"Disallowed":[], "Allowed":[]} # "robots.txt" içerisinde bulunan "Disallowed" ve "Allowed" isimli kısımların her ikisinide bir argümana atıyoruz ve bunları bir "dizi" olarak tanımlıyoruz
print ("robots txt bulundu----------")
print ("-----------------------------------")

for line in result.split("\n"): #bulunan sonucu sonuç sayısı kadar bölüyoruz
	if line.startswith('Allow'):    # eğer satır başlangıcı "izinli" kısım ila başlıyor ise;
	result_data_set["Allowed"].append(line.split(': ')[1].split(' ')[0])     #belirtilen argümana(result_data_set) "Allowed" olarak eklemeye başla
	elif line.startswith('Disallow'):    #Eğer satır başlangıcı "izinsiz" kelimesi ile başlıyorsa;
result_data_set["Disallowed"].append(line.split(': ')[1].split(' ')[0])      #belirtilen argümana(result_data_set) "Disallowed" olarak eklemeye başla

print (result_data_set) #sonucu ekrana yazdır
print ("GERCEK ROBOTLAR BULUNDU")
print ("------------------------")
robotbul() #metodu çağırdık
time.sleep(7) #sonuçlara göz atabilmek için kısa süreliğine programı durdurduk.
time.sleep(7)















def dnsrecon(): #dnsrecon adında bir metod oluşturduk.
print ("dnsreceon basliyor") #Programın calısma bilgisini kullanıcıya verdik
print ("------------------")
time.sleep(3) #Kısa bir süre calısmasına olanak vermek için programı "3 saniye" beklettik
dnsistek = "-d" #dnsrecon aracında tarama parametresi "-d" olarak kullanılır. Program çalışma sürecinde bir hata çıkmasını engellemek için tanımlanmıştır.
sonuc = subprocess.call(['dnsreceon', dnsistek+d4]) #sistemde bulunan "dnsrecon" aracını programa çağırdık ve gerekli argüman ile birlikte "d4" ifademiz ile hedefi gösterdik
print ("dns recon taramasi tamamlandi...") #Progamın bitimini kullanıcıya verdik
print ("---------------------------------")
print (sonuc) #sonucu ekrana yazdırdık.
dnsrecon() #metodu çağırdık. 
time.sleep(4) #sonuçlara göz atabilmemiz için kısa bir süreliğine programı durdurduk.







# traceroute OK -->200
def traceroute(): #traceroute adında bir metod oluşturduk
print("tracerouter basliyor...") #Aracın çalışmaya başlayacağının bilgisini kullanıcıya verdik
time.sleep(2) #Sonucları rahat bir şekilde görebilmemiz için programı "2 saniye" durdurduk.
tracetarama = subprocess.call("traceroute "+d4).read() #Sistemde hazır olan "traceroute" isimli aracı programımızda çalışması için çağırdık.
#traceroute()
print ("traceroute bitti") #aracın çalışmasını bitirdiğinin bilgisini kullanıcıya verdik
print ("-----------------")
time.sleep(5)#Sonucları rahat bir şekilde görebilmemiz için programı "2 saniye" durdurduk.



