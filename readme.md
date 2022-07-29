## Hand Written Digit recognition
The program tells the what digit it is with a given image (dimensions : 28x28)
with a built in board for drawing digits 


## Files
- interface.py - contain the main gui for program and main file to run program 
- training_model.ipynb - jupyter notebook contain the code to train model (its a sequential model with mnist data set)
- image.png and test.eps - image.png is image of last drawn digit on board and test.eps is supporting file to save it as png
- trained_model.h5 - trained model for classification of digit can be imported directly using 
  - `from keras.models import load_model`
  - `model = load_model('trained_model.h5')`

## Libraries used
1. tkinter - for gui 
2. tensorflow - for training of model 
3. numpy - for dealing with numpy array 
4. Pillow, cv - working with images 
5. matplotlib - for visualizing data 
