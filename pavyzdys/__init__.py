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
    
@check50.check(exists)
def test0():
    """Informacija faile U1.txt yra surašyta teisingai"""
    linesRez = len(open("U1.txt").readlines())
    if not lines:
        raise check50.Failure("U1.txt yra tusčias")
    if linesRez < k:
        raise check50.Failure("U1.txt yra užrašytas neteisingai.")
    elif linesRez > k:
        raise check50.Failure("U1.txt yra užrašytas neteisingai.")

@check50.check(compiles)
def test1():
    """Informacija faile U1rez.txt yra išvedama teisingai"""
    check50.run("> U1rez.txt").exit(0)
    check50.run("./balsavimas").exit(0)
    with open("U1rez.txt") as m:
        rez = m.read().split()
    linesRez = len(open("U1rez.txt").readlines())
    eilutes = 3
    if not linesRez:
        raise check50.Failure("U1rez.txt yra tusčias")
    if linesRez < eilutes:
        raise check50.Failure("U1rez.txt išvedė per mažai eilučių.")
    if linesRez > eilutes:
        raise check50.Failure("U1rez.txt išvedė per daug eilučių.")
        
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
