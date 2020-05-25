import check50

with open('U1.txt') as f:
    lines = f.read().split()
k = int(lines[0]) + 2
@check50.check()
def exists():
  """balsavimas.cpp egzistuoja."""
  check50.exists("balsavimas.cpp")

@check50.check(exists)
def compiles():
    """balsavimas.cpp kompiliuojasi be klaidų."""
    check50.run("g++     balsavimas.cpp  -lcrypt -lcs50 -lm -o balsavimas").exit(0)
   
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
    if len(lines) < k:
        raise check50.Failure("U1.txt yra užrašytas neteisingai.")
    elif len(lines) > k:
        raise check50.Failure(k)

@check50.check(compiles)
def test1():
    """Informacija faile U1rez.txt yra išvedama teisingai"""
    check50.run("> U1rez.txt").exit(0)
    check50.run("./sportas").exit(0)
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
def pvz1():
    """Gaunamas teisingas atsakymas pagal 1 pavyzdį"""
    check50.run("> U1.txt").exit(0)
    duomenys = open("U1.txt","w")
    L = ["6 \n", "15 10 22 \n", "15 40 13 \n", "23 26 26 \n", "110 30 58 \n", "33 33 32 \n", "0 56 0 \n", "2 1 3 \n"]
    duomenys.writelines(L)
    duomenys.close()
    #check50.run("> U1rez.txt").exit(0)
    #check50.run("./sportas").exit(0)
    with open("U1rez.txt") as m:
        rez = m.read().split()
    ats = ["196", "195", "151", "6", "12", "6", "2"]
    if ats == rez:
        pass
    else:
        raise check50.Mismatch(ats, rez)
      
