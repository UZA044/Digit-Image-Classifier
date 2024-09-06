# Image Digit Classifier

## Overview
The **Image Digit Classifier** is a machine learning project that deploy CNNs ( Convolutional Neural Networks ) to classify handwritten digit images. My project aims to accurately recognize digits (0-9) from images, showcasing a robust solution which can be further scaled to be utilized at real-world applications.

## Features
- **Data Augmentation**: Enhances training data by applying various transformations to create more robust models, allows for much more accurate predictions by the model.
- **Interactive GUI**: Allows users to draw digits and get real-time predictions while also being able to upload clear images receiving real-time predictions of the digit in question.
- **High Accuracy**: Optimized for accuracy through fine-tuning of the CNN architecture and data preprocessing techniques, averaging a 90% successfull recognition of a digit from the MNIST dataset.

## Technologies Used
- **Python**: Main programming language.
- **TensorFlow/Keras**: Used for building and training the CNN model.
- **PIL (Pillow)**: For image preprocessing and inversion.
- **Tkinter**: For creating the interactive GUI.
- **NumPy**: For numerical computations and array manipulations.
- **Matplotlib**: For visualizing processed images.

## Results
The model shows great accuracy : approximately 90% on images from the unseen data on MNIST testing dataset
The model showcases good accuracy on real world imaages , taken on a camera, given that there is good lighting and relatively low noise on images.
