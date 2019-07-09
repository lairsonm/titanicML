import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import Image, display


#load the train dataset
train = pd.read_csv('data/train.csv')

# set the index to passengerId
train = train.set_index('PassengerId')

#load the test dataset
test = pd.read_csv('data/test.csv')

train.shape

# identify datatypes of the 11 columns, add the stats to the datadict
datadict = pd.DataFrame(train.dtypes)

# identify missing values of the 11 columns,add the stats to the datadict
datadict['MissingVal'] = train.isnull().sum()

# Identify the count for each variable, add the stats to datadict
datadict['Count']=train.count()

# rename the 0 column
datadict = datadict.rename(columns={0:'DataType'})

# get discripte statistcs on "object" datatypes
train.describe(include=['object'])

# get discriptive statistcs on "number" datatypes
train.describe(include=['number'])

