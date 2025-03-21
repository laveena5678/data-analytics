def cleaning(df,column):    
    
    df[column]=df[column].fillna(df[column].mean())

    df = df.dropna()

    df = df.drop_duplicates()
    return df