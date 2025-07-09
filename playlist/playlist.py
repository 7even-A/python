playlist = ["MLK","4 Wheeler","Indiana Jones","Hong Kong","Put the money in the bag"]

print(playlist)
print(playlist[0])
print(playlist[-1])

playlist.append("Kai Cenat Barber")
playlist.remove("Put the money in the bag")
playlist.insert(1, "Fredrick Douglas")
playlist[-1] = "Family Distrack Pt.1"

print(playlist)

for song in enumerate(playlist):
    print(song)

