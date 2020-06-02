from fnmatch import fnmatch
from collections import Iterable

def match(Obj, Pattern):
  '''
  match the Obj with the Pattern,
  if the Obj is the str, do fnmatch with the Pattern or the element in the Pattern if the Pattern is iterable
  if the Obj is not the str, check if the Obj is the Pattern or in the Pattern
  '''
  if isinstance(Pattern, str) or not isinstance(Pattern, Iterable):
    if isinstance(Obj, str): return fnmatch(Obj, Pattern)
    else: return Obj==Pattern
  else: 
    if isinstance(Obj, str):
      for i in Pattern:
        if fnmatch(Obj, i): return True 
      return False
    else: return Obj in Pattern