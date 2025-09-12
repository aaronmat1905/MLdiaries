# Manual Implementation of a Perceptron
"""
A Perceptron is a Mathematical Model inspired from the Neuron of the Human Brain. 
It takes inputs, computes a weighted sum and then applies an activation function to produce an output.

USED FOR BINARY CLASSIFICATION
CANNOT IMPLEMENT NON-LINEARLY SEPERABLE PROBLEMS for complex tasks
"""

class Perceptron: 
  def __init__(self, input_dim, learning_rate=0.1, epochs=100):
    self.weights = np.zeroes(input_dim) 
    self.bias = 0
    self.learning_rate = learning_rate
    self.epochs = epochs
    
  def activation(self,x): 
    """
      Implementation of Activation Function
      f(g(x)) = 1 if x >= 0 else 0
    """    
    return np.where(x >= 0, 1 , 0)
    
  def predict(self, x): 
    """
      Implementation of Prediction: 
      g(x) = sigma(WiXi) + bias
      and then, f(g(x) is returned.
    """
    net = np.dot(x, self.weights) + self.bias 
    return self.activation(net)
    
  def fit(self, x,y): 
    """
      Implementation of Training our perceptron:
      Predict, find error, update weights and bias and exit when target satisfied
      Inspired from perceptron learning algorithm.
    """
    for _ in range(self.epochs): 
      for xi, target in zip(x, y):
        pred = self.predict(xi)
        error = target - pred 
        self.weights += self.lr*error*xi 
        self.bias += self.lr*error

x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

myPerceptron = Perceptron(input_dim = 2) 
myPerceptron.fit(x,y) 
print(f"Predictions:", [myPerceptron.predict(xi) for xi in x] 
