import pandas as pd
import numpy as np
from sklearn import metrics


y_true = ['Enfermo','Sano','Enfermo','Sano''Enfermo','Sano',
          'Enfermo','Sano','Enfermo','Sano','Enfermo','Sano',
          'Enfermo','Sano','Enfermo','Sano','Enfermo','Sano'
          'Enfermo','Sano']

y_pred =  ['Sano','Sano','Sano','Sano','Sano','Sano','Sano',
          'Enfermo','Enfermo','Sano','Enfermo','Sano','Enfermo','Sano',
          'Enfermo','Sano','Enfermo','Sano','Enfermo','Sano']

print ( 'Exactitud:',
       metrics.accuracy_score(y_true,y_pred))
