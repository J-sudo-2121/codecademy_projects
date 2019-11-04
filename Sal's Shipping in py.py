def ground_shipping(weight):
  if weight <= 2:
    return weight * 1.5 + 20
  elif (weight > 2) and (not weight >= 6):
    return weight * 3 + 20
  elif (weight > 6) and (not weight >= 10):
    return weight * 4 + 20
  else:
    return weight * 4.75 + 20

def drone_shipping(weight):
  if weight <= 2:
    return weight * 4.5
  elif (weight > 2) and (not weight >= 6):
    return weight * 9
  elif (weight > 6) and (not weight >= 10):
    return weight * 12
  else:
    return weight * 14.25

premium_shipping = 125

def cheapest(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_shipping
  
  if ground < premium and ground < drone :
    return "You should ship using ground shipping. It is the cheapest for you and it will cost you " + str(ground) + " dollars."
  elif drone < premium and drone < ground:
    return "You should ship using drone shipping. It is the cheapest for you and it will cost you " + str(drone) + " dollars."
  else:
    return "You should ship using premium shipping. It is the cheapest for you and it will cost you 125 dollars."

print(cheapest(30))