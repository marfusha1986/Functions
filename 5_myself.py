play = ('Squirtle', 'Charmander', 'Pikachu', 'Bulbasaur')
for i in enumerate(play):
    print(i[0], i[1])

xan = ('water', 'fire', 'electric', 'grass')
for idx, val in enumerate(xan):
    print(idx, val)

play = xan
for i in range(len(play)):
    print(i, play[i])