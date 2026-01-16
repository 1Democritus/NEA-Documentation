import numpy

class DNN():
  def __init__(self, learningRate, columnSize, outputSize):
    self.__learningRate = learningRate #determines the rate at which weights change
    #initialise random values between 0.5 and -0.5
    self.__w1 = numpy.random.randn(50, columnSize) - 0.5 
    self.__b1 = numpy.random.randn(50, 1) - 0.5
    self.__w2 = numpy.random.randn(outputSize, 50) - 0.5
    self.__b2 = numpy.random.randn(outputSize, 1) - 0.5

  def feedForward(self, tupl):
    hiddenTensors = numpy.dot(self.__w1, tupl) + self.__b1
    hiddenTensorsActivated = self.ReLU(hiddenTensors)
    finalTensors = numpy.dot(self.__w2, hiddenTensorsActivated) + self.__b2
    finalTensorsActivated = self.softmax(finalTensors)
    return hiddenTensors, hiddenTensorsActivated, finalTensors, finalTensorsActivated
  
  def backprop(self, epochError, tensors, trainset):
    Ysize = trainset.shape[1]
    finalWeightDerivative = numpy.dot(epochError, tensors[1].T) / Ysize
    finalBiasDerivative = numpy.sum(epochError, axis = 1, keepdims = True) / Ysize
    hiddenDerivative = numpy.dot(self.__w2.T, epochError) * self.ReLUderivative(tensors[0])
    hiddenWeightDerivative = hiddenDerivative.dot(trainset.T) / Ysize
    hiddenBiasDerivative = numpy.sum(hiddenDerivative, axis = 1, keepdims = True) / Ysize
    return hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative

  def updateParameters(self, hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative):
    self.__w1 -= self.__learningRate * hiddenWeightDerivative
    self.__b1 -= self.__learningRate * hiddenBiasDerivative
    self.__w2 -= self.__learningRate * finalWeightDerivative
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
  tupl = trainset
  for epoch in range(epochCount):
    tensors = model.feedForward(tupl)
    predictions = numpy.argmax(tensors[3], axis = 0)
    epochError = tensors[3] - label
    hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative = model.backprop(epochError, tensors, tupl)
    model.updateParameters(hiddenWeightDerivative, hiddenBiasDerivative, finalWeightDerivative, finalBiasDerivative)
    accuracy = numpy.sum(predictions == numpy.argmax(label, axis = 0))/len(label)
    print(f"Epoch: {epoch + 1}, accuracy: {accuracy}")
  return model
