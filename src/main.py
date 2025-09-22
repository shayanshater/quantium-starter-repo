import pandas as pd
import os

def make_dataframe(directory):
    files = os.listdir(directory)
    frames = []
    for file in files:
        frames.append(pd.read_csv("data/" + file))
    df = pd.concat(frames, axis=0, ignore_index=True)
    
    #select pink morsel
    df = df[df["product"] == "pink morsel"]

    #create sales column
    df["price"] = df["price"].str.replace("$", "").astype(float)
    df['sales'] = df.price * df.quantity
    
    
    #create final df
    df = df[["date", "sales", "region"]]
    return df



    
    
    
    
