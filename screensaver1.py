from random import *
import win32gui
import win32api

# variable for memory
dc = win32gui.GetDC(0)

def rainbowGenerator():
	# CREATES A RAINBOW ARRAY

	colors = []

	# green emerges on top of red
	for i in range(256):
		newColor = win32api.RGB(255, i, 0)
		colors.append(newColor)

	# red diminishes before green
	for i in range(1, 256):
		newColor = win32api.RGB(255 - i, 255, 0)
		colors.append(newColor)

	# blue emerges on top of green
	for i in range(1, 256):
		newColor = win32api.RGB(0, 255, i)
		colors.append(newColor)

	# green diminishes before blue
	for i in range(1, 256):
		newColor = win32api.RGB(0, 255 - i, 255)
		colors.append(newColor)

	return colors

def colorGenerator():
	# GENERATES AN ARRAY OF COLORS

	rainbowColors = rainbowGenerator()
	randomColors = []
	for i in range(len(rainbowColors)):
		r = randint(0,255)
		g = randint(0,255)
		b = randint(0,255)
		rgb = win32api.RGB(r,g,b)
		randomColors.append(rgb)
	
	# There is a 1% chance that the screen will be a rainbow palette
	random = randint(1,100)
	if (random == 1):
		colors = rainbowColors
	else:
		colors = randomColors
	
	# add a reversed list (without first and last index) to current list
	for i in range(1,1020):
		colors.append(colors[i*-1])
	
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

			win32gui.SetPixel(dc, i, j, color)
	
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