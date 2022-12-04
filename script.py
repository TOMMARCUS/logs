# run this in any directory
# add -v for verbose
# get Pillow (fork of PIL) from
# pip before running -->
# pip install Pillow

# import required libraries
import os
import sys
from PIL import Image

# define a function for
# compressing an image
def compressMe(file, verbose = False):
	
	# Get the path of the file
	print(file)
	#filepath = os.path.join(os.getcwd(),file)
	#print(filepath)
			
	
	# open the image
	picture = Image.open("E:/Pins/"+file)
	
	# Save the picture with desired quality
	# To change the quality of image,
	# set the quality variable at
	# your desired level, The more
	# the value of quality variable
	# and lesser the compression
	picture.save("E:/Pins/Compressed_"+file,
				"JPEG",
				optimize = True,
				quality = 10)
	return

# Define a main function
def main():
	
	verbose = False
	
	# checks for verbose flag
	if (len(sys.argv)>1):
		
		if (sys.argv[1].lower()=="-v"):
			verbose = True
					
	# finds current working dir
	cwd = "E:\Pins"
	#path = "This PC/realme 8/Internal shared storage/DCIM/Camera"
	print(cwd)
	formats = ('.jpg', '.jpeg')
	
	# looping through all the files
	# in a current directory
	for file in os.listdir(cwd):
		print(file)
		# If the file format is JPG or JPEG
		if os.path.splitext(file)[1].lower() in formats:
			print('compressing', file)
			compressMe(file, verbose)

	print("Done")

# Driver code
if __name__ == "__main__":
	main()








"""import os

path ="E:/"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))

#print all the file names
for name in filelist:
	print(name)
"""

'''import os

def listdirs(rootdir):
	for file in os.listdir(rootdir):
		d = os.path.join(rootdir, file)
		if os.path.isdir(d):
			print(d)
			listdirs(d)

rootdir = "E:/"
listdirs(rootdir)
'''