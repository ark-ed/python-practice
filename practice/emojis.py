# Text to emoji
# .get(keyname, value) -- keyname (required) value (optional, used for returning a value if keyname does not exist)


def emoji_converter(a):
  emojis = {
    ":)" : "🙂",
    ":/" : "😐",
    ":(" : "😔",
    ":D" : "😀",
    ">:(" : "😡"
  }
  
  b = a.split(" ")
  output = ""
    
  for x in b:
    output = output+emojis.get(x,x) + " "

  return output

while True:
  msg = input("> ")
  result = emoji_converter(msg)
  print(result)