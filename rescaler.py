from sklearn import preprocessing
import numpy as np

#create array
x = np.array([[-50.1], [-10.0], [1.5], [40.2], [90.3]])

# Create scaler
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))

# Scale feature
x_scale = minmax_scale.fit_transform(x)

# Show feature
print(x_scale)
