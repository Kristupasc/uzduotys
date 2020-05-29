# Šis file yra vykdomas, kai veikia check50 komanda (tikrinimas užduoties)
# Kodas yra rašomas Python kalba.
# Štai yra pavyzdinis kodas, kuris patikrina ar egzistuoja visi failai, ar duomenų failas yra surašytas teisingai,
# ar rezultatų faile yra išvesta teisinga informacija ir patikrinimas, ar gaunamas teisingas atsakymas pagal du pavyzdžius.

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
    check50.run("./balsavimas").exit(0) # tai yra komanda, kuri yra tas pats kaip per code blocks paspausti F9
    eilutes = len(open("Rezultatai.txt").readlines()) # atidaro Rezultatų failą ir nuskaito, kiek jame yra eilučių.
    eilutesAts = 0 # skaičių 0 reikia pakeisti į eilučių kiekį, kiek turi būti rezultatų faile.
    if not eilutes: #jeigu rezultatų failė nėra eilučių (jis tuščias)
        raise check50.Failure("U1rez.txt yra tusčias") # Išvedama, jog rezultatų failas yra tuščias. Tolesnės eilutės nebėra skaitomos.
    if eilutes != eilutesAts: # tikrinama, ar eilučių kiekis nėra lygus teisingu eilučių kiekiu.
        raise check50.Failure("U1rez.txt išvedė per daug eilučių.") # Išvedama, jog rezultatų failas yra užrašytas neteisingai.
# jeigu funkcija nuėjo iki šios vietos be jokių trugdžių, funkcija išveda: Informacija faile Rezultatai.txt yra išvedama teisingai.
        
@check50.check(compiles)
def pvz2():
    """Gaunamas teisingas atsakymas pagal antrą pavyzdį"""
    check50.run("> U1.txt").exit(0)
    duomenys = open("U1.txt","w")
    L = ["3 \n", "20 20 20 \n", "17 99 21 \n", "0 13 14 \n", "1 2 3 \n"]
    duomenys.writelines(L)
    duomenys.close()
    check50.run("> U1rez.txt").exit(0)
    check50.run("./balsavimas").exit(0)
    with open("U1rez.txt") as m:
        rez = m.read().split()
    ats = ["37", "132", "55", "1", "6", "7", "3"]
    if ats == rez:
        pass
    else:
        raise check50.Mismatch(ats, rez)
