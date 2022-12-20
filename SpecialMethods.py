class CD:
    def __init__(self, songwriter, title, songs):
        self.songwriter = songwriter
        self.title = title
        self.songs = songs

    def __str__(self):
        return f'Album: {self.title} by {self.songwriter}'

    def __len__(self):
        return self.songs

    def __del__(self):
        print(self.__str__()+" has been deleted")


mycd = CD("Pink Floyd", "The Wall", 24)
print(mycd)
print(len(mycd))
del mycd
