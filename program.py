import ast
import random

g = open('songlist.txt', 'r')
with g as document:
    for line in document:
        songlist = line
    g.close()

songlist = ast.literal_eval(songlist) #convert dictionary in the form of string to dictionary

def addartist(artist,artistsong):
	artist = str(artist)
	artist = artist.replace(" ","")
	artist = artist.lower()
	if artist in songlist:
		message = 'Artist in database. Press Q to quit.'
		return message
	if artist not in songlist:
		artistsong = StringVar()
		artistsong = str(artistsong)
		songlist.update({artist:artistsong})
		success = 'You have successfully added an artist!'
		return success
	f = open('songlist.txt','w+')
	f.write(str(songlist))
	f.close()

def searchsongs(artist):
	artist = str(artist)
	artist = artist.replace(" ","")
	artist = artist.lower()
	if artist in songlist:
		return songlist[artist]
	else:
		message = ('Artist not in database. Press Q to quit.')
		return message

def addsongs(artist,artistsong):
	artist = str(artist)
	artist = artist.replace(" ","")
	artist = artist.lower()
	if artist in songlist:
		listofartistsong = songlist[artist]
		if artistsong not in listofartistsong:
			listofartistsong.append(artistsong)
			songlist.pop(artist)
			songlist.update({artist:listofartistsong})
			f = open('songlist.txt','w+')
			f.write(str(songlist))
			f.close()
			success = 'You have successfully added a song.'
			return success
	else:
		message = ('Artist not in database. Press Q to quit.')
		return message

def randomizer(artist):
	artist = artist.replace(" ","")
	artist = artist.lower()
	if artist in songlist:
		song = random.choice(songlist[artist])
		return song
	else:
		message = ('Artist not in database. Press Q to quit.')
		return message

#Source Codes:
#https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
#https://www.guru99.com/python-dictionary-beginners-tutorial.html#3
#https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-filex