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
  
  def backprop(self, tuple, tensors):
    finalDerivative = ##
    hiddenDerivative = ##
    return hiddenDerivative, finalDerivative

  def updateParameters(self, hiddenDerivative, finalDerivative):
    self.__w1, self.__b1 -= self.__learningRate * hiddenDerivative
    self.__w2, self.__b2 -= self.__learningRate * finalDerivative

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



def trainModel(lr, layerno, epochCount, trainset):
  model = DNN(learningRate = lr, hiddenlayerNo = layerno)
  for epoch in range(epochCount):
    tensors = model.feedForward(trainset)
    hiddenDerivative, finalDerivative = model.backprop(trainset, tensors)
    model.updateParameters(hiddenDerivative, finalDerivative)
    #display loss
