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
        if(len(linesRez) < 1):
            raise check50.Failure("File U1rez.txt nepakanka duomenų")
        else:
            if (linesRez[0] == 2):
                pass
            else:
                raise check50.Failure("Blogai suskaičiuotas ispilstytas aliejus")
