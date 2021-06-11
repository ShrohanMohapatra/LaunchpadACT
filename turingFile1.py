def turingMachine(Tape):
  for i in range(int(len(Tape)/2)):
    if Tape[i]=='a' and Tape[len(Tape)-1-i]=='b': pass
    else: return False
  return True
assert turingMachine(['a','a','a','b','b','b'])==True
assert turingMachine(['a','a','a','b','b'])==False
assert turingMachine(['a','a','b','b','b'])==False
assert turingMachine([])==True
