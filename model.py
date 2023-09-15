import numpy as np


class LinearRegression:

    def __init__(self, use_intercept=True):
        self.coefficients = None
        self.intercept = 0.0 if use_intercept else None
        self.use_intercept = use_intercept

    def fit(self, X, y):
        if self.use_intercept:
            ones = np.ones((X.shape[0], 1))
            X_b = np.hstack([ones, X])
        else:
            X_b = X

        theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

        if self.use_intercept:
            self.intercept = theta_best[0]
            self.coefficients = theta_best[1:]
        else:
            self.coefficients = theta_best

    def predict(self, X):
        if self.use_intercept:
            ones = np.ones((X.shape[0], 1))
            X_b = np.hstack([ones, X])
            return X_b.dot(np.insert(self.coefficients, 0, self.intercept))
        else:
            return X.dot(self.coefficients)

    def __str__(self):
        return f"Linear Regression Model: Intercept = {self.intercept}, Coefficients = {self.coefficients}"


class QuadraticRegression(LinearRegression
                          ):  # Inherits from LinearRegression for simplicity

    def fit(self, X, y):
        X_squared = X**2
        if self.use_intercept:
            ones = np.ones((X.shape[0], 1))
            X_b = np.hstack([ones, X, X_squared])
        else:
            X_b = np.hstack([X, X_squared])

        theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

        if self.use_intercept:
            self.intercept = theta_best[0]
            self.coefficients = theta_best[1:]
        else:
            self.coefficients = theta_best

    def predict(self, X):
        X_squared = X**2
        if self.use_intercept:
            ones = np.ones((X.shape[0], 1))
            X_b = np.hstack([ones, X, X_squared])
            return X_b.dot(np.insert(self.coefficients, 0, self.intercept))
        else:
            return np.hstack([X, X_squared]).dot(self.coefficients)

    def __str__(self):
        return f"Quadratic Regression Model: Intercept = {self.intercept}, Coefficients = {self.coefficients}"
