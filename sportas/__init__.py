import check50

with open('U1.txt') as f:
    lines = f.read().split()
    
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
        raise check50.Failure("file U1.txt yra tusčias")
    if len(lines) != 1:
        raise check50.Failure("file U1.txt turi būti įrasytas vienas skaicius")
        
@check50.check(compiles)
def test1():
    """Teisingai įrašyta į rezultatus"""
    check50.run("> U1rez.txt").exit(0)
    check50.run("./sportas").exit(0)
    with open('U1rez.txt') as f1:
        linesRez = f1.read().split()
        if(len(linesRez) != 1):
            raise check50.Failure("File U1rez.txt nepakanka duomenų")
        else:
            if (linesRez[0] == "2"):
                pass
            else:
                raise check50.Failure("Neteisingas numeris")
                
@check50.check(exists)
def test2():
    """Gaunamas teisingas atsakymas pagal 1 pavyzdį"""
    check50.run("> U1rez.txt"_).exit(0)
    duomenys = open("U1.txt","w")
    #L = ["6 \n", "Petras A. Petraitis 213 15 20 00 \n", "Jurgis Jurgutis 221 16 12 12 \n", "Rima Joana 115 15 15 59 \n",
         #"Zigmas Nosis 256 16 23 9 \n", "Roma Liepa 111 15 15 15 \n", "Rytis Uosis Ainis 255 16 23 9 \n", "5 \n", 
         #"256 16 43 15 5 5 5 5 \n", "213 15 50 10 4 0 5 3 \n", "111 16 5 35 5 4 \n", "255 16 55 59 5 4 3 1 \n", "115 16 42 22 2 5 \n"]
    duomenys.write("Hello")
    duomenys.close()
    file = open("U1.txt", "r+")
    raise check50.Failure(file.read())
