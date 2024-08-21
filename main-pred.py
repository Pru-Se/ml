import numpy as np
x = np.random.rand(100)
y = 2 * x + 1 + 0.2* np.random.randn(100)
plt.scatter(x, y)

from sklearn.neural_network import MLPRegressor
nn = MLPRegressor(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
nn.fit(x.reshape(-1, 1), y)

y_pred = nn.predict(x.reshape(-1, 1))

plt.scatter(x, y)
plt.scatter(x, y_pred)
