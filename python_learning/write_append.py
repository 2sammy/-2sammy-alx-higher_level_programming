from posixpath import split


writeMe = "nice text"
saveFile = open("niceWrite.txt","w")
saveFile.write(writeMe)
saveFile.close()

#appending a file
appendMe = "some file"
saveFile = open("someFile.txt","a")
saveFile.write(appendMe)
saveFile.close()

#reading a file
#readMe= "sammy"
readMe = open("someFile.txt","r").read()
#saveFile.read()
print(readMe)
splitMe = readMe.split("\n")
print(splitMe[0])

readMe2 = open("someFile.txt","r").readlines
print(readMe2)

