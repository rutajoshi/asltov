from tkinter import *

import numpy as np
import cv2

class MyFirstGUI:
	def __init__(self, master):
		self.master = master
		master.title("A simple GUI")

		self.label = Label(master, text="This is our first GUI")
		#self.label.pack()

		self.startVideoCapture = Button(master, text="Start", command=self.startVideo)
		#self.greet_button.pack()

		self.stopVideoCapture = Button(master, text="Stop", command=self.stopVideo)
		#self.close_button.pack()

		self.label.grid(columnspan=2)
		self.startVideoCapture.grid(row=1)
		self.stopVideoCapture.grid(row=1, column=1)

	def startVideo(self):
		cap = cv2.VideoCapture(0)

		while(True):
		    # Capture frame-by-frame
		    ret, frame = cap.read()

		    # Our operations on the frame come here
		    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		    # Display the resulting frame
		    cv2.imshow('frame',gray)
		    if cv2.waitKey(1) & 0xFF == ord('q'):
		        break

	def stopVideo(self):
		# When everything done, release the capture
		cap.release()
		cv2.destroyAllWindows()







root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()