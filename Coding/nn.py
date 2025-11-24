import numpy

class DNN():
  def __init__(self, learningRate, columnSize, outputSize):
    self.__learningRate = learningRate #determines the rate at which weights change
    #initialise random values between 0.5 and -0.5
    self.__w1 = numpy.random.randn(50, columnSize) - 0.5 
    self.__b1 = numpy.random.randn(50, 1) - 0.5
    self.__w2 = numpy.random.randn(outputSize, 50) - 0.5
    self.__b2 = numpy.random.randn(outputSize, 1) - 0.5

  def feedForward(self, tuple):
    hiddenTensors = numpy.dot(self.__w1, tuple) - self.__b1
    hiddenTensorsActivated = self.ReLU(hiddenTensors)
    finalTensors = numpy.dot(self.__w2, hiddenTensorsActivated) - self.__b2
    finalTensorsActivated = self.softmax(finalTensors)
    return hiddenTensors, hiddenTensorsActivated, finalTensors, finalTensorsActivated
  
  def backprop(self, epochError, tensors, trainset):
    Ysize = trainset.shape(1)
    finalWeightDerivative = numpy.dot(epochError, tensors[1].T) / Ysize
    finalBiasDerivative = numpy.sum(epochError) / Ysize
    hiddenDerivative = numpy.dot(self.__w2.T, epochError) * self.ReLUderivative(tensors[0])
    hiddenWeightDerivative = hiddenDerivative.dot(trainset.T) / Ysize
    hiddenBiasDerivative = numpy.sum(hiddenDerivative) / Ysize
    return hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative

  def updateParameters(self, hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative):
    self.__w1 -= self.__learningRate * hiddenWeightDerivative
    self.__b1 -= self.__learningRate * hiddenBiasDerivative
    self.__w2 -= self.__learningRate * finalWeightDerivative
    self.__b2 -= self.__learningRate * finalBiasDerivative

  @staticmethod
  def softmax(tuple): #activation function to be used for final layer
    expSum = numpy.sum(numpy.exp(i) for i in tuple)
    softmaxTuple = numpy.array([numpy.exp(weight)/expSum for weight in tuple])
    return softmaxTuple

  @staticmethod
  def ReLU(tuple):
    return numpy.maximum(0, tuple)

  @staticmethod
  def ReLUderivative(tuple):
    #needed for finding derivatives
    return (tuple>0).astype(float)

def trainModel(model, epochCount, trainset, label):
  tuple = numpy.array(trainset).flatten()
  print(tuple)
  for epoch in range(epochCount):
    tensors = model.feedForward(tuple)
    predictions = numpy.argmax(numpy.vstack([tensors[3][0], tensors[3][1], tensors[3][2], tensors[3][3], tensors[3][4]]), axis = 0)
    epochError = predictions - label
    hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative = model.backprop(epochError, tensors, tuple)
    model.updateParameters(hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative)
    accuracy = numpy.sum(predictions == label)/len(label)
    print(f"Epoch: {epoch + 1}, accuracy: {accuracy}")
