e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
f2e = {}
for eng, fre in e2f.items():
    f2e[fre] = eng
print(f2e)

print(set(e2f.keys()))
