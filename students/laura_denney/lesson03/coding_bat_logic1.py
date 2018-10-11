def cigar_party(cigars, is_weekend):
  if is_weekend is True and cigars >= 40:
    return True
  elif cigars >= 40 and cigars <= 60:
    return True
  else:
    return False

def date_fashion(you, date):
  if you<= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1

