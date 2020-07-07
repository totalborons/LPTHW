# this is how classes and modules are made in here...
# basically module is one and single hand only while the classes are meant to be made new everyttime

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy Birthday to you",
                   "I dont want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


# basically a class always take self object together with it implicitly even when not passed and usually also never passed along
# this might create problems when you are creating classes always have one argument as self there apart from othere functions
