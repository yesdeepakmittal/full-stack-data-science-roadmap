class Perceptron:
    def __init__(self,learning_rate = 0.01,n_iterations = 10, random_state = 7) -> None:
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.random_state = random_state
        
    def hypothesis(self,X,weight,bias):
        return X * weight + bias
        
    def fit_model(self,X,y):
        self.weight_ = 0.0
        self.bias_ = 0.0
        
        for iter in range(self.n_iterations):
            for x,train_y in zip(X,y):
                change = self.learning_rate * (train_y - self.hypothesis(x,self.weight_,self.bias_))
                
                # update weights & bias
                self.weight_ = change * x 
                self.bias_ = change
                