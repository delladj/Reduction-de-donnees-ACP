import numpy as np

def pretrait (dataset) :
    for attr in dataset :
      mean= np.mean(dataset[attr])
      # dataset[attr]= dataset[attr].fillna(mean)
      dataset[attr].fillna(dataset[attr].median(), inplace=True)
      # dataset[attr].fillna(0, inplace=True)
      # dataset[attr].fillna(method='bfill', inplace=True)
      # dataset[attr].fillna(method='ffill', inplace=True)
      # dataset[attr].interpolate() 
    return dataset

    
    
    
    
    
    
    
    
    
    
