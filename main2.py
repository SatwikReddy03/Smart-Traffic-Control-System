#This is the main file

#import the required packages
import os
from density import tensorflow_pred
from time_allocation import *
from util import *
#Code

inputs=r'input_data'

while True:
    for filename in os.listdir(inputs):
        try:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                image_path = os.path.join(inputs, filename)
                o1,o2=tensorflow_pred(image_path)
                print(o1,o2)
                instance=generate_instance(o1,o2)
                time_allocated=allocate_time(o1,o2,instance)
                print(time_allocated)
                #print(filename)
        except:
            pass
    else:
        break
