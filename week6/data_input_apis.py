# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
This is about using an api "Application program interface" ...basic idea, allows
direct access to some database or parts of it without having do download everything

Documentation is here...

https://pandas-datareader.readthedocs.io/en/latest/index.html

'''

from pandas_datareader import data, wb # This will import the data reader
import datetime # Then this will import the datatime package...more on all of this later

start = datetime.datetime(2005,1,1) # simple funcitonality of the datatime package
                                    # just specify the year, month, date and it returns
                                    # and object that the data reader will interpert

codes = ["GDPC1", "PCEC96"] # here are the codes, remember this from EGB?
                            # Honestly, this is the hardest part with APIs figuring
                            # out the codes to ask of the API

fred = data.DataReader(codes,"fred",start)  # Then for fred, you hand it the codes
                                            # Tell it you want to ask from FRED
                                            # then tell it the start date
                                            
print(fred)

fred.dropna(inplace = True)

fred.pct_change().plot()
fred.pct_change().std()

# How to change the start date....

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# This is the world bank example, its a bit more intricate in what needs to be
# specified....

var = ["NY.GDP.PCAP.PP.KD"] # this should be gdp per capita
iso = ["USA", "FRA"]
year = 2013

wbgdp_pc = wb.download(indicator = var, country = iso, start = year, end = year)

wbgdp_pc.index
# One of the things here is that the dataframe can be multiindexed, country, year
# in this case, again we will come back to this in the future...


wbgdp_pc.plot(kind = "barh")

# We can quickly plot this as well...

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
ticker = ['AMZN', 'GOOG']
q = data.get_quote_yahoo("XXBTZUSD") # This is going to give a "real time" quote
print(q)

# This is how to get historical quotes...

start = datetime.datetime(2005,1,1)
end = datetime.datetime(2017,10,1)

hq = data.DataReader(ticker, 'yahoo', start, end)
# This is interesting, chcekout the type of hq? Is it a dataframe or something else

hq["Close"].plot()

#Then lets plot this...
#%%
###############################################################################
# Here is how to get bit coin data... Thanks Diego!

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2017,10,17)

bitcoin = data.DataReader("BITSTAMP/USD", 'quandl', start, end)

bitcoin["Last"].plot()
















