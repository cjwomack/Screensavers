import pyautogui
import win32gui
import win32api
import time

# variable for memory
dc = win32gui.GetDC(0)

# screen resolution variables (full HD)
x = 1920
y = 1080

def distributeColor():
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
	
	# add a reversed list (without first and last index) to current list
	for i in range(1,1020):
		colors.append(colors[i*-1])
	
	return colors

def snapshot():
	# CAPTURES THE CURRENT SCREEN

	# HOW TO USE:
	# The returned list contains x amount of lists, where x is the number of pixel columns. 
	# Those lists contain y amount of lists, where y is the number of pixel rows. 
	# Those lists contain the RGB value as index 0, x value as index 1, and y value as index 2. 

	image = []
	# for each column of pixels, add a list that contains data on the row of those column of pixels.
	for i in range(x):
		ylist = []
		for j in range(y):
			temp = []
			pixel = win32gui.GetPixel(dc,x,y)
			temp.append(pixel)
			temp.append(i)
			temp.append(j)
			ylist.append(temp)
		image.append(ylist)
	return(image)

def errorCover():
	# COVERS SCREEN IN AN ERROR-LIKE RAINBOW PALETTE

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

def screenRecover():
	# RECOVERS SCREEN FROM ERROR PALETTE

	for x in image:
		for pixelData in x:
			# check snapshot() description to understand index values
			win32gui.SetPixel(dc, pixelData[1], pixelData[2], pixelData[0])
	
def main():

	# create a rainbow array
	colors = distributeColor()
	
	# capture current screen state
	image = snapshot()

	while(True):
		# cover screen in error
		errorCover()

		# recover screen from error
		screenRecover()	

if __name__ == "__main__":
    main()