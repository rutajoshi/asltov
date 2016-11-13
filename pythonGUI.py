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
		self.startVideoCapture.pack()

		# self.stopVideoCapture = Button(master, text="Stop", command=self.stopVideo)
		#self.close_button.pack()

		# self.label.grid(columnspan=2)
		# self.startVideoCapture.grid(row=1)
		# self.stopVideoCapture.grid(row=1, column=1)

		self.cap = None

	def startVideo(self):
		self.cap = cv2.VideoCapture(0)
		print("Something is happening!!!\n")
		print(self.cap)
		while(True):
			# Capture frame-by-frame
			ret, frame = self.cap.read()
			print("Ret = " + str(ret) + "\n")
			print("Frame = " + str(frame) + "\n")
			    # Our operations on the frame come here
			if frame is not None:
				cv2.imshow("preview", frame)
				rval, frame = vc.read()

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

			# if (not self.cap.isOpened()):
			# 	self.cap.open(0)
			# 	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			#
			# # Display the resulting frame
			# cv2.imshow('frame',gray)
			# if cv2.waitKey(1) & 0xFF == ord('q'):
			# 	break
		self.cap.release()
		cv2.destroyAllWindows()


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
