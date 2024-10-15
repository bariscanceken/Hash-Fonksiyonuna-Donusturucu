import hashlib

password_input = input("Neyi Şifrelemek İstersin?: ")
with_which = int(input("Hangi Şifreleme Yöntemiyle Şifrelemek İstersin? |(1)md5,(2)sha1,(3)sha224,(4)sha256,(5)sha384,(6)sha512)| :  "))
sifrelenecek = password_input

number = [1,2,3,4,5,6]

def convert() :
    
    global sifrelenecek

    if with_which == 1 :
            sifreleyici = hashlib.md5()
            neyle = "md5"
            
    elif with_which == 2 :
         sifreleyici = hashlib.sha1()
         neyle = "sha1"
         
    elif with_which == 3 :
         sifreleyici = hashlib.sha224()
         neyle = "sha224"
         
    elif with_which == 4 :
         sifreleyici = hashlib.sha256()
         neyle = "sha256"
         
    elif with_which == 5 :
         sifreleyici = hashlib.sha384()
         neyle = "sha384"
         
    elif with_which == 6 :
         sifreleyici = hashlib.sha512()
         neyle = "sha512"
         
    while with_which not in number :
        print("Hatalı Veri Girdiniz. Tekrar Deneyin!")
        convert()

    sifreleyici.update(sifrelenecek.encode())
    typestr = sifreleyici.hexdigest()

    with open("hashconverter.txt", "a") as file:
        file.write(f"{sifrelenecek} ----> {neyle} ile sifrelenmis hali = {typestr}\n")

convert()