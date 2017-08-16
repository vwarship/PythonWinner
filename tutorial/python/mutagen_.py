from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3

filename = 'test.mp3'

mp3 = MP3(filename)
print(mp3.pprint())

id3 = ID3(filename)
print(id3.pprint())

id3 = EasyID3(filename)
for key in id3.keys():
    id3[key] = ''
# id3.delete()
print(id3)
id3.save()
