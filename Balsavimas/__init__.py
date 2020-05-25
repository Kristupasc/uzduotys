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
        raise check50.Mismatch(ats, rez, help = "pavyzdys yra: 3 3 3 3 3")
