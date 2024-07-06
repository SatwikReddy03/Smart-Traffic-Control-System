import tensorflow as tf
import os
import numpy as np

def tensorflow_pred(image_path):
    # Suppress TF log-info messages - remove to display TF logs 
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() 
                    for line in tf.io.gfile.GFile("pretrained_labels.txt")]

    try:
        graph = tf.Graph()
        with graph.as_default():
            # Unpersists graph from file
            with tf.io.gfile.GFile("pretrained_graph.pb", 'rb') as f:
                graph_def = tf.compat.v1.GraphDef()  # For TensorFlow 2.x compatibility
                graph_def.ParseFromString(f.read())
                _ = tf.import_graph_def(graph_def, name='')

        with tf.compat.v1.Session(graph=graph) as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

            predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            for node_id in top_k:
                congestion_type = label_lines[node_id]
                score = predictions[0][node_id]
                if score >= 0.5:
                    return congestion_type, score

    except tf.errors.InvalidArgumentError:
        pass
        #print('Poor image quality, unable to predict')

#print(tensorflow_pred(r'C:\Users\satwi\OneDrive\Desktop\IOT Project\input_data\Aut10_015.jpg'))
