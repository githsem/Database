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
def veri_al():
    cursor.execute("SELECT * FROM kitaplik")
    liste = cursor.fetchall()
    print("Kitaplik Listeleri")
    for i in liste:
        print(i)
def veri_al2():
    cursor.execute("SELECT Isim,Yazar FROM kitaplik")
    liste = cursor.fetchall()
    print("Kitaplik Listeleri")
    for i in liste:
        print(i)
def veri_al3(yayinevi):
    cursor.execute("SELECT * FROM kitaplik Where Yayinevi = ?",(yayinevi,))
    liste = cursor.fetchall()
    print("Kitaplik Listeleri")
    for i in liste:
        print(i)

yayinevi = input("Yayinevini Giriniz : ")
veri_al3(yayinevi)

con.close()