from fnmatch import fnmatch
from collections import Iterable

def __obj_match(Obj, Pattern):
  if isinstance(Pattern, Iterable):
    if isinstance(Obj, str):
      for i in Pattern:
        if fnmatch(Obj, i): return True 
      return False
    else: return Obj in Pattern
    
  else: 
    if isinstance(Obj, str): return fnmatch(Obj, Pattern)
    else: return Obj==Pattern

def match(Obj, Pattern):
  '''
  match the Obj with the Pattern,
  if the Obj is the str, do fnmatch with the Pattern or the element in the Pattern if the Pattern is iterable
  if the Obj is not the str, check if the Obj is the Pattern or in the Pattern
  '''
  if isinstance(Obj, Iterable):
    for i in Obj:
      if __obj_match(i, Pattern): return True
    else: return False
  else: return __obj_match(Obj, Pattern)