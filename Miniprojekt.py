import random
import time
import math

poäng=0
ett=0
x=0
två=0
i=0
n=0

spela = True

def svar(val,alternativ):
    global ett
    global två
    global x
    if val == alternativ:
        if alternativ=="1":
            ett += 1
        elif alternativ=="2":
            två += 1
        elif alternativ== "X" or "x":
            x += 1

def fruktfrågor():
    fruktkopia = fruktenskaper
    z = fruktkopia.pop(random.randint(0,len(fruktkopia)-1))
    print(z)
    b=input("\n >").upper()
    svar(b,"1")
    svar(b,"X")
    svar(b,"2")

def res1(var,frukt):
    if var >= 5:
        print("Du är en",frukt)

def res2(var1,var2,frukt):
    if var1 >= 4 and var2 >=2 or var2 >= 4 and var1 >= 2:
        print ("Du är en",frukt)

def res3(var1,var2,var3):
    if var1 == var2 or var1 == var3 or var2 == var3:
        print('Du är en lurig en... Du är en hel fruktsallad!')

def poängen(gissa,svar):
    global poäng
    if gissa == svar:
        poäng += 1
        print("Rätt! Grattis, du fick en poäng :D \n")
    else:
        print('Tyvärr, fel svar :/ Rätt svar var',svar,'\n')

def frågorna():
    kopia = frågor
    a = kopia.pop(random.randint(0,len(kopia)-1))
    frågan = a[0]
    svaret = a[1]
    print(frågan)
    f = input('>').upper()
    poängen(f,svaret)

fruktenskaper = [
    "\n \n En varm sommardag föredrar jag... \n 1) att ligga ute och jäsa i solen \n X) att vara innomhus i den sköna skuggan \n 2) att ligga i (jord)källaren och vänta på bättre tider",
    "\n \n Jag tycker bäst om \n 1) klara, starka färger som syns! \n X) färger som inte är så uppseendeväckande, fast fortfarande färger \n 2) svart. Eller andra jordnära färger som smälter in",
    "\n \n Jag är för det mesta... \n 1) explosiv! Bäst att ta chansen när den kommer \n X) smart. Jag prioriterar mina resurser så att de ska räcka länge \n 2) obrydd. Det brukar aldrig vara något problem att räcka till",
    "\n \n Andra beskriver ofta mig som... \n 1) speciell. Antingen älskar man mig eller så avskyr man mig \n X) ok. Ingen brukar ha någon speciell åsikt men ingen verka tycka illa om mig heller \n 2) ... Vilka andra? Folk brukar inte vara med mig om de inte måste",
    "\n \n Mitt ego säger att jag är... \n 1) söt! \n X) ofta rätt sur... \n 2) meh",
    "\n \n Jag är... \n 1) självsäker! Jag vet vem jag är och är nöjd med det \n X) ... ingen aning.... \n 2) inte direkt osäker... Men jag föredrar om jag inte syns",
    "\n \n Folk brukar kalla mig... \n 1) olika smeknamn. Jag är så speciell att de inte kan bestämma sig \n X) mitt namn?.. Vad annars? \n 2) En hel del saker som inte ska talas öppet om.. Jag blir ofta asocierad med andra.. mindre trevliga.. typer",    
]
frågor = [
    ['Vilken frukt är bäst föräldrar?','PÄRON'],
    ['Vilken grönsak är Titanic mest rädd för?','ISBERGSSALLAD'],
    ['Vilka baljväxter gör att man ser arg ut?','RÖDA LINSER'],
    ['Vad kallas en skilsmässa i Göteborg?','PÄRONSPLITT'],
    ['Vilken grönsak är mest lättskrämd?','RÄDISA'],
    ['Vilket bär svarar bäst i telefon?', 'HALLON'],
    ['Vilken grönsak är bäst mamma?','MOROT'],
    ['Vilken grönsak är bäst pappa?','PAPRIKA'],
]
fruktkopia = []
kopia = []

print("- "*18,"\n","-"*32,"\n Välkommen till Frågande Frukten!","\n","-"*32,"\n","*"*32,"\n","*"*7," "*6,"*"*7," ","*"*7,"\n","*"*6," ","*"*4," ","*"*6," ","*"*7, "\n","*"*12," ","*"*7," ","*"*7,"\n","*"*11," ","*"*8," ","*"*7,"\n","*"*10," ","*"*9," ","*"*7,"\n","*"*9," ","*"*10," ","*"*7,"\n","*"*32,"\n","*"*9," ","*"*10," ","*"*7,"\n","*"*32,"\n","-"*32,"\n"," "*7,"Vill du spela?!","\n"," "*6,"~"*17,"\n"," "*7,">Ja"," "*6,">Nej","\n","-"*32)
a=input(">").upper()

try:
    if a == "JA":
        while spela == True: 
            print("Vad vill du spela?","\n a) 'Min inre frukt'" "\n b) 'Fruktastiska frågor'","\n \n Skriv 'a' eller 'b'")
            d =input(">").upper()
            
            if d == "A":
                print("Vad frukt-ansvärt roligt!","\n Här kommer spelet;")
                time.sleep(1)   
                print("\n \n","Vad stämmer bäst in på dig?")
                while n < 7:
                    fruktfrågor()
                    n += 1    
                res1(ett,'Drakfrukt!')
                res1(x,'Äpple!')
                res1(två,'Potats!')
                res2(ett,x,'Apelsin!')
                res2(ett,två,'Tomat!')
                res2(x,två,'Morot!')
                res3(ett,x,två)
                time.sleep(1)
                print('\n Vad vill du göra nu?!')
                time.sleep(1)
                print('Vill du fortsätta eller sluta spela?!',"\n a) 'Fortsätta'" "\n b) 'Sluta spela'","\n \n Skriv 'a' eller 'b'")
                e =input(">").upper()
                if e == "B":
                    print('Okejdå, ses snart igen!')
                    time.sleep(2)
                    spela = False
                elif e == "A":
                    print('Vad kul!')
                    time.sleep(1)           
            
            elif d == "B":
                print("Vad banannars skulle du vilja?!", '\n Du kommer att få frågor och så svarar du den frukt, grönsak eller liknanade som du tror är rätt!','\n Ps. Stavning är viktigt så check den innan du svarar :P')
                time.sleep(2)
                print('\n Första frågan;','\n')
                while i < 8:
                    frågorna()
                    i +=1
                if poäng < 4:
                    print('Du fick',str(poäng),'rätt, det var iaf ett bra försök!')
                else:
                    print('Du fick',str(poäng),'rätt, bra jobbat!')
                time.sleep(1)
                print('\n Vad vill du göra nu?!')
                time.sleep(1)
                print('Vill du fortsätta eller sluta spela?!',"\n a) 'Fortsätta'" "\n b) 'Sluta spela'","\n \n Skriv 'a' eller 'b'")
                e =input(">").upper()
                if e == "B":
                    print('Okejdå, ses snart igen!')
                    time.sleep(2)
                    spela = False
                elif e == "A":
                    print('Vad kul!')
                    time.sleep(1)
            
            else:
                raise KeyboardInterrupt
    
    elif a == "NEJ":
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
    
    else:
        raise KeyboardInterrupt

except KeyboardInterrupt:
    print("Jag tror du missförstod...","\n","Försök igen med den gröna knappen")