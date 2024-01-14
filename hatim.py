

print('\t\t\t\t\t\tHatim Hesaplama Uygulamasına Hoş Geldiniz.')

#Kullanıcının hangi hatimi hesaplamak istediğini seçmesi için bir menü
Menü = input('\t\t\t\t\t\t Lütfen Yapmak İstediğiniz Hatimi Seçiniz : '

  "\n\t1. Ayetülkürsi Hatmi : \n\t"
    "2. Enbiya Hatmi : \n\t"
      "3. Çarşamba,Perşembe Hatmi : \n\t"
        "4. Salati Münciye Hatmi : \n\t"
        '5. İhlas Hatmi : \n\t'
        '6. Salati Nariye Hatmi : \n\t'
        '7. Yasin-i Şerif Hatmi : \n\t')


#AyetülKürsi hatmini hesaplamak için gerekli olan kod bloğu
if Menü == "1" :
 
 KisiAdet  = int(input("\tLütfen Kişi Sayısı Giriniz : "))
 
 #Okunması gereken sayı 
 Ayetülkürsi = 313
 
 Adet = Ayetülkürsi % KisiAdet
 
 adet = Ayetülkürsi // KisiAdet  
 
 if KisiAdet == 313 : 

  print (KisiAdet-Adet,"KİŞİ",adet)
  
 else:
   
   print (Adet,"KİŞİ",Ayetülkürsi//KisiAdet+1)

   print (KisiAdet-Adet,"KİŞİ",adet)



#Enbiya hatmini hesaplamak için gerekli olan kod bloğu
elif Menü == "2" :
 
 KisiAdet = int(input("\tLütfen Kişi Sayısını Giriniz : "))
 
 #Okunması gereken sayı 
 EnbiyaHatmi = 500
 
 Adet = EnbiyaHatmi % KisiAdet
 
 adet = EnbiyaHatmi//KisiAdet
 
 if KisiAdet == 500 : 
    
    print (KisiAdet-Adet,"KİŞİ",adet)

 else:
   
   print (Adet,"KİŞİ",EnbiyaHatmi//KisiAdet+1)

   print (KisiAdet-Adet,"KİŞİ",adet)




#Çarşamba ve Perşembe hatmini hesaplamak için gerekli olan kod bloğu
elif Menü == "3":
  
  KisiAdet = int(input("\tLütfen Kişi Sayısını Giriniz : "))
  
  #Okunması gereken sayı 
  ÇarşambaPerşembeHatmi=100
  
  Adet = ÇarşambaPerşembeHatmi%KisiAdet
  
  adet = ÇarşambaPerşembeHatmi//KisiAdet
  

  if KisiAdet == 100 : 

    print (KisiAdet-Adet,"KİŞİ",adet)

  else:
   
   print (Adet,"KİŞİ",ÇarşambaPerşembeHatmi//KisiAdet+1)

   print (KisiAdet-Adet,"KİŞİ",adet)


  


#Salati Münciye hatmini hesaplamak için gerekli olan kod bloğu
elif Menü == "4" :
  
  KisiAdet = int(input("\tLütfen Kişi Sayısnı Giriniz : "))
  
  #Okunması gereken sayı 
  SalatiMünciye = 1000
  
  Adet = SalatiMünciye % KisiAdet
  
  adet = SalatiMünciye // KisiAdet
    
  if KisiAdet == 1000 : 

    print (KisiAdet-Adet,"KİŞİ",adet)

  else:
   
   print (Adet,"KİŞİ",SalatiMünciye//KisiAdet+1)

   print (KisiAdet-Adet,"KİŞİ",adet)




#İhlas hatmini hesaplamak için gerekli olan kod bloğu
elif Menü == '5' :

  KisiAdet = int(input("\tLütfen Kişi Sayısı Giriniz : "))
 
 #Okunması gereken sayı 
  ihlas = 1000

  Adet = ihlas % KisiAdet
  
  adet = ihlas // KisiAdet

  if KisiAdet == 1000 : 

    print (KisiAdet-Adet,"KİŞİ",adet)

  else:
   
   print (Adet,"KİŞİ",ihlas//KisiAdet+1)

   print (KisiAdet-Adet,"KİŞİ",adet)




#Salati Nariye hatmini hesaplamak için gerekli olan kod bloğu
elif Menü == '6' :

  KisiAdet = int(input("\tLütfen Kişi Sayısı Giriniz : "))
 
 #Okunması gereken sayı 
  Nariye = 4444

  Adet = Nariye % KisiAdet
  
  adet = Nariye // KisiAdet

  if KisiAdet == 4444 : 

    print (KisiAdet-Adet,"KİŞİ",adet)

  else:
   
   print (Adet,"KİŞİ",Nariye//KisiAdet+1)

   print (KisiAdet-Adet,"KİŞİ",adet)




#Yasin-i Şerif hatmini hesaplamak için gerekli olan kod bloğu
elif Menü == '7' :

  KisiAdet = int(input("\tLütfen Kişi Sayısı Giriniz : "))
 
 #Okunması gereken sayı 
  Yasin = 41

  Adet = Yasin % KisiAdet
  
  adet = Yasin // KisiAdet

  if KisiAdet == 41 : 

    print (KisiAdet-Adet,"KİŞİ",adet)

  else:
   
   print (Adet,"KİŞİ",Yasin//KisiAdet+1)

   print (KisiAdet-Adet,"KİŞİ",adet)

print("🕋 ALLAH KABUL ETSİN 🕋")




















































































