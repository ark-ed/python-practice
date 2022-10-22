# Number to text
# Mosh's Solution

instructions = {
  "1" : "one ",
  "2" : "two ",
  "3" : "three ",
  "4" : "four ",
  "5" : "five "
}

numbers = input("-->")
output = ""
for x in numbers:
  output = output+instructions.get(x)

print(output)