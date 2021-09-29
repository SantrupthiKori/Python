
words = ['cat', 'window', 'defenestrate']
for w in words:
  print(w, len(w))

words = ['cat', 'window', 'defenestrate','evaluation']
for w in words[2:]:
  if len(w) > 6:
     words.insert(0, w)
     print(w, len(w))

