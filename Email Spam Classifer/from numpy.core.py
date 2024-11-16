import cv2
import numpy as np
from PIL import Image

def main(image):
    # check type of array
    print(type(image))

    # show the shape of the array
    print(image.shape)

    # creating image object from array
    data = Image.fromarray(image)

    # saving the final output as a PNG file
    data.save('gfg_dummy_pic.png')

# driver code
if __name__ == "__main__":
    img = np.asarray(Image.open("C:\\Users\\ASUS\\Desktop\\Average-anterior-upper-body-maps-of-absolute-skin-temperature-patterns-after-40-minutes.jpg"))
    # function call
    main(img)
import cv2
import numpy as np
from PIL import Image

def main(image):
    # check type of array
    print(type(image))

    # show the shape of the array
    print(image.shape)

    # creating image object from array
    data = Image.fromarray(image)

    # saving the final output as a PNG file
    data.save('gfg_dummy_pic.png')

# driver code
if __name__ == "__main__":
    img = np.asarray(Image.open("C:\\Users\\ASUS\\Desktop\\Average-anterior-upper-body-maps-of-absolute-skin-temperature-patterns-after-40-minutes.jpg"))
    # function call
    main(img)
