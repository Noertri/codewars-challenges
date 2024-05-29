def valid_braces(braces):
  sum_ord = 0

  for i in range(len(braces)):
    if braces[i] == "(" and (i+1) < len(braces) and braces[i+1] not in ["]", "}"]:
      sum_ord += ord(braces[i])
    elif braces[i] == "[" and (i+1) < len(braces) and braces[i+1] not in [")", "}"]:
      sum_ord += ord(braces[i])
    elif braces[i] == "{" and (i+1) < len(braces) and braces[i+1] not in ["]", ")"]:
      sum_ord += ord(braces[i])
    elif braces[i] == ")":
      sum_ord -= ord("(")
    elif braces[i] == "]":
      sum_ord -= ord("[")
    elif braces[i] == "}":
      sum_ord -= ord("{")
    else:
      sum_ord -= 1

  if sum_ord != 0:
    return False

  return True


print(valid_braces("()"))
