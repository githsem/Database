import sqlite3
con = sqlite3.connect("kutuphane.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()

def veri_ekle():
    cursor.execute("INSERT INTO kitaplik VALUES('Istanbul Hatirasi','Ahmet Umit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()

isim = input("Isim :")
yazar = input("Yazar :")
yayinevi = input("Yayin Evi :")
sayfa_sayisi = int(input("Sayfa Sayisi :"))
veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi)

con.close()