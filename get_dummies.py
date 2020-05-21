def dummies(dataset, column):
    dummies = pd.get_dummies(dataset[column],prefix=column)
    dataset = pd.concat([dataset,dummies],axis=1)
    return dataset