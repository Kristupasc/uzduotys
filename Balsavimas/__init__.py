import check50

with open('U1.txt') as f:
    lines = f.read().split()
    
@check50.check()
def exists():
  """balsavimas.cpp egzistuoja."""
  check50.exists("balsavimas.cpp")
