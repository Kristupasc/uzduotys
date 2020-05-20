import check50

with open('U1.txt') as f:
    lines = f.read().split()
sk = lines[1]

@check50.check()
def exists():
  """sportas.cpp egzistuoja."""
  check50.exists("sportas.cpp")
  
@check50.check(exists)
def compiles():
    """sportas.cpp kompiliuojasi be klaidų."""
    check50.run("g++ sportas.cpp -lcrypt -lcs50 -lm -o sportas").exit(0)
   
@check50.check(compiles)
def exists_txt():
    """U1.txt egzistuoja."""
    check50.exists("U1.txt")
   
@check50.check(compiles)
def exists_reztxt():
    """U1rez.txt egzistuoja."""
    check50.exists("U1rez.txt")
    
@check50.check(exists)
def test0():
    """Informacija faile U1.txt yra surašyta teisingai"""
    if not lines:
        raise check50.Failure("U1.txt yra tusčias")
    if len(lines) < 4:
        raise check50.Failure("U1.txt yra užrašytas neteisingai.")
        
@check50.check(exists)
def test1():
    """Informacija faile U1rez.txt yra išvedama teisingai"""
    check50.run("> U1rez.txt").exit(0)
    check50.run("./aliejus").exit(0)
    #with open('U1rez.txt') as f1:
        #linesRez = f1.read().split()
    #eilutes = 2 + sk
    #if not linesRez:
        #raise check50.Failure("U1rez.txt yra tusčias")
    #if len(linesRez) != eilutes:
        #raise check50.Failure(lines[2])
 
@check50.check(compiles)
def test2():
    """Gaunamas teisingas atsakymas pagal 1 pavyzdį"""
    check50.run("> U1.txt").exit(0)
    duomenys = open("U1.txt","w")
    L = ["6 \n", "Petras A. Petraitis 213 15 20 00 \n", "Jurgis Jurgutis 221 16 12 12 \n", "Rima Joana 115 15 15 59 \n",
         "Zigmas Nosis 256 16 23 9 \n", "Roma Liepa 111 15 15 15 \n", "Rytis Uosis Ainis 255 16 23 9 \n", "5 \n", 
         "256 16 43 15 5 5 5 5 \n", "213 15 50 10 4 0 5 3 \n", "111 16 5 35 5 4 \n", "255 16 55 59 5 4 3 1 \n", "115 16 42 22 2 5 \n"]
    duomenys.writelines(L)
    duomenys.close()
    check50.run("> U1rez.txt").exit(0)
    check50.run("./sportas").exit(0)
    with open("U1rez.txt") as m:
        rez = m.read().split()
    ats = ["Merginos", "111", "Roma", "Liepa", "0", "51", "20", "115", "Rima", "Joana", "1", "29", "23",
           "Vaikinai", "256", "Zigmas", "Nosis", "0", "20", "6", "213", "Petras", "A.", "Petraitis",
           "0", "38", "10", "255", "Rytis", "Uosis", "Ainis", "0", "39", "50"]
    if ats == rez:
        pass
    else:
        raise check50.Failure("Atsakymas neteisingas")
