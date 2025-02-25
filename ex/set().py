p1 = {'Urano','Netuno','Terra', 'Marte'}
p2 = {'Marte', 'Saturno', 'Jupiter', 'Lua','Eris'}
p3 = {'Sol', 'Mercurio', 'Venus', 'Lua'}
p4 = p1.copy()
intersecion = p1 & p2 #or p1.intersection(p2)
union = p1 | p2 #or p1.union(p2)
diff = p1 - p2 #or p1.difference(p2)z
sym_diff = p1 ^ p2 #or p1.symmetric.difference(p2)
print(f'Intersecção entre {p1} e {p2}:\n {intersecion}\n União: {union}\n Diferença: {diff}\n Diferença simétrica: {sym_diff} ')
print(p2.isdisjoint(p3))
p4.add('Jupiter')
p4.add('Jupiter')#repetido
p4.remove('Jupiter')
p4.discard('Lua')
print(p4.pop())
p1.clear() # clear
print(p1.issubset(p4))#p1 <= p4
print(p4.issubset(p1)) #p4 <= p1
print(p1.issuperset(p4))#p1 >= p4
print(p4.issuperset(p1)) #p4 >= p1
