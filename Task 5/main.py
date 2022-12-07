# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos

# sugaisau su sita uzduotimi ilgaiu nei norejau/tikejausi :D
from modules.math.division import division as divivsion
from modules.math.subtraction import substraction
from modules.math.multiplication import multiplication
from modules.math.composition import composition as addition

# zemiau importuoju one by simply del code editoriaus warnings
# from modules.numbers.numbers import *

from modules.numbers.numbers import one
from modules.numbers.numbers import two
from modules.numbers.numbers import three
from modules.numbers.numbers import four
from modules.numbers.numbers import five

# Kitų failų ir žemiau esančio kodo nekeiskite
a = addition(one, four)
b = divivsion(four, two)
c = substraction(three, two)
d = multiplication(five, two)

print(a)
print(b)
print(c)
print(d)
