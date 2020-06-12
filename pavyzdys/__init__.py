# Šis file yra vykdomas, kai veikia check50 komanda (užduoties tikrinimas)
# Kodas yra rašomas Python kalba.
# Štai yra pavyzdinis kodas, kuris patikrina ar egzistuoja visi failai, ar duomenų failas yra surašytas teisingai,
# ar rezultatų faile yra išvesta teisinga informacija ir patikrinimas, ar gaunamas teisingas atsakymas pagal du pavyzdžius.
# žodžius balsavimas ir uzduotis pakeiskite į savo užduoties pavadinimą.

import check50 # importuojama check50 aplinka.

# funkcijos iki test0 veikia visuose uždaviniuose, tik reikia pakeisti uzduotis.cpp į savo užduoties failo pavadinimą.

@check50.check() # vykdoma check funkcija
def egzistuoja(): # egzistuoja yra funkcijos pavadinimas, jį galima keisti
  """uzduotis.cpp egzistuoja.""" # šis tekstas bus išvedamas jeigu nebus klaidų
  check50.exists("uzduotis.cpp") # Vykdoma funkcija, kuri patikrina, ar failas uzduotis.cpp egzistuoja
  # jeigu egzistuoja, tada išvedamas tekstas, kuris yra parašytas funkcijos pradžioje (uzduotis.cpp egzistuoja)

@check50.check(egzistuoja) # ši funkcija veikia tik tada jeigu funkcija pavadinimu egzistuoja veikia.
def kompiliuojasi(): # kompiliuojasi yra funkcijos pavadinimas, jį galima keisti
    """uzduotis.cpp kompiliuojasi be klaidų.""" # šis tekstas bus išvedamas jeigu programa kompiliuosis be klaidų
    check50.run("g++     uzduotis.cpp  -lcrypt -lcs50 -lm -o uzduotis").exit(0) # tikrina, ar pasileidžia programa (tas pats kaip
    # per code blocks paspausti F9).
   
@check50.check(kompiliuojasi) # funkcija veikia tik tada, jeigu failas kompiliuojasi.
def egzistuoja_Duomenys(): # egzistuoja_Duomenys yra funkcijos pavadinimas, jį galima keisti
    """Duomenys.txt egzistuoja.""" # ši funkcija veikia tik tada jeigu Duomenų failas egzistuoja.
    check50.exists("Duomenys.txt") # tikrinama, ar egzistuoja Duomenys.txt failas sistemoje.
   
@check50.check(kompiliuojasi) # funkcija veikia tik tada, jeigu failas kompiliuojasi.
def egzistuoja_Rezultatai(): # egzistuoja_Rezultatai yra funkcijos pavadinimas, jį galima keisti
    """Rezultatai.txt egzistuoja.""" # ši funkcija veikia tik tada jeigu Rezultatų failas egzistuoja.
    check50.exists("Rezultatai.txt") # tikrinama, ar egzistuoja Rezultatai.txt failas sistemoje.
    
@check50.check(kompiliuojasi) # funkcija veikia tik tada, jeigu failas kompiliuojasi.
def test0(): # tai yra pirmasis testas, kuris skirsis priklausant nuo uždavinio.
  # Kai kuriuose uždaviniuose Duomenų faile gali būti skirtingas kiekis eilučių. Tada reikia rašyti labiau komplikuotą kodą,
  # arba tiesiog ištrinti šią funkciją.
    """Informacija faile Duomenys.txt yra surašyta teisingai"""
    eilutes = len(open("Duomenys.txt").readlines()) # atidaro Duomenų failą ir nuskaito, kiek jame yra eilučių.
    eilutesAts = 0 # skaičių 0 reikia pakeisti į eilučių kiekį, kiek turi būti duomenų faile.
    if not eilutes: #jeigu duomenų failė nėra eilučių (jis tuščias)
        raise check50.Failure("Duomenys.txt yra tusčias") # Išvedama, jog duomenų failas yra tuščias. Tolesnės eilutės nebėra skaitomos.
    if eilutes != eilutesAts: # tikrinama, ar eilučių kiekis nėra lygus teisingu eilučių kiekiu.
        raise check50.Failure("Duomenys.txt yra užrašytas neteisingai.") # Išvedama, jog duomenų failas yra užrašytas neteisingai.
# jeigu funkcija nuėjo iki šios vietos be jokių trugdžių, funkcija išveda: Informacija faile Duomenys.txt yra surašyta teisingai.

@check50.check(kompiliuojasi) # funkcija veikia tik tada, jeigu failas kompiliuojasi.
def test1():
  # Kai kuriuose uždaviniuose Rezultatų faile gali būti skirtingas kiekis eilučių. Tada reikia rašyti labiau komplikuotą kodą,
  # arba tiesiog ištrinti šią funkciją.
    """Informacija faile Rezultatai.txt yra išvedama teisingai"""
    check50.run("./balsavimas").exit(0) # tai yra komanda, kuri yra tas pats kaip per code blocks paspaudimas F9
    eilutes = len(open("Rezultatai.txt").readlines()) # atidaro Rezultatų failą ir nuskaito, kiek jame yra eilučių.
    eilutesAts = 0 # skaičių 0 reikia pakeisti į eilučių kiekį, kiek turi būti rezultatų faile.
    if not eilutes: #jeigu rezultatų failė nėra eilučių (jis tuščias)
        raise check50.Failure("U1rez.txt yra tusčias") # Išvedama, jog rezultatų failas yra tuščias. Tolesnės eilutės nebėra skaitomos.
    if eilutes != eilutesAts: # tikrinama, ar eilučių kiekis nėra lygus teisingu eilučių kiekiu.
        raise check50.Failure("U1rez.txt išvedė per daug eilučių.") # Išvedama, jog rezultatų failas yra užrašytas neteisingai.
# jeigu funkcija nuėjo iki šios vietos be jokių trugdžių, funkcija išveda: Informacija faile Rezultatai.txt yra išvedama teisingai.
        
@check50.check(kompiliuojasi)
def pvz1():
    """Gaunamas teisingas atsakymas pagal pirmą pavyzdį"""
    check50.run("> Duomenys.txt").exit(0) # ištrinamas Duomenys.txt failas, kad galėtume įrašyti savo duomenis.
    duomenys = open("Duomenys.txt","w") # Atidaromas Rezultatai.txt failas, kad galėtume į jį rašyti duomenis.
    L = ["3 \n", "20 20 20 \n", "17 99 21 \n", "0 13 14 \n", "1 2 3 \n"] # L yra masyvas, kuriame yra visa duomenų informacija.
#pvz. jeigu duomenys yra:
#6
#15 10 22
#15 40 13
#23 26 26
#110 30 58
#33 33 32
#0 56 0
#2 1 3
#tada L = ["6 \n", "15 10 22 \n", "15 40 13 \n", "23 26 26 \n", "110 30 58 \n", "33 33 32 \n", "0 56 0 \n", "2 1 3 \n"]
    duomenys.writelines(L) # įrašoma į duomenų failą informacija L masyve.
    duomenys.close() # uždaromas duomenų failas (į jį rašyti nebereikės)
    check50.run("./balsavimas").exit(0) # tai yra komanda, kuri yra tas pats kaip per code blocks paspausti F9
    with open("Rezultatai.txt") as m: # atidaromas Rezultatai.txt failas
        rez = m.read().split() # nuskaitomas Rezultatai.txt failas ir duomenys įdedami į rez masyvą
    ats = ["37", "132", "55", "1", "6", "7", "3"] # tai yra informacija, kuri turi būti Rezultatų faile
#pvz. jeigu rezultatai turi būti:
#196 195 151
#6 12 6
#2
#tada ats = ["196", "195", "151", "6", "12", "6", "2"]
    if ats == rez: #tikrinama, ar gauti rezultatai yra tokie patys kaip rezultatai pagal pavyzdį.
        pass # niekas neįvyksta.
    else: # jeigu rezultatai nesutampa su rezultatais pagal pavyzdį
        raise check50.Mismatch(ats, rez) # Išvedama, kad nėra gautas teisingas atsakymas pagal pavyzdį ir parodyta, koks
# tūrėjo būti atsakymas, ir kokį gavo programa.

#Jeigu norite padaryti antrą patikrinimą, tik su kitais duomenimis, galima copy pastinti visą funkciją, tik pakeisti
# jos pavadinimą ir L bei ats masyvus.
