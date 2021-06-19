# simple tip claculator
def tip(total, percentage):
  tip_total = (total * percentage) / 100
  return tip_total
  
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0