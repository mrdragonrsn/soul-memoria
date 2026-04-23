# Avaliação - Métricas

## Métricas de Classificação

### Accuracy
```python
from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_pred)
```

### Precision, Recall, F1
```python
from sklearn.metrics import precision_score, recall_score, f1_score
precision_score(y_true, y_pred, average='macro')
recall_score(y_true, y_pred, average='macro')
f1_score(y_true, y_pred, average='macro')
```

### ROC-AUC
```python
from sklearn.metrics import roc_auc_score
roc_auc_score(y_true, y_proba)
```

## Matriz de Confusão

```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
# [[TN, FP], [FN, TP]]
```

## Regressão

### MAE
```python
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_true, y_pred)
```

### MSE / RMSE
```python
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
```

### R² Score
```python
from sklearn.metrics import r2_score
r2_score(y_true, y_pred)
```

## Cross-Validation

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
```

## Referências
[[avaliacao/_metricas]]
[[avaliacao/matriz_confusao]]