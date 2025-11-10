import numpy



class DNN():
  def __init__(learningRate, hiddenlayerNo):
    self.__learningRate = learningRate
    self.__hiddenlayerNo = hiddenlayerNo

  def feedforward(tuple):
    pass

  def backprop(tuple):
    pass

  def softmax(tuple): #activation function to be used for final layer
    expSum = sum(exp(i) for i in tuple)
    softmaxTuple = [exp(weight)/expSum for weight in tuple]
    return softmaxTuple

  def ReLU(x):
    return max(0, x)

  def meanSquaredError(predicted, actual):
    return sum((actual[idx]-predicted[idx])**2 for idx in range(len(predicted)))

def trainModel(lr, layerno, epochCount, trainset):
  model = DNN(learningRate = lr, hiddenlayerNo = layerno)
  #
