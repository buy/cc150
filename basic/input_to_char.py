"""
2:48
@author Chang Liu
@Python 2.7

User inputs a sequence of digits. Every digit is a keystroke, that is equivalent to some character out of a sequence of characters. Digit zero and five mean NULL. The table is given below 
0 - NULL 
1 - v, t, f, r, q 
2 - f, t, k 
3 - w, z, b, g 
4 - r, s 
5 - NULL 
6 - f, i, r 
7 - p 
8 - l, o 
9 - p 

Generate all possible character sequence for a given sequence of digits. 
Ex - If the user input 9801, your program should generate 
{plv, plt, plf, plr, plq, pov, pot, pof, por, poq} (not necessarily in this order). 

This problem is somewhat similar to the SMS problem. It basically boils down to generating a cartesian product of the character sets corresponding to keys.
"""

class InputsToChar(object):
  def __init__(self, inputs):
    if inputs is None:
      print 'Invalid Inputs!'
      raise SystemExit

    inputs = str(inputs)
    inputs = inputs.replace('0', '')
    inputs = inputs.replace('5', '')
    self.inputs = inputs
    self.charArray = [None, 'vtfrq', 'ftk', 'wzbg', 'rs', None, 'fir', 'p', 'lo', 'p']
    self.result = []
    
  def printAll(self, pos = 0):
    

    
    
if __name__ == '__main__':
  input = InputsToChar(9801)
  input.printAll()
