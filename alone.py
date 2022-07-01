""" Software yg kami buat bersifat OPEN SOURCE"""

import sys, os, time

os.system(' ')

print ("\n[*] Memulai Program....\n")
time.sleep(3)
print (" [..............................] 0%")
time.sleep(1)
print (" [>>>>>>>>>>>>..................] 40%")
time.sleep(2)
print (" [>>>>>>>>>>>>>>>>>>>>>>........] 78%")
time.sleep(1)
print (" [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>] 100%\n")
time.sleep (2)
print (" [*] Membuka Program....\n")
time.sleep(3)

banner ="""
                                   ______
    ___   __           ___   __   | |____|
   / _ \ |  |   ___   |   \ |  |  | |____
  / /_\ \ | |  / _ \   | | \ | |  | |____|
  |  _  | | | | /_\ | _| | \ | |_ | |____
  |_| |_| |__| \___/  |__|  \___| |_|___ |
                                      /_/"""

print (banner)
print (" Authors:              RX77E")
print (" Spesial Thank's:      Arief")
print (" Instagram:            https://www.instagram.com/memelucubikin")
print (" GitHub:               https://github.com/Sreetx")

try:
    print (" [#] Alone adalah sebuah tools pembuat script deface web yg sangat simple dan praktis")
    enter = input("\n [#] Tekan enter untuk melanjutkan...")

    judul = input(" [?] Masukkan judul web/script yang akan dibuat: ")
    deskripsi = input(" [?] Masukkan deskripsi web/script: ")
    tema = input(" [?] Masukkan warna background, tersedia dalam[white, black, green, purple, red, blue]: ")
    link = input(" [?] Masukkan link gambar untuk background: ")
    pembukaan = input(" [?] Masukkan judul pesan yang akan ditulis: ")
    warnajudul = input(" [?] Masukkan warna judul, tersedia dalam[white, black, green, purple, red, blue]: ")
    pesan = input(" [?] Masukkan pesan yang akan ditulis: ")
    warnatulisan = input(" [?] Pilih warna tulisan, tersedia dalam[white, black, green, purple, red, blue]: ")
    penutup = input(" [?] Masukkan nama samaran kalian. misal: RX77E(lewatkan jika tidak perlu): ")
except KeyboardInterrupt: print ("\n\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()

print ("\n [*] Menyiapkan File....")
open("Hasil script.html", "w").write("""<!DOCTYPE html>
<html lang="en" style="padding-left: 32px; padding-right: 32px; margin-left: 32px; margin-right: 32px;">
<head>
<title>"""+judul+"""</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=width-device, initial-scale=1">
<meta name="description" content=" """+deskripsi+""" ">
</head>
<body background=" """+link+"""" style="background-color: """+tema+""";">
<br />
<center><p style="color: """+warnajudul+"""; font-size: 35px;"><b>"""+pembukaan+"""</b></h1></center>
<br />
<center><p style="color: """+warnatulisan+"""; font-size: 23px;">"""+pesan+"""</h3></center>
<br></br>
<br></br>
<br></br>
<p align="right" style="color: red; font-size: 17px;">"""+penutup+"""    </p>
</body>
</html>""")

print ("  [*] Selesai")
print ("  [*] File berhasil disimpan dengan nama 'Hasil Script.html'^_^\n")

try:
    thank = input(" [?] Terima kasih ke: ")
    if thank.lower() in ('Arief').split():
        print ("\n [*] Terima kasih kembali :)")
        print ("\n [*] Mematikan program....\n");time.sleep(3);sys.exit()
    else:
        print ("\n [*] Mematikan program....\n");time.sleep(3);sys.exit()
except KeyboardInterrupt: print ("\n\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()
    
