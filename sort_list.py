# Sort alphabetically a list of names
def sort_list():
  while True:
    changed = False
    for i in range(len(names) - 1):
      if (names[i] > names[i + 1]):
        aux = names[i]
        names[i] = names[i + 1]
        names[i + 1] = aux
        changed = True
    if not changed: break

names = []
print "Enter the names. Enter '####' to finish."
name = raw_input()

while (name != '####'):
  names.append(name)
  sort_list()
  name = raw_input()

for item in names:
  print item
