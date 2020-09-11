# Author: John Sweetall jts6052@psu.edu
# Collaborator: Caroline Brustoloni cxb5766@psu.edu
# Collaborator: Siddhant Rajoriya sbr5632@psu.edu
# Collaborator: Saeed Alshebli saa6016@psu.edu
# Section: 2
# Breakout: 11

def run () :
  score = float(input("Enter you CMPSC 131 grade: "))
  print(f"Your letter grade in CMPSC 131 is \
{getLetterGrade(score)}.")

def getLetterGrade(score):
  if score >= 93:
    return "A";
  elif score >= 90:
    return "A-"
  elif score >= 87:
    return "B+"
  elif score >= 83:
    return "B"
  elif score >= 80:
    return "B-"
  elif score >= 77:
    return "C+"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
