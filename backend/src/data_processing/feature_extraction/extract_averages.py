

def extract_ma(df, window = 30):
    df['MA{}'.format(str(window))] = df['Adj Close'].rolling(window).mean()
    return df

def extract_ema(df, window = 100):
    
    df['EMA{}'.format(str(window))] = df['Adj Close'].ewm(span=window, adjust=False).mean() 
    return df

    