
``` input
2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18

```
# Import library
from sklearn import linear_model

# Set data
features, rows = map(int, input().split())
X, Y = [], []

# Get the parameters X and Y for discovery the variables a and b
for i in range(rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < features:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)
print(X)

# Set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_

# Get the parameters X for discovery the Y
new_rows = int(input())
new_X = []
for i in range(new_rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)

# Gets the result and show on the screen
result = model.predict(new_X)
for i in range(len(result)):
    print(round(result[i],2))
