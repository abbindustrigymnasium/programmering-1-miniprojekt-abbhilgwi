import random                                                                        #importerar det som behövs
import time

poäng=0                                                                              #En variabel som lagrar antalet poäng, B spelet
ett=0                                                                                #1,x,2 varibler som lagrar hur många gånger användaren svarat vardera alterntiv, A spelet
x=0
två=0
i=0                                                                                  #Två olika varibler som används till whileloopar
n=0

spela = True                                                                        #En bool som används i en while för att det ska gå att köra spelet flera gånger

def svar(val,alternativ):                                                           #Deffinierar en metod som används för att kolla vad användaren svarat, A spelet
    global ett                                                                      #För att resultatet av metodens påverkan på variablerna ska lägga sig på varandra och inte nollställas då metoden körs igen behöver metoden använda global variabler
    global två
    global x
    if val == alternativ:                                                           #Ifall valet är det samma som alternativet ska den kolla vilket altenativ som valet stämmer som, och lägga till 1 i den variabeln
        if alternativ=="1":                                                         
            ett += 1
        elif alternativ=="2":
            två += 1
        elif alternativ== "X" or "x":
            x += 1

def inrefrukt():                                                                    #Deffinierar en metod som lottara en fråga ur en lista och skriver ut den samt använder metoden 'svar', A spelet
    kopia1 = fruktegenskaper                                                        #Säger att en kopia av listan med alla frågor är lika dan som listan med frågorna, det gör att det går att ta bort frågor ur kopian utan att behöva lägga tillbaka dem innan en spelar igen    
    while len(kopia1) > 0:                                                          #Sägar att så länge det finns alternativ kvar i 'kopia1' så ska metoden köras
        z = kopia1.pop(random.randint(0,len(kopia1)-1))                             #Tar ur ett random valt index ur kopian som representerar en fråga som nu lagras i variablen z
        print(z)                                                                    #Skriver ut frågan
        b=input("\n >").upper()                                                     #Användarens svar ovanlat till CapsLock för att det inte ska vara shiftlägeskänsligt
        svar(b,"1")                                                                 #Använder metoden svar för att se om användaren svarat 1, x eller 2 och lägger sedan till 1 i rätt variabel
        svar(b,"X")
        svar(b,"2")

def res1(var,frukt):                                                                #Alternatv 1 av resultatet, ifall någon av variablerna är lika med eller större än fem, A spelet
    if var >= 5:
        print("Du är en",frukt)

def res2(var1,var2,frukt):                                                          #Alternativ 2 av resultatet, ifall ingen av variblerna av överlägset störst men en av dem är liten, A spelet
    if var1 >= 4 and var2 >=2 or var2 >= 4 and var1 >= 2:
        print ("Du är en",frukt)

def res3(var1,var2,var3):                                                           #Alternativ 3 av resultatet, ifall två av veriablerna har samma värde, A spelet
    if var1 > 1 and var1 == var2 or var1 > 1 and var1 == var3 or var2>1 and var2 == var3:
        print('Du är en lurig en... Du är en hel fruktsallad!')

def poängen(gissa,svar):                                                            #Deffinierar en metod som ser om användaren svarat rätt och isåfall ger den ett poäng samt meddelar den ifall svaret var rätt eller inte, B spelet
    global poäng                                                                    #För att resultatet av metodens påverkan på variabeln ska lägga sig på varandra och inte nollställas då metoden körs igen behöver metoden använda global variabel
    if gissa == svar:                                                               #Ifall gissa är det samma som svar får användaren ett poäng och ett meddelande som berättar det medan om det inte är så får användaren ett meddelande som säger att den svarat fel och berättar det korrekta svaret
        poäng += 1
        print("Rätt! Grattis, du fick en poäng :D \n")
    else:
        print('Tyvärr, fel svar :/ Rätt svar var',svar,'\n')

def fruktfrågor():                                                                  #Deffinierar en metod som lottar en fråga och dess svar ur en lista, tar isär frågan och svaret och skriver ut frågan samt använder metoden 'poäng', B spelet
    kopia2 = frågor                                                                 #Visar att en kopia av lstan med frågor och var innehåller exakt samma saker som listan 'frågor'
    while len(kopia2) > 0:                                                          #Säger att så länge det finns alternativ kvar i 'kopia2' så ska metoden köras
        a = kopia2.pop(random.randint(0,len(kopia2)-1))                             #Tar ut ett random valt index ur kopian och lagrar den i variabeln a
        frågan = a[0]                                                               #Placerar frågan och dess svar i olika variabler
        svaret = a[1]
        print(frågan)                                                               #Skriver ut frågan
        f = input('>').upper()                                                      #Användarens input lagras i variabeln f och görs om till CapsLock
        poängen(f,svaret)                                                           #Använder metoden 'svar' med användarens input och svaret på frågan

def avslut():                                                                       #Deffinierar en metod som avslutar loopar
    raise KeyboardInterrupt

fruktegenskaper = [                                                                 #En lista med frågor och alternativ, A spelet
    "\n \n En varm sommardag föredrar jag... \n 1) att ligga ute och jäsa i solen \n X) att vara innomhus i den sköna skuggan \n 2) att ligga i (jord)källaren och vänta på bättre tider",
    "\n \n Jag tycker bäst om \n 1) klara, starka färger som syns! \n X) färger som inte är så uppseendeväckande, fast fortfarande färger \n 2) svart. Eller andra jordnära färger som smälter in",
    "\n \n Jag är för det mesta... \n 1) explosiv! Bäst att ta chansen när den kommer \n X) smart. Jag prioriterar mina resurser så att de ska räcka länge \n 2) obrydd. Det brukar aldrig vara något problem att räcka till",
    "\n \n Andra beskriver ofta mig som... \n 1) speciell. Antingen älskar man mig eller så avskyr man mig \n X) ok. Ingen brukar ha någon speciell åsikt men ingen verka tycka illa om mig heller \n 2) ... Vilka andra? Folk brukar inte vara med mig om de inte måste",
    "\n \n Mitt ego säger att jag är... \n 1) söt! \n X) ofta rätt sur... \n 2) meh",
    "\n \n Jag är... \n 1) självsäker! Jag vet vem jag är och är nöjd med det \n X) ... ingen aning.... \n 2) inte direkt osäker... Men jag föredrar om jag inte syns",
    "\n \n Folk brukar kalla mig... \n 1) olika smeknamn. Jag är så speciell att de inte kan bestämma sig \n X) mitt namn?.. Vad annars? \n 2) En hel del saker som inte ska talas öppet om.. Jag blir ofta asocierad med andra.. mindre trevliga.. typer",    
]
frågor = [                                                                          #En lista med frågor och korrekt svar, B spelet
    ['Vilken frukt är bäst föräldrar?','PÄRON'],
    ['Vilken grönsak är Titanic mest rädd för?','ISBERGSSALLAD'],
    ['Vilka baljväxter gör att man ser arg ut?','RÖDA LINSER'],
    ['Vad kallas en skilsmässa i Göteborg?','PÄRONSPLITT'],
    ['Vilken grönsak är mest lättskrämd?','RÄDISA'],
    ['Vilket bär svarar bäst i telefon?', 'HALLON'],
    ['Vilken grönsak är bäst mamma?','MOROT'],
    ['Vilken grönsak är bäst pappa?','PAPRIKA'],
]
kopia1 = []                                                                     #De två kopiorna av listor som är tomma till dess att de används i metoderna 'inrefrukt' repektive 'fruktfrågor'
kopia2 = []

print("- "*18,"\n","-"*32,"\n Välkommen till Frågande Frukten!","\n","-"*32,"\n","*"*32,"\n","*"*7," "*6,"*"*7," ","*"*7,"\n","*"*6," ","*"*4," ","*"*6," ","*"*7, "\n","*"*12," ","*"*7," ","*"*7,"\n","*"*11," ","*"*8," ","*"*7,"\n","*"*10," ","*"*9," ","*"*7,"\n","*"*9," ","*"*10," ","*"*7,"\n","*"*32,"\n","*"*9," ","*"*10," ","*"*7,"\n","*"*32,"\n","-"*32,"\n"," "*7,"Vill du spela?!","\n"," "*6,"~"*17,"\n"," "*7,">Ja"," "*6,">Nej","\n","-"*32)    #Ett designat välkomstmeddelande med frågan ifall användaren vill spela
a=input(">").upper()                                                                #Användarens input fast i CapsLock, lagrad i variabeln a

try:                                                                                #Ifall användarens input inte stämmer överens med något av följande if-sats vilkor, kör exept
    if a == "JA":                                                                   #Ifall användarens svar är JA
        while spela == True:                                                        #Så länge inte boolen spela ändras till False ska koden köra omigen
            print("Vad vill du spela?","\n a) 'Min inre frukt'" "\n b) 'Fruktastiska frågor'","\n \n Skriv 'a' eller 'b'")  #Frågar användaren vilket spel den vill köra
            d =input(">").upper()                                                   #Användarens svar fast CapsLock, lagrad i variabeln d
            
            if d == "A":                                                            #Ifall användarens svar är A startar A spelet
                print("Vad frukt-ansvärt roligt!","\n Här kommer spelet;")          #Meddelande för att presentera spelet
                time.sleep(1)                                                       #En kort paus för att läsaren ska hinna läsa
                print("\n \n","Vad stämmer bäst in på dig? \n(Om du inte anger ett gilltigt alternativ kommer svaret inte att räknas med)")                        #Förklarar vad användaren ska svara på
                inrefrukt()                                                         #Kör metoden 'inrefrukt', som alltså är spelet
                res1(ett,'Drakfrukt!')                                              #Kör första alternativet av resultat med variabeln ett
                res1(x,'Äpple!')                                                    #Kör första alternativet av resultat med variabeln x
                res1(två,'Potats!')                                                 #Kör första alternativet av resultat med variabeln två
                res2(ett,x,'Apelsin!')                                              #Kör andra alternativet av resultat med variablerna ett & x
                res2(ett,två,'Tomat!')                                              #Kör andra alternativet av resultat med variablerna ett & två
                res2(x,två,'Morot!')                                                #Kör andra alternativet av resultat med variablerna x & två
                res3(ett,x,två)                                                     #Kör trdeje alternativet av resultat med samtliga variabler; ett, x &två
                time.sleep(1)                                                       #Ger användaren till att läsa resultatet
                print('\n Vad vill du göra nu?!')                                   #Frågar användaren ifall den vill fortsäta spela med mellanrum mellan textraderna för att ge den tid att läsa samt för att skapa effekt av ett samtal
                time.sleep(1)
                print('Vill du fortsätta eller sluta spela?!',"\n a) 'Fortsätta'" "\n b) 'Sluta spela'","\n \n Skriv 'a' eller 'b'")
                e =input(">").upper()                                               #Användarens val fast CapsLock, lagrad i variabeln e
                if e == "B":                                                        #Ifall användaren väljer att inte fortsätta spela säger programmet hejdå och ändrar boolen spela till false så att loopen bryts och programet avslutas
                    print('Okejdå, ses snart igen!')                                
                    time.sleep(2)
                    spela = False
                elif e == "A":                                                      #Ifall användaren väljer att fortsätta att spela svarar programmet och loopen startas om från där den frågar vilket spel användaren vill köra
                    print('Vad kul!')
                    time.sleep(1)           
            
            elif d == "B":                                                          #Ifall användaren väljer B startas B spelet
                print("Vad banannars skulle du vilja?!", '\n Du kommer att få frågor och så svarar du den frukt, grönsak eller liknanade som du tror är rätt!','\n Ps. Stavning är viktigt så check den innan du svarar :P')    #Förklarar vad spelet går ut på och vad användaren ska göra
                time.sleep(2)                                                       #Paus för att användaren ska hinna läsa instruktionerna
                print('\n Nu börjar vi;','\n')                                      #Förklarar att spelet börjar                                     
                fruktfrågor()                                                       #Kör metoden 'fruktfrågor', som alltså är spelet
                if poäng < 4:                                                       #Beroende på om användaren får mindre än fyra poäng eller inte så berättar programmet det olika för att vara trevlig
                    print('Du fick',str(poäng),'rätt, det var iaf ett bra försök!')
                else:
                    print('Du fick',str(poäng),'rätt, bra jobbat!')
                time.sleep(1)                                                       #Tid så att användaren ska hinna läsa
                print('\n Vad vill du göra nu?!')                                   #Frågar ifall användaren vill fortsätta spela med mellanrum för att den ska hinna läsa samt för att ge effekten av ett samtal
                time.sleep(1)
                print('Vill du fortsätta eller sluta spela?!',"\n a) 'Fortsätta'" "\n b) 'Sluta spela'","\n \n Skriv 'a' eller 'b'")
                e =input(">").upper()                                               #Användarens svar fast CapsLock, lagrad i variabeln e
                if e == "B":                                                        #Ifall användaren väljer att inte fortsätta spela säger programmet hejdå och variabeln spela ändras till False så att loopen bryts och programmet avslutas
                    print('Okejdå, ses snart igen!')
                    time.sleep(2)
                    spela = False
                elif e == "A":                                                      #Ifall användaren väljer att fortsätta spela svarar programmet och loppen börjar om från valet av spel
                    print('Vad kul!')
                    time.sleep(1)
            
            else:                                                                   #Ifall användaren inte väljer ett gilltigt alternativ kommer den att komma till except
                avslut()
    
    elif a == "NEJ":                                                                #Ifall användaren svarar att den inte vill spela försöker programmet övertyga användaren om motsatsen, sedan kommer den till except
        print("Nej! Vad synd :(","\n","Säg bara till om du ångrar dig...")
        time.sleep(1)
        print("\n","\n","Den gröna knappen")
        time.sleep(2)
        print("\n","\n","Där uppe!")
        time.sleep(1)
        print("\n","Till höger!")
        time.sleep(2)
        print("\n","ok...")
        time.sleep(0.5)
        print("...fattar vinken")
        time.sleep(0.5)
        print("\n","\n")    
    
    else:                                                                           #Ifall användaren inte ger ett gilltigt svar på frågan om den vill spela kommer den till except
        avslut()

except KeyboardInterrupt:                                                           #Except, ifall någonting gott snett på vägen kommer programmet att anslutas men en kommentar på att användaren skrivit in någonting fel
    print("Jag tror du missförstod...","\n","Försök igen med den gröna knappen")