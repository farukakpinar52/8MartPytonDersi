#çıktı almak için kullanılan komut
print("Başlangıç için güzel bir gün.")

#string ifadeler için çift tırnak içi metinsel ifade
baslik = "ilk değişkenim"
print(baslik)
#baslik degiskenine ait degeri degistirdik
baslik = "ihtiyaç kredisi"
print(baslik)
#numeric değerler
numara = 1
print(numara)


#float double decimal
deger1=22.3
deger2=1.44
fark=deger1-deger2
print(fark)

#bool ifadeler büyük harfle başlar
artisVarMi=True
sabitMi = False

#matematiksel operatörler
print(5+12)
print(numara+144)
print(12-deger1)
print(10*deger2)
print(1/deger1)

#mantıksal operatörler
print((2-1)==1)
print(1!=2)

#toplu yorum satırı ctrl + K + C
#satırları ctrl  + K + U
# print("abc")
# print("abc")

# or ve and keywordleri

print(5<2 or 20>1)
print(5<2 and 20>1)
print("or and")
print(5<2 or 20>1 and 2>1)
print(5<2 and 20>1 or 2>1)
print(5<2 and 20>1 and 2>1)

#burada ilk 5<2 and 20>1 kısmının sonucu gelir
#daha sonra and durumu incelenir


#karar yapıları
#if else
# : -> indent yapısı
if 2>1:
    deger="if"
else :
    deger="else"
print(deger)


#float ve int değerleri birbirlerine dönüşebilir
#float int e dönüşürken küsüratını kaybeder
a=5
b=2.6

#a değerinifloat yapalım
c=float(a)
#b değerini integer yapalım
d=int(b)

print(c)
print(d)
print(type(c))
print(type(d))


#sayılardan oluşmuş string bir değer int ve float a dönüşebilir
x="23"
intx=int(x)
print(intx)
print(type(intx))

#paragraf bir metin oluşturmak için """ tırnek yada ''' kullanılır
a=""" selam
bugün burada ptyhon
öğreniyoruz"""
print(a)

#stringler dizi gibi de davranır
a="0123456789"
print(a[4])
print(a[2:6])

#String Fonksiyonlar
#Len(): Bir string dizinin uzunluğunu almak için, diğer popüler birçok dilde olduğu gibi len() fonksiyonu kullanılır.
print(len(a))
#Strip (): bir string değerin başındaki veya sonundaki tüm boşlukları kaldırır.
metin="   aaa   "
print(metin.strip())
metin2="AaBbCc"
#Lower() : String değeri küçük harfe çevirir.
print(metin2.lower())
#Upper() : String değeri BÜYÜK HARFLERE çevirir.
print(metin2.upper())
#Replace() : Bir string değerini başka bir string değeri ile değiştirir.
print(metin2.replace("Aa","Dd"))
#Split() : Bir string değeri belirtilen ayırıcıyı örneğini kullanarak alt parçalara böler.
metin3="Selam sizleri böyle görmek bizi mutlu etti."
print(metin3.split(" "))
#kelimeler diziye ayrıldıktan sonra istenen index değerini göstermek için.
print(metin3.split(" ")[4])

#Capitalize() : İlk karakteri büyük harfe çevirir. fonksiyonlar art arda kullanılabilir
metin4="selam    sağımda iki boşluk var  "
print(metin4.capitalize().strip())

#Casefold() : String değeri küçük harfe çevirir.
selam="SELAAmamam"
print(selam.casefold())
#Center() : String değeri belirtilen karakter uzunluğunda ortalar.
isim="Faruk Akpınar"
print(isim.center(40))
#Count() : Bir değerin kaç defa tekrarlandığını verir.
metin5="sen öyle bir sen oldu ki içimde ben de senden öte sen demeye sensiz geldim."
print(metin5.count("sen"))
#Encode() : String değerdeki ü i ö ı karakterlerininin utf-8 karşılıklarını gösterir
print(metin5.encode())
#Endswith() : String değer belirli bir değerle bitiyorsa true değer döndürür.
print(metin5.endswith("."))


#Expandtabs() : String değeri belirtilen tab uzunluğunda yeniden düzenler.

#Find() : String değerde belirli bir değer arar ve bulduğu yeri döndürür.

#Index() : String değerde belirli bir değer arar ve bulduğu yeri döndürür.

#Join() : Öğeyi string değerin sonuna ekler.

#Ljust() : String değerin sola hizalı versiyonunu döndürür.

#Rjust() : String değerin sağa hizalı versiyonunu döndürür.

#isalnum() : String değerdeki tüm karakterler alfanumerik değerse (A-Z, a-z, 0–9) True döndürür.

#isalpha() : String değerdeki tüm karakterler alfabetik değerse (A-Z, a-z) True döndürür.

#isdecimal() : String değerdeki (Unicode) tüm karakterler ondalıklı değerse True döndürür.

#isnumeric() : String değerdeki tüm karakterler numerik değerse True döndürür.

#isdigit() : String değerdeki tüm karakterler tek haneli rakamsa True döndürür.

#isidentifier() : String geçerli bir tanımlayıcı değer ise True döndürür.

#islower() : String değerdeki tüm karakterler küçük harf ise True döndürür.

#isupper() : String değerdeki tüm karakterler büyük harf ise True döndürür.

#isprintable() : String değerdeki tüm karakterler yazdırılabilir ise True döndürür.

#isspace() : String değerdeki tüm karakterler boşluksa True döndürür.

#istitle() : String değerdeki her sözcüğün baş harfi büyük ise başlık olabilir, True döndürür.

#Partition() : String değeri üç parçaya ayırır.

#Splitlines() : String değeri satır sonlarında böler ve bir liste oluşturur.

#Swapcase() : Büyük harfleri küçük harfe, küçük harfleri büyük harfe çevirir.

#Startswith() : String belirli bir değerle başlıyorsa True döndürür.

#Zfill() : String değerin başına belirtilen sayıda 0 koyar.
k="444"
print(k.zfill(10))

#Format () kendisine iletilen numerik değişkenleri alır, biçimlendirir ve bunları { } şeklindeki yer tutucularının bulunduğu string e yerleştirir:

yaş1=40
yaş2=5
metin6="Ailemde {0} ve {1} yaşında insanlar var"
print(metin6.format(yaş1,yaş2))


# f .2f .3f kullanımı f-virgünden sonra 6 basamak   .2f - virgülden sonra 2 basamak
miktar = 5
fiyat=11.44
tutar=miktar*fiyat
siparişNotu="Fiyatı {1} olan cipsten {0} adet alarak toplamda {2} TL ödeme yaptım."
print(siparişNotu.format(miktar,fiyat,tutar))

siparişNotu="Fiyatı {1:.2f} olan cipsten {0:f} adet alarak toplamda {2:.2f} TL ödeme yaptım."
print(siparişNotu.format(miktar,fiyat,tutar))

#metin içindeki {} içine 
#:< →Verilen değeri belirtilen boşluğa göre sola hizalar.
s1="Sıcaklık {:<10} ile {:<10} santigrat dereceler arasında."
print(s1.format(12,32))
#:> →Verilen değeri belirtilen boşluğa göre sola hizalar.
s2="Sıcaklık {:>10} ile {:>10} santigrat dereceler arasında."
print(s2.format(12,32))
#:^ →Verilen değeri belirtilen boşluğa göre ortalar.

#: (bir boşluk) →Negatif değerlere eksi koyar, pozitif değerlere işaret koymaz.

#:+ →Verilen değerin işareti yoksa pozitif kabul eder ve + koyar

#:- →Sadece negatif değerlere eksi koyar

# :, →Binlik ayıracı olarak ,(virgül) koyar
a="Ana para {:,} liradır."
print(a.format(382978522))
# :% →Verilen değeri sonuna % (yüzde) işareti koyar
faiz1="faiz oranı {:%} 'dır."
print(faiz1.format(0.52))
faiz2="faiz oranı {:.0%} 'dır."
print(faiz2.format(0.52))
faiz3="faiz oranı {:.1%} 'dır."
print(faiz3.format(0.52))
faiz4="faiz oranı {:.2%} 'dır."
print(faiz4.format(0.52))

# :b →Decimal değeri Binary ye çevirir

# :d →Binary değeri Decimal e çevirir


