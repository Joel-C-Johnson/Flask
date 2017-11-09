import glob, os
path1 = '/home/joel/Documents/flask/head'
path2 = '/home/joel/Documents/flask/content'
dir1 = os.chdir(path1)
dir2 = os.chdir(path2)
listdir1 = []
listdir2 = []

for files in glob.glob("*.py"):
	listdir1.append(files)

for files in glob.glob("*.py"):
	listdir2.append(files)

for i in range(0,len(listdir1)):
	txt1 = listdir1[1]
	f1 = open(txt1)
	f1_contents = f1.read()
	f1.close()
	#print txt1
	for i in range(0,len(listdir2)):
		txt2 = listdir2[1]
		#fo2 =open("txt2","w")
		f2 = open(txt2)
		f2_contents = f2.read()
		f2.close()

		f3 = open("concatenated.txt", "w")
		f3.write(f1_contents + "\n" +  f2_contents)
		f3.close()





"""
f1 = open("file1.txt")
f1_contents = f1.read()
f1.close()

f2 = open("file2.txt")
f2_contents = f2.read()
f2.close()

f3 = open("concatenated.txt", "w") # open in `w` mode to write
f3.write(f1_contents + f2_contents) # concatenate the contents
f3.close()
"""
