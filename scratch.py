

# NOTE: this is OpenCV code we need to modify.
# It activates the webcam and starts reading frames
import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
cv2.destroyWindow("preview")


# NOTE: this is tf code that takes a dataset as a set of filenames and trains a model on it
# This is basic format for the code, so we need to add our own data and get it to work

# step 1
filenames = ['im_01.jpg', 'im_02.jpg', 'im_03.jpg', 'im_04.jpg']

# step 2
filename_queue = tf.train.string_input_producer(filenames)

# step 3: read, decode and resize images
reader = tf.WholeFileReader()
filename, content = reader.read(filename_queue)
image = tf.image.decode_jpeg(content, channels=3)
image = tf.cast(image, tf.float32)
resized_image = tf.image.resize_images(images, 224, 224)

# step 4: Batching
image_batch = tf.train.batch([resized_image], batch_size=8)



