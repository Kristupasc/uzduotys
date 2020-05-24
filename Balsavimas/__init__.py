import check50

with open('U1.txt') as f:
    lines = f.read().split()
k = lines[0] + 2

@check50.check()
def exists():
  """balsavimas.cpp egzistuoja."""
  check50.exists("balsavimas.cpp")
  
@check50.check(exists)
def compiles():
    """balsavimas.cpp kompiliuojasi be klaidų."""
    check50.run("g++ balsavimas.cpp -lcrypt -lcs50 -lm -o balsavimas").exit(0)
   
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
      raise check50.Failure("U1.txt yra užrašytas neteisingai.")
