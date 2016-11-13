
# NOTE: this is tf code that takes a dataset as a set of filenames and trains a model on it
# This is basic format for the code, so we need to add our own data and get it to work
from os import listdir
from os.path import isfile, join
import tensorflow as tf

mypath = '/Users/Ruta/Developer/calhacks3/asltov/imageRecogData'

# step 1
filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("Finished step 1")

# step 2
filename_queue = tf.train.string_input_producer(filenames)
print("Finished step 2")

# step 3: read, decode and resize images
reader = tf.WholeFileReader()
filename, content = reader.read(filename_queue)
print("Read the filename queue")

my_img = tf.image.decode_png(content) # use png or jpg decoder based on your files.
print("Decoded images")

init_op = tf.initialize_all_variables()
print("Initialized all vars")
sess = tf.Session()
with sess.as_default():
    sess.run(init_op)
    print("Ran the init op")
    # Start populating the filename queue.
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    print("Started populating filename queue")

    for i in range(10): #length of your filename list
        print("Evaluating image #" + str(i))
        image = my_img.eval() #here is your image Tensor :)

    print(image.shape)
    Image.show(Image.fromarray(np.asarray(image)))

    coord.request_stop()
    coord.join(threads)

# image = tf.image.decode_jpeg(content, channels=3)
# image = tf.cast(image, tf.float32)
# resized_image = tf.image.resize_images(image, 224, 224)
# images.append(resized_image)
#
# print("Finished step 3")
#
# # step 4: Batching
# image_batch = tf.train.batch(images, batch_size=8)
# print("Finished step 4")
