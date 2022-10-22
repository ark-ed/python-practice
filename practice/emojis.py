# Text to emoji
# .get(keyname, value) -- keyname (required) value (optional, used for returning a value if keyname does not exist)

emojis = {
  ":)" : "🙂",
  ":/" : "😐",
  ":(" : "😔",
  ":D" : "😀",
  ">:(" : "😡"
}

def e():
  a = input(">")
  b = a.split(" ")
  output = ""
  
  for x in b:
    output = output+emojis.get(x,x) + " "
  
  print(output)

while True:
  #os.system('clear')
  e()