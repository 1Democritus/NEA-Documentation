import numpy

class DNN():
  def __init__(self, learningRate, hiddenlayerNo):
    self.__learningRate = learningRate
    self.__hiddenlayerNo = hiddenlayerNo
    self.__w1 = ####
    self.__b1 = ####
    self.__w2 = ####
    self.__b2 = ####

  def feedForward(self, tuple):
    hiddenTensors = self.__w1.dot(tuple) - self.__b1
    hiddenTensorsActivated = self.ReLU(vals)
    finalTensors = self.__w2.dot(hiddenTensorsActivated) - self.__b2
    finalTensorsActivated = self.softmax(finalTensorsActivated)
    return hiddenTensors, hiddenTensorsActivated, finalTensors, finalTensorsActivated
  
  def backprop(self, epochError, tensors, trainset, m):
    finalWeightDerivative = epochError.dot(tensors[1].T) / m
    finalBiasDerivative = sum(epochError) / m
    hiddenDerivative = self.__w2.T.dot(epochError) * self.ReLUderivative(tensors[0])
    hiddenWeightDerivative = hiddenDerivative.dot(trainset.T) / m
    hiddenBiasDerivative = sum(hiddenDerivative) / m
    return hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative

  def updateParameters(self, hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative):
    self.__w1 -= self.__learningRate * hiddenWeightDerivative
    self.__b1 -= self.__learningRate * hiddenBiasDerivative
    self.__w2 -= self.__learningRate * finalWeightDerivative
    self.__b2 -= self.__learningRate * finalBiasDerivative

 @staticmethod
  def softmax(tuple): #activation function to be used for final layer
    expSum = sum(numpy.exp(i) for i in tuple)
    softmaxTuple = [numpy.exp(weight)/expSum for weight in tuple]
    return softmaxTuple

  @staticmethod
  def ReLU(tuple):
    return numpy.maximum(0, tuple)

  @staticmethod
  def ReLUderivative(tuple):
    #needed for finding derivatives
    return (tuple>0).astype(float)

  @staticmethod
  def softmaxDerivative(tuple):
    pass

def crossentropyError(yPred, yActual):
  pass

def trainModel(lr, layerno, epochCount, trainset, label, tensors):
  model = DNN(learningRate = lr, hiddenlayerNo = layerno)
  for epoch in range(epochCount):
    tensors = model.feedForward(trainset)
    epochError = tensors[3] - label
    hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative = model.backprop(epochError, tensors, trainset, m = #)
    model.updateParameters(hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative)
    #display loss
