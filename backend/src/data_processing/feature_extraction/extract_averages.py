

def extract_ma(stock_data, window = 30):
    stock_data['MA{}'.format(str(window))] = stock_data['Adj Close'].rolling(window).mean()
    return stock_data

def extract_ema(stock_data, window = 100):
    
    stock_data['EMA{}'.format(str(window))] = stock_data['Adj Close'].ewm(span=window, adjust=False).mean() 
    return stock_data

def extract_tr(stock_data):
    stock_data['High-Low'] = stock_data['High'] - stock_data['Low']
    stock_data['High-PrevClose'] = abs(stock_data['High'] - stock_data['Close'].shift(1))
    stock_data['Low-PrevClose'] = abs(stock_data['Low'] - stock_data['Close'].shift(1))

    stock_data['TR'] = stock_data[['High-Low', 'High-PrevClose', 'Low-PrevClose']].max(axis=1)
    return stock_data

def extract_atr(stock_data, window = 14):
   
    stock_data = extract_tr(stock_data)
    # Calculate the ATR
    stock_data['ATR'] = stock_data['TR'].rolling(window=window).mean()

    # Drop intermediate columns
    stock_data.drop(['High-Low', 'High-PrevClose', 'Low-PrevClose', 'TR'], axis=1, inplace=True)
    return stock_data

def extract_adx(stock_data, window = 14):
    stock_data = extract_tr(stock_data)

    # Calculate the Directional Movement (DM)
    stock_data['UpMove'] = stock_data['High'] - stock_data['High'].shift(1)
    stock_data['DownMove'] = stock_data['Low'].shift(1) - stock_data['Low']

    # Initialize the Directional Index (DI) and Directional Index Rating (DXR) columns
    stock_data['DI+'] = (stock_data['UpMove'] > stock_data['DownMove']) * stock_data['UpMove']
    stock_data['DI-'] = (stock_data['DownMove'] > stock_data['UpMove']) * stock_data['DownMove']

    # Calculate the smoothed components of DI+ and DI-
    stock_data['SmoothDI+'] = stock_data['DI+'].rolling(window=window).mean()
    stock_data['SmoothDI-'] = stock_data['DI-'].rolling(window=window).mean()

    # Calculate the Directional Index (DX) and the Directional Movement Index (DMI)
    stock_data['DX'] = abs(stock_data['SmoothDI+'] - stock_data['SmoothDI-']) / (stock_data['SmoothDI+'] + stock_data['SmoothDI-'])
    stock_data['DMI'] = stock_data['DX'].rolling(window=window).mean()

    # Calculate the Average Directional Index (ADX)
    stock_data['ADX'] = stock_data['DMI'].rolling(window=window).mean()

    # Drop intermediate columns
    stock_data.drop(['High-Low', 'High-PrevClose', 'Low-PrevClose', 'TR', 'UpMove', 'DownMove', 'DI+', 'DI-', 'DX', 'DMI'], axis=1, inplace=True)

    return stock_data

def extract_bollinger_band(stock_data, window=30):
    std_dev = 2  # Number of standard deviations

    # Calculate the rolling mean (Simple Moving Average)
    stock_data['SMA'] = stock_data['Close'].rolling(window=window).mean()

    # Calculate the rolling standard deviation
    stock_data['STD'] = stock_data['Close'].rolling(window=window).std()

    # Calculate the Upper Bollinger Band
    stock_data['Upper_Band'] = stock_data['SMA'] + (std_dev * stock_data['STD'])

    # Calculate the Lower Bollinger Band
    stock_data['Lower_Band'] = stock_data['SMA'] - (std_dev * stock_data['STD'])

    stock_data.drop(['SMA', 'STD'], axis=1, inplace=True)

    return stock_data

def extract_commodity_channel_index(stock_data, window=10):

    df = stock_data

    # Define the period for the moving average and constant multiplier
    period = window
    constant = 0.015

    # Calculate typical price
    df['TypicalPrice'] = (df['High'] + df['Low'] + df['Close']) / 3

    # Calculate the moving average of the typical price
    df['MovingAverage'] = df['TypicalPrice'].rolling(window=period).mean()

    # Calculate the mean deviation
    df['MeanDeviation'] = df['TypicalPrice'].rolling(window=period).apply(lambda x: abs((x - x.mean())).mean(),
                                                                          raw=True)

    # Calculate CCI
    df['CCI'] = (df['TypicalPrice'] - df['MovingAverage']) / (constant * df['MeanDeviation'])

    df.drop(['TypicalPrice', 'MovingAverage', 'MeanDeviation'], axis=1, inplace=True)

    return df

def relative_strength_index(stock_data, window=14):
    df = stock_data

    # Define the period for RSI calculation
    period = window

    # Calculate price changes and gains/losses
    df['PriceChange'] = df['Close'].diff()
    df['Gain'] = df['PriceChange'].apply(lambda x: x if x > 0 else 0)
    df['Loss'] = df['PriceChange'].apply(lambda x: abs(x) if x < 0 else 0)

    # Calculate average gains and losses over the specified period
    df['AvgGain'] = df['Gain'].rolling(window=period).mean()
    df['AvgLoss'] = df['Loss'].rolling(window=period).mean()

    # Calculate the relative strength (RS)
    df['RS'] = df['AvgGain'] / df['AvgLoss']

    # Calculate the relative strength index (RSI)
    df['RSI'] = 100 - (100 / (1 + df['RS']))

    df.drop(['RS', 'AvgGain', 'AvgLoss', 'PriceChange', 'Gain', 'Loss'], axis=1, inplace=True)

    return df
