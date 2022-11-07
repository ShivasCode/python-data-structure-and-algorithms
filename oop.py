class Artist:
	def __init__(self,name,age,genre):
		self.name = name 
		self.age = age
		self.genre = genre


class Artista:
	def __init__(self,name, max_artist):
		self.name = name
		self.max_artist = max_artist
		self.artists = []
	def add_artist(self,artist):
		if len(self.artists) < self.max_artist:
			self.artists.append(artist)
		else:
			print('idiot')

a1 = Artist('Joma',20,'java')

b1 = Artista('hatdog',3)

b1.add_artist(a1)

print(b1.artists)