ENGLISH: (Překlad do češtiny je níže)
Peer to peer translation

------------------------------------------------------------------

Configuration
    1. open config.json: nano config.json
    2. change port value to port you want the program to listen on
    3. change ip to your pc local ip address
    4. change subnet-range to your specified range in this format:
        an example of a local ip address: 192.168.80.5
                                     first.second.third.fourth
        format of this range is: "from_third-to_third-from_fourth-to_fourth"
        so when a network scan is needed the scanner will scan ip addresses from: 192.168.from_third.from_fourth to: 192.168.to_third.to_fourth
        for example: subnet-range="80-90-1-254"
            program will scan: 192.168.80.1, 192.168.80.2, 192.168.80.3, ..., 192.168.80.254, 192.168.81.1, ..., 192.168.90.254
    5. change word-dict to your words you want to be able to translate
    6. cut and paste config.json and log.txt to /home folder
	sudo mv /YOUR_DIRECTORY/config.json /home
	sudo mv /YOUR_DIRECTORY/log.txt /home

------------------------------------------------------------------

Installation

    1. check if you have systemd installed:
        - type in your terminal: systemd --version"
            -if the output isn't similar to this: systemd 247 (247.3-6)
                -install systemd (need sudo privileges "sudo"): apt install -y systemd

    2. place p2ptranslate.service in /etc/systemd/system (need sudo privileges "sudo")
	mv /YOUR_DIRECTORY/p2ptranslate.service /etc/systemd/system

        -edit p2ptranslate.service: nano p2ptranslate.service
            -change USER_NAME in User=USER_NAME to your username
            -change /PATH/TO/FILE.py in ExecStart=/usr/bin/python3 /PATH/TO/FILE.py to the location where main.py is located (example: /home/tom/main.py)

    3. execute:
        systemctl enable p2ptranslate
        systemctl daemon-reload
        systemctl start p2ptranslate

    4. check if daemon is running:
        systemctl status p2ptranslate 

------------------------------------------------------------------

Troubleshooting
"That word cannot be translated locally."
Either the word is not stored locally or config file is missing. Check if in /home folder is config.json and if it's set by Configuration standards, or generate new config file by running build_conf.py.

"That word cannot be translated remotely."
Either the word is not stored remotely, there is no connection to network or no other running translator application.

"That word cannot be translated in any way."
Either the word is not stored locally and remotely, there is no connection to network or no other running translator application.

"Config file is missing. Run build_conf.py"
config.json is not in /home folder, check if it's still in original folder and move it in /home or run build_conf.py to generate new config file in /home that has to be configured

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ČESKY:
Peer to peer překladač

------------------------------------------------------------------

Konfigurace
    1. otevři config.json: nano config.json
    2. změň hodnotu port na port na kterém chceš aby program naslouchal
    3. změň ip na lokální ip adresu počítače
    4. změň subnet-range na tvůj specifický rozsah v tomto formátu:
        příklad lokální ip adresy: 192.168.80.5
                       první.druhý.třetí.čtvrtý
        formát subnet-range je: "od_třetí-do_třetí-od_čtvrtý-do_čtvrtý"
        takže když je potřeba sken sítě,skenr projede ip adresy od: 192.168.od_třetí.od_čtvrtý do: 192.168.do_třetí.do_čtvrtý
        například: subnet-range="80-90-1-254"
            program proskenuje: 192.168.80.1, 192.168.80.2, 192.168.80.3, ..., 192.168.80.254, 192.168.81.1, ..., 192.168.90.254
    5. změň word-dict na slova které chceš být schopný přeložit
    6. přesuň config.json a log.log do /home složky
	sudo mv /YOUR_DIRECTORY/config.json /home
	sudo mv /YOUR_DIRECTORY/log.txt /home

------------------------------------------------------------------

Instalace

    1. zkontroluj jestli máš systemd nainstalované:
        - napiš do svého terminálu: systemd --version
            -pokud výstup není podobný: systemd 247 (247.3-6)
                -nainstaluj systemd (je třeba mít sudo práva "sudo"): apt install -y systemd

    2. přesuň p2ptranslate.service do /etc/systemd/system/ (je třeba mít sudo práva "sudo")
	mv /YOUR_DIRECTORY/p2ptranslate.service /etc/systemd/system

        -přepiš p2ptranslate.service: nano p2ptranslate.service
            -změň USER_NAME v User=USER_NAME na své uživatelské jméno
            -změň /PATH/TO/FILE.py v ExecStart=/usr/bin/python3 /PATH/TO/FILE.py na místo, kde je main.py uložený (příklad: /home/tom/main.py)

    3. spusť:
        systemctl enable p2ptranslate
        systemctl daemon-reload
        systemctl start p2ptranslate

    4. zkontroluj jestli je daemon spušťen:
        systemctl status p2ptranslate 

------------------------------------------------------------------

Řešení problémů
"That word cannot be translated locally."
Buď vámi hledané slovo není uložené lokálně nebo soubor config chybí. Zkontroluje jestli ve složce /home je config.json a jesti je nakonfigurovnán podle standardů Konfigurace, nebo si vygeneruj nový pomocí build_conf.py.

"That word cannot be translated remotely."
Buď vámi hledané slovo není uložené na síťi, není žádné připojení k síťi nebo nejsou na síťi žádné jiné běžící překládací aplikace.

"That word cannot be translated in any way."
Buď vámi hledané slovo není uložené ani lokálně a ani na sítí, není žádné připojení k síťi nebo nejsou na síťi žádné jiné běžící překládací aplikace.

"Config file is missing. Run build_conf.py"
config.json není ve složce /home, zkontrolujte jestli je stále v původní složce a přesuňte ho do /home nebo spusttě build.conf.py na vygenerování nového souboru config ve složce /home, který se musí nakonfigurovat.

