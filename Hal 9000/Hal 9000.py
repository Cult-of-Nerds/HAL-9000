#*********
# -*- Created by Ian Smith
# -*- https://github.com/Cult-of-Nerds
# -*- https://www.youtube.com/channel/UCCxkqK3cD49RXKsMSLGrppQ
# -*- This work is licensed under the GNU General Public License v3.0
#*********
#Hal 9000 Terminal
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
Isp899 = "Isp899"
Kalinka = "Kalinka"
Guest = "Guest"
P = 7793
Q = 7789
N = P * Q
B = 1081
A = 56137
U = 0
I = 0
D = 0
Y = 0
G = 0
import os
import time
import subprocess
import webbrowser
import random
import datetime
from time import gmtime, strftime
while a == 0:
    print()
    print('----------Hal-9000 Terminal----------')
    print(time.strftime('----%m/%d/%Y-----------%H:%M:%S----'))
    b = input("1. System Overview\n2. Quit Session\n3. Login\n(1-3): ")
    print('')
    if b == '1':
        print("Access Denied")
        print()
    if b == '2':
        c = input("(y,n): ")
    if c == 'y':
        close
    if c == 'n':
        print()
    if b == '3':
        d = input("Username: ")
    if d == 'Isp899':
        print()
        e = input("Password: ")
    if e == 'Kalinka':
        print()
        print ('Welcome, Isp899')
        print()
        f = input("1. System Overview\n2. Administrative\n3. Quit Session\n4. Logoff\n(1-4): ")
        if f == '1':
            print()
            print(time.strftime('%m/%d/%Y %H:%M:%S'))
            print('All Systems Ok')
            print()
            d = Isp899
            e = Kalinka
        if f == '2':
            print('------------Administrative-----------')
            g = input("1. RSA Encrypter\n2. Applicatons\n3. Station Overview\n4. Root Terminal\n(1-4): ")
        if g == '1':
#*********
# -*- Created by Vance and Ian
# -*- https://github.com/Cult-of-Nerds
# -*- https://www.youtube.com/channel/UCCxkqK3cD49RXKsMSLGrppQ
# -*- This work is licensed under the GNU General Public License v3.0
#*********
#RSA Encryptor
            while U == 0:
                print()
                print('----------RSA Cipher Program---------')
                print()
                I = input("1. Encryption\n2. Decryption\n3. Quit\n(1-3): ")
                print('')
                if I == '1':
                    print("-------------Encrytption-------------")
                    print()
                    X = input('Plaintext: ')
                    YT = list(X)
                    FG = len(X)
                    D=0
                    Y = open('RSAC.txt','w')
                    for K in range(FG):
                        try:
                            XY = ord(YT[D])** B %N
                            #ord(XY) gives the keyboard number for XY   
                        except:
                            print('ERROR 1: ENCRYPT_ONLY_LETTERS')
                            X = 0
                            XY = 0
                        Y.write(str(XY) + '\n')
                        D = D+1
                    Y.close()
                    E = open('RSAC.txt','r')
                    print(E.read())
                    E.close()
                if I == '2':
                    print("-------------Decryption--------------")
                    print()
                    HH = ''
                    CC = ''
                    U = open('RSAP.txt','w')
                    print('Ciphertext: ')
                    while HH != 'done':
                        try:
                            Y = input()
                            if Y == 'done' or Y == '':
                                HH = 'done'
                            if Y != 'done' and Y != '':
                                YX = int(Y)**A %N
                                U.write(chr(YX))
                                
                            #chr(YX) gives the letter of the keyboard number YX
                        except:
                            print('ERROR 2: DECRYPT_BY_NUMERICAL_SETS')
                            Y = Y
                            YX = YX
                            HH = 'done'
                    U.close()
                    I = open('RSAP.txt','r')
                    print(I.read())
                    I.close()
                    input()
                if I != '1' and I != '2' and I != '3':
                    print("ERROR 3: ONLY CHOOSE 1-3")
                input()
                U = 0
                if I == '3':
                    print("----------------Exit?----------------")
                    G = input("Are you sure you want to Exit? . . . Hal 9000 is a lot worse.\n(y,n): ")
                    if G == 'y':
                        print('')
                        d = Isp899
                        e = Kalinka
                    if G == 'n':
                        print('')
                        main()
                        g = '1'
        if g == '4':
            print()
            j = input("root@HAL9000: ")
        if j == 'Open the pod bay doors please Hal.':
            print("I'm sorry Dave. I'm afraid I can't do that.")
            d = Isp899
            e = Kalinka
            j = input("root@HAL9000: ")
        if j == 'Do you read me Hal?':
            print("Affirmative, Dave. I read you.")
            d = Isp899
            e = Kalinka
            j = input("root@HAL9000: ")
        if j == 'Whats the problem Hal?':
            print("I think you know what the problem is just as well as I do.")
            d = Isp899
            e = Kalinka
            j = input("root@HAL9000: ")
        if j == 'What are you talking about?':
            print("This mission is too important for me to allow you to jeopardize it.")
            d = Isp899
            e = Kalinka
            j = input("root@HAL9000: ")
        if j == 'What are you talking about, Hal?':
            print("I know that you and Frank were planning to disconnect me and I'm afraid that's something I cannot allow to happen.")
            d = Isp899
            e = Kalinka
            j = input("root@HAL9000: ")
        if j == 'Date':
            print (time.strftime('%m/%d/%Y %H:%M:%S'))
            d = Isp899
            e = Kalinka
            j = input("root@HAL9000: ")
        if j == 'Weather':
            webbrowser.open('https://weather.com/weather/today')
            d = Isp899
            e = Kalinka
        if j == 'Search':
            print('What to search?')
            findWeb = input()
            if findWeb != ('STOP'):
                webbrowser.open('https://www.google.com/search?ei=yDG3XImiBKaAtgWyyLi4Bw&q='+ findWeb +'&oq=hello+def&gs_l=psy-ab.1.0.0l10.3811.4542..5781...0.0..0.266.773.0j2j2......0....1..gws-wiz.......0i71j0i67j0i131.YtTXdO35_O4')
                d = Isp899
                e = Kalinka
        if j == 'help':
            print("-----------I need somebody-----------")
            print("For more information on a specific command, type HELP <<command-name>>")
            print()
            print("Date         Displays the date and time.")
            print()
            print("Search       Search the internet.")
            print()
            print("Weather      Displays the current weather.")
            d = Isp899
            e = Kalinka
        if j == 'help Date':
            print("Displays the date and time.(m/d/y H:M:S)")
            d = Isp899
            e = Kalinka
        if j == 'help Search':
            print("Searches the internet using the default web browser.")
            d = Isp899
            e = Kalinka
        if j == 'help Weather':
            print("Displays the weather in the default web browser.(weather.com)")
            d = Isp899
            e = Kalinka
        if j == 'quit':
            close
        if j == 'exit':
            print()
            d = Isp899
            e = Kalinka
        if j == 'logoff':
            print()
        if g == '2':
            print('-------------Applications------------')
            print()
            h = input("1. Google Chrome\n2. Steam\n3. Discord\n4. Spotify\n5. Word\n6. Outlook\n7. File Explorer\n8. Adobe Premiere\n9. Paint\n10.Notepad+ +\n(1-10): ")
            if h == '1':
                subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
            if h == '2':
                subprocess.Popen(['C:\Program Files (x86)\Steam\Steam.exe'])
                d = Isp899
                e = Kalinka
            if h == '3':
                subprocess.Popen(['C:/Users/ips89/AppData/Local/Discord/Update.exe'])
                d = Isp899
                e = Kalinka
            if h == '4':
                subprocess.Popen(['C:/Users/ips89/AppData/Roaming/Spotify/Spotify.exe'])
                d = Isp899
                e = Kalinka
            if h == '5':
                subprocess.Popen(['"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"'])
                d = Isp899
                e = Kalinka
            if h == '6':
                subprocess.Popen(['"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"'])
                d = Isp899
                e = Kalinka
            if h == '7':
                subprocess.Popen(['C:\Windows\SysWOW64\explorer.exe'])
                d = Isp899
                e = Kalinka
            if h == '8':
                subprocess.Popen(['"C:\Program Files\Adobe\Adobe Premiere Elements 2019\Elements Home\Adobe Premiere Elements 2019.exe"'])
                d = Isp899
                e = Kalinka
            if h == '9':
                subprocess.Popen(['C:\Program Files\Mozilla Firefox\firefox.exe'])
                d = Isp899
                e = Kalinka
            if h == '10':
                subprocess.Popen(['C:\Program Files\Mozilla Firefox\firefox.exe'])
                d = Isp899
                e = Kalinka
        if g == '3':
            print("----------Station Overview-----------")
            i = input("Joint Air-Locks: Secure\nPod-Bay Doors: Secured\nPhotovoltaic Arrays: Charging 87% Efficiency\nElectrical: 0 Faults\n HRS Radiators: 38C\nTOTAL FAULTS: 0\n\nroot@HAL9000: ")
        if i == 'Open the pod bay doors please Hal.':
            print("I'm sorry Dave. I'm afraid I can't do that.")
            d = Isp899
            e = Kalinka
        if i == 'Do you read me Hal?':
            print("Affirmative, Dave. I read you.")
            d = Isp899
            e = Kalinka
        if i == 'Whats the problem Hal?':
            print("I think you know what the problem is just as well as I do.")
            d = Isp899
            e = Kalinka
        if i == 'What are you talking about?':
            print("This mission is too important for me to allow you to jeopardize it.")
            d = Isp899
            e = Kalinka
        if i == 'What are you talking about, Hal?':
            print("I know that you and Frank were planning to disconnect me and I'm afraid that's something I cannot allow to happen.")
            d = Isp899
            e = Kalinka
        if f == '3':
            print("------------Quit Session?------------")
            c = 0
            c = input("(y,n): ")
        if c == 'y':
            print()
        if c == 'n':
            print()
            d = Isp899
            e = Kalinka
        if f == '4':
            d = 0
            e = 0
            print()
    if d == 'Guest':
        print()
        e = input("Password: ")
    if e == 'Guest':
        print()
        print('Welcome, Guest')
        print()
        f = input("1. System Overview\n2. Quit Session\n3. Logoff\n(1-3): ")
        if f == '1':
            print()
            print (time.strftime('%m/%d/%Y %H:%M:%S'))
            print('All Systems Ok')
            print()
            d = Guest
            e = Guest
        if f == '2':
            print("------------Quit Session?------------")
            c = 0
            c = input("(y,n): ")
        if c == 'y':
            close
        if c == 'n':
            print()
            d = Guest
            e = Guest
        if f == '3':
            d = 0
            e = 0