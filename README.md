# match
match an obj with a pattern or a list of patterns
 
If the Obj is the string, do fnmatch with the Pattern or the element in the Pattern if the Pattern is iterable
 
if the Obj is not the string, check if the Obj is the Pattern or in the Pattern

Examples:

from match import match

>>> match(‘abc’, ‘def)
False

>>> match(‘abc’, ‘abc)
True

>>> match(‘abc’, [‘ab*’, ‘def]
True

>>> match (1, [‘1’, 2, 3]
False

>>> match (1, [1, 2, 3]
True
