"""
Simple Linear Regression:
	
	y = b0 + b1 * x

where the coefficients can be estimated as follows:

B1 = sum((x(i) - mean(x)) * (y(i) - mean(y))) / sum( (x(i) - mean(x))^2 )
B0 = mean(y) - B1 * mean(x)
"""

import pandas as pd
import numpy as np


def load_dataset():
	data = pd.read_excel("insurance.xls")
	return data


def calculate_mean(values):
	return sum(values) / float(len(values))


def variance(values, mean):
	return sum([(x - mean) ** 2 for x in values])


def covariance(X, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(X)):
		covar += (X[i] - mean_x) * (y[i] - mean_y)
	return covar


# df = load_dataset()
# X = list(df['X'])
# y = list(df['Y'])
# mean_x, mean_y = calculate_mean(X), calculate_mean(y)
# var_x, var_y = variance(X, mean_x), variance(y, mean_y)

# print('x stats: mean=%.3f variance=%.3f' % (mean_x, var_x))
# print('y stats: mean=%.3f variance=%.3f' % (mean_y, var_y))

# covar = covariance(X, mean_x, y, mean_y)
# print('Covariance: %.3f' % (covar))

# Estimating the coefficients
# B1 = covariance(x, y) / variance(x)
# B0 = mean(y) - B1 * mean(x)

def coefficients(dataset):
	X = list(dataset['X'])
	y = list(dataset['Y'])
	mean_x, mean_y = calculate_mean(X), calculate_mean(y)
	var_x, var_y = variance(X, mean_x), variance(y, mean_y)
	b1 = covariance(X, mean_x, y, mean_y) / var_x
	b0 = mean_y - b1 * mean_x
	return [b0, b1]


def main():
	dataset = load_dataset()
	b0, b1 = coefficients(dataset)
	print('Coefficients: B0=%.3f, B1=%.3f' % (b0, b1))


if __name__ == '__main__':
	main()