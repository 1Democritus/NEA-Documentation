import numpy

class DNN():
  def __init__(self, learningRate, columnSize, hiddenSize, outputSize):
    self.__learningRate = learningRate #determines the rate at which weights change
    self.__w1 = numpy.random.randn(hiddenSize, columnSize) * numpy.sqrt(2 / columnSize) #for scaling the inputs
    self.__b1 = numpy.zeros((hiddenSize, 1))
    self.__w2 = numpy.random.randn(outputSize, hiddenSize) * numpy.sqrt(2 / hiddenSize)
    self.__b2 = numpy.zeros((outputSize, 1))

  def feedForward(self, tupl):
    hiddenTensors = numpy.dot(self.__w1, tupl) + self.__b1 #dot function is a shortcut to multiplying all neuron weights by all inputs and storing the results
    hiddenTensorsActivated = self.ReLU(hiddenTensors) #pass tensors through activation function for nonlinearity
    finalTensors = numpy.dot(self.__w2, hiddenTensorsActivated) + self.__b2
    finalTensorsActivated = self.softmax(finalTensors)
    return hiddenTensors, hiddenTensorsActivated, finalTensors, finalTensorsActivated
  
  def backprop(self, epochError, tensors, trainset): #calculating partial derivatives of functions with respect to the loss
    Ysize = trainset.shape[1]
    finalWeightDerivative = numpy.dot(epochError, tensors[1].T) / Ysize
    finalBiasDerivative = numpy.sum(epochError, axis = 1, keepdims = True) / Ysize
    hiddenDerivative = numpy.dot(self.__w2.T, epochError) * self.ReLUderivative(tensors[0])
    hiddenWeightDerivative = hiddenDerivative.dot(trainset.T) / Ysize
    hiddenBiasDerivative = numpy.sum(hiddenDerivative, axis = 1, keepdims = True) / Ysize
    return hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative

  def updateParameters(self, hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative, L2constant = 0.01):
    #subtract derivative multiplied by learning rate from variables
    self.__w1 -= self.__learningRate * (hiddenWeightDerivative + L2constant * self.__w1)
    self.__b1 -= self.__learningRate * hiddenBiasDerivative
    self.__w2 -= self.__learningRate * (finalWeightDerivative + L2constant * self.__w2)
    self.__b2 -= self.__learningRate * finalBiasDerivative

  @staticmethod
  def softmax(tupl): #activation function to be used for final layer
    expSums = numpy.exp(tupl - numpy.max(tupl, axis=0, keepdims=True))
    return expSums / numpy.sum(expSums, axis=0, keepdims=True)

  @staticmethod
  def ReLU(tupl): #introduces nonlinearity
    return numpy.maximum(0, tupl)

  @staticmethod
  def ReLUderivative(tupl):
    #needed for finding derivatives
    return (tupl>0).astype(float)

def trainModel(model, epochCount, trainset, label):
  #database has a class imbalance; therefore class weights set to counterbalance and give more leverage to rare classes
  countPerClass = numpy.sum(label, axis = 1, keepdims = True)
  classWeights = label.shape[1] / (label.shape[0] * countPerClass)
  exampleWeights = numpy.sum(classWeights * label, axis=0, keepdims=True) #extreme assignment of weights to individual patients to counterbalance massive class imbalance
  
  for epoch in range(1, epochCount+1):
    tensors = model.feedForward(trainset)
    predictions = numpy.argmax(tensors[3], axis = 0)
    epochError = (tensors[3] - label) * exampleWeights
    hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative = model.backprop(epochError, tensors, trainset)
    model.updateParameters(hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative)
    accuracy = numpy.sum(predictions == numpy.argmax(label, axis = 0))/label.shape[1]
    if epoch % 20 == 0:
      print(f"Epoch: {epoch}, accuracy: {accuracy}")
  return model
