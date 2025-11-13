import numpy

class DNN():
  def __init__(self, learningRate, hiddenlayerNo):
    self.__learningRate = learningRate
    self.__hiddenlayerNo = hiddenlayerNo
    self.__weight = ####
    self.__bias = ####

  def feedforward(self, tuple):
    vals = self.__weight.dot(tuple) - self.__bias
    valsActivated = self.ReLU(vals)
    return vals, valsActivated

  def finalfeedforward(self, tuple):
    vals = self.__weight.dot(tuple) - self.__bias
    valsActivated = self.softmax(vals)
    vals, valsActivated
  
  def backprop(self, tuple):
    #calculate partial derivatives using chain rule
    pass

  def updateParameters(self, ):
    pass

 @staticmethod
  def softmax(tuple): #activation function to be used for final layer
    expSum = sum(numpy.exp(i) for i in tuple)
    softmaxTuple = [numpy.exp(weight)/expSum for weight in tuple]
    return softmaxTuple

  @staticmethod
  def ReLU(x):
    return numpy.maximum(0, x)



def trainModel(lr, layerno, epochCount, trainset):
  model = DNN(learningRate = lr, hiddenlayerNo = layerno)
  for epoch in epochCount:
    model.feedforward(trainset)
    model.backprop(trainset)
    model.updateParameters(trainset)
    #display loss
