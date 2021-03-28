from PIL import Image

import sys

def main():
	# try:

	image = Image.open(sys.argv[1])
	converted_image = image.convert('RGB')

	converted_image.save("converted_image.pdf")

	# except:
	# 	print("Could not process image. Please Retry")





if __name__ == '__main__':
	main()