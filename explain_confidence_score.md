

First I will explain how the score is generated. The confidence score displayed on the edge of box is the output of the model faster_rcnn_resnet_101. Here is how it is generated.

enter image description here

The figure above is borrowed from Fast R-CNN but for the box predictor part, Faster R-CNN has the same structure. We start from the ROI pooling layer, all the region proposals (on the feature map) go through the pooling layer and will be represented as fixed shaped feature vectors, then through the fully connected layers and will become the ROI feature vector as shown in the figure. Now the same ROI feature vector will be fed to a softmax classifier for class prediction and a bbox regressor for bounding box regression. Here is how they look like in the tensorflow graph.

enter image description here

In the graph, Flatten and Flatten_1 node both receive the same feature tensor and they perform flatten op (After flatten op, they are in fact the ROI feature vector in the first figure) and they are still the same. Now we focus on the ClassPredictor because this will actually give the final class predictions.

enter image description here

The figure above is what is inside ClassPredictor. It is in fact a fully connected layer as shown in the first figure. The output tensor is of shape 64*24 in the figure and it represents 64 predicted objects, each is one of the 24 classes (23 classes with 1 background class). So for each object, the ouput is a 1x24 vector, the 99% as well as 100% confidence score is the biggest value in the vector.

So regarding your question, the confidence score is not defined but the ouput of the model, there is a confidence score threshold which you can define in the visualization function, all scores bigger than this threshold will be displayed on the image. So you cannot change the confidence score unless you retrain the model and/or provide more training data. In your figure, the 99% detection of tablet will be classified as false positive when calculating the precision.

And the solution to address it is to add more training data and/or train for more steps (but not overfitting)
