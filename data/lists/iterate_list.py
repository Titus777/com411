def directions():
  directions = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions
def menu():
  print("Please select a direction :")
  ways = directions()
  for index in range(len(ways)):
    print("{} : {}" .format(index,ways[index]))

def run() :
  menu()
run()