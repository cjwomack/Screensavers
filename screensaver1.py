from random import *
import win32gui
import win32api

# variable for memory
dc = win32gui.GetDC(0)

def rainbowGenerator():
	# CREATES A RAINBOW ARRAY

	colors = []

	# green emerges on top of red
	colors += [(255, i, 0) for i in range(256)] 

	# red diminishes before green
	colors += [(254 - i, 255, 0) for i in range(255)]

	# blue emerges on top of green
	colors += [(0, 255, i + 1) for i in range(256)]

	# green diminishes before blue
	colors += [(0, 254 - i, 255) for i in range(255)]

	return colors

def rainbowActualGenerator():
	for index in range(1021):
		if index < 256: # .. 255
			yield (255, index, 0)
		elif 256 <= index < 511: # 256 .. 510
			yield (510 - index, 255, 0)
		elif 511 <= index < 766: # 511 ... 766
			yield (0, 255, (index - 510))
		elif 766 <= index < 1021:
			yield (0, 1020 - index, 255)
			

def colorGenerator():
	# GENERATES AN ARRAY OF COLORS
        gen = rainbowActualGenerator()
	rainbowColors = [next(gen) for i in range(1021)]
	randomColors = [(randint(0,255), randint(0,255), randint(0,255)) for i in range(len(rainbowColors))]

	
	# There is a 1% chance that the screen will be a rainbow palette
	colors = rainbowColors if randint(1,100) == 1 else randomColors
	
	# add a reversed list (without first and last index) to current list
	colors += colors[:1020:-1]
	#for i in range(1,1020):
	#	colors.append(colors[i*-1])
	
	return colors

def errorCover(colors):
	# COVERS SCREEN IN AN ERROR-LIKE RAINBOW PALETTE

	# declare stuff
	x = 1919
	y = 1079
	counter = 0

	for i in range(x):
		for j in range(y):
			color = colors[counter]
			# if reaching end of list, reset counter
			if (counter < len(colors) - 1):
				counter += 1
			else:
				counter = 0

			win32gui.SetPixel(dc, i, j, win32api.RGB(*color))
	
def main():
	# Screen dimensions
	x = 1920
	y = 1080

	while(True):

		# pick color palette
		colors = colorGenerator()

		# cover screen in error
		errorCover(colors)

if __name__ == "__main__":
    main()
