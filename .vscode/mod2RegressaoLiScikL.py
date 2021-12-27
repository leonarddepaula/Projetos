# regressaõ Linear Scikit-learn
import matplotlib.pyplot as plt
import numpy as np


# Dados

x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111,
      0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]

y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657,
      1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]
# plot dos dados


plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

# transforma em numpy array
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

# modelo
from sklearn.linear_model import LinearRegression

# treinando o modelo: y = a*x +b, valores reais (a, b) = (2, 1)
reg = LinearRegression()
reg.fit(x, y)

# coeficiente a, b estimados:
# valores estimados usando numpy diretamente
# a estimado no numpy: 2.05414951
# bestimado no numpy: 0.96798926
print('A estimado: ', reg.coef_.ravel()[0])
print('B estimado: ',reg.intercept_[0])

# predição do modelo 
y_pred = reg.predict(x)

# socre do modelo
score = reg.score(x, y)
print('score', score)

# plot dos dado
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.plot(x, y_pred, label='regressão linear(R2: {:.3f})'.format(score))
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title("Regressão Linear Scikit-Learn")
plt.grid()
plt.show()

# plot dos dado para exemplificar o R2
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.plot(x, y_pred, label='regressão linear(R2: {:.3f})'.format(score))
plt.hlines(y=y.mean(), xmin=x.min(), xmax=x.max(), linestyle='dashed',
            label='Modelo De Referencia do $R^2$')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title("Regressão Linear Scikit-Learn")
plt.grid()
plt.show()

# função para calculo do MSE
def mse (y_true, y_pred, is_ref = False):
    # mse modelo 
    if is_ref:
        mse = ((y_true - y_true.mean())**2).mean()
    else:
        mse = ((y_true - y_pred)**2).mean()
    return mse

# função para calculço do coeficiente de determinação R2
def r2(mse_reg, mse_ref):
    return 1 - mse_reg/mse_ref

# visulizando  y e y_pred
print('y_true:', y.ravel())
print('y_pred:', y_pred.ravel())

# Calculando o mse dos modelos 
mse_reg = mse (y_true=y, y_pred=y_pred)
print("MSE do modelo de regressão:",mse_reg)
mse_ref = mse(y_true=y, y_pred=y_pred, is_ref=True)
print("MSE do modelo de Referencia: ", mse_ref)

# calculando o R2 score
r2_score = r2(mse_reg=mse_reg, mse_ref=mse_ref)
print('coeficiente R2 do modelo implementado (calculado: ',r2_score)

# score retornado pelo scikit-learn
r2_score_skl = reg.score(x, y)