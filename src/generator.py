import numpy as np
import json
import os
import matplotlib.pyplot as plt

class ImageGenerator:
    def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        self.file_path = file_path
        self.label_path = label_path
        self.batch_size = batch_size
        self.image_size = image_size
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle
        self.images = []
        self.labels = []
        self.load_data()
        self.index = 0

    def load_data(self):
        with open(self.label_path) as f:
            labels = json.load(f)
        for filename, label in labels.items():
            img = np.load(os.path.join(self.file_path, filename))
            self.images.append(img.reshape(self.image_size))
            self.labels.append(label)
        self.images = np.array(self.images)
        self.labels = np.array(self.labels)

    def next(self):
        # Implement batch generation with optional rotation and mirroring
        pass

    def show(self):
        batch_images, batch_labels = self.next()
        fig, ax = plt.subplots(1, len(batch_images), figsize=(15, 15))
        for i, img in enumerate(batch_images):
            ax[i].imshow(img, cmap='gray')
            ax[i].title.set_text(f'Label: {batch_labels[i]}')
        plt.show()

# Note: Implement the next() method to handle batch processing.




# import os.path
# import json
# import scipy.misc
# import numpy as np
# import matplotlib.pyplot as plt

# # In this exercise task you will implement an image generator. Generator objects in python are defined as having a next function.
# # This next function returns the next generated object. In our case it returns the input of a neural network each time it gets called.
# # This input consists of a batch of images and its corresponding labels.
# class ImageGenerator:
#     def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
#         # Define all members of your generator class object as global members here.
#         # These need to include:
#         # the batch size
#         # the image size
#         # flags for different augmentations and whether the data should be shuffled for each epoch
#         # Also depending on the size of your data-set you can consider loading all images into memory here already.
#         # The labels are stored in json format and can be directly loaded as dictionary.
#         # Note that the file names correspond to the dicts of the label dictionary.

#         self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
#                            7: 'horse', 8: 'ship', 9: 'truck'}
#         #TODO: implement constructor

#     def next(self):
#         # This function creates a batch of images and corresponding labels and returns them.
#         # In this context a "batch" of images just means a bunch, say 10 images that are forwarded at once.
#         # Note that your amount of total data might not be divisible without remainder with the batch_size.
#         # Think about how to handle such cases
#         #TODO: implement next method
#         pass
#         #return images, labels

#     def augment(self,img):
#         # this function takes a single image as an input and performs a random transformation
#         # (mirroring and/or rotation) on it and outputs the transformed image
#         #TODO: implement augmentation function

#         return img

#     def current_epoch(self):
#         # return the current epoch number
#         return 0

#     def class_name(self, x):
#         # This function returns the class name for a specific input
#         #TODO: implement class name function
#         return
#     def show(self):
#         # In order to verify that the generator creates batches as required, this functions calls next to get a
#         # batch of images and labels and visualizes it.
#         #TODO: implement show method
#         pass

