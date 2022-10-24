""" Software yg kami buat bersifat OPEN SOURCE"""

import sys, os, time, optparse

os.system('cls||clear')

banner ="""
                                   ______
    ___   __           ___   __   | |____|
   / _ \ |  |   ___   |   \ |  |  | |____
  / /_\ \ | |  / _ \   | | \ | |  | |____|
  |  _  | | | | /_\ | _| | \ | |_ | |____
  |_| |_| |__| \___/  |__|  \___| |_|___ |
                                      /_/

    Authors:              RX77E
    Spesial Thank's:      Arief
    Instagram:            https://www.instagram.com/memelucubikin
    GitHub:               https://github.com/Sreetx
"""
try:
    print(banner)
    judulweb = input('\n [?] Masukkan judul web: ')
    desweb = input(' [?] Masukkan deskripsi website: ')
    wallpaper = input(' [?] Masukkan link gambar untuk background(lewatkan jika tidak perlu): ')
    bcgwrn = input(' [?] Masukkan warna background: ')
    wkk = input(' [?] Masukkan warna background kotak judul: ')
    warjud = input(' [?] Masukkan warna judul: ')
    judcont = input(' [?] Masukkan Judul: ')
    backcont = input(' [?] Masukkan warna background kotak pesan: ')
    warcont = input(' [?] Masukkan warna teks pada kotak pesan: ')
    pesan = input(' [?] Masukkan pesan: ')
    pengirim = input(' [?] Masukkan pengirim(lewatkan jika tidak peru): ')

    html = '''<!DOCTYPE html>
<html>
<head>
<title>'''+str(judulweb)+'''</title>
<meta name="description" content="'''+str(desweb)+'''>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body style="background: '''+str(wallpaper)+'''; background-color: '''+str(bcgwrn)+''';">
<div style="width: 100%; border: 1px solid #000000; background-color: '''+str(wkk)+'''; padding: 10px;">
    <center><h1 style="color: '''+str(warjud)+''';"><b>'''+str(judcont)+'''</b></h1></center>
</div>
<br />
<div style="background-color: '''+str(backcont)+'''; border: 1px solid #000000; color: '''+str(warcont)+'''; margin: 10px auto 35px; padding: 10px 4% 20px; max-width: 75%; -webkit-font-smoothing: subpixel-antialiased; box-shadow: 0 1px 1px rgba(166, 166, 166);">
    <center><h3>'''+str(pesan)+'''</h3></center>
    <center><h3>From: '''+str(pengirim)+'''</h3></center>
</div>
</body>
</html>
'''
    print('\n [+] Menyiapkan script'); time.sleep(1.5)
    open('Hasil.html', 'w').write(html)
    print(' [+] Selesai. File disimpan dengan nama "Hasil.html"\n');sys.exit()

except KeyboardInterrupt: print ("\n\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()
    
