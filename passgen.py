

def passgenerator():
    info = {
    'thn':int(input('Mulai Tahun? :')),
    'kel':int(input('Sampai Tahun? : '))
    }
    simpan = open(input('masukan nama dan file format .txt : '),'w')


    for thn in range(info['thn'],info['kel']+1):
        for w in range(1,13):
            for r in range(1,32):

                print(f"{r}{w}{thn}")
                
                simpan.write(f"{r}{w}{thn}\n")


    simpan.close()
    print("Done")
    pass


print("    ____  ___   __________ _____________   __ ")
print("   / __ \/   | / ___/ ___// ____/ ____/ | / / ")
print("  / /_/ / /| | \__ \\__ \ / / __/ __/ /  |/ /  ")
print(" / ____/ ___ |___/ /__/ / /_/ / /___/ /|  /   ")
print("/_/   /_/  |_/____/____/\____/_____/_/ |_/    ")
                                             

while __name__=="__main__":


    print('password generator')
    print('(1) password generator Tanggal lahir!')
    print("(2) EXIT ")
    print(10*"==")
    
    masuk = str(input("Masukan pilihan(angka)? "))
        
    if masuk == "1":
            passgenerator()
        
    if masuk == "2":
            exit()


    
