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
        

