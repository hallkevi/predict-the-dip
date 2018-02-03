# predict-the-dip
Simple univariate linear regression model coded in Python to estimate a future stock price.

We want to predict the future price of a stock with the help of some basic differential statistics in Python.
We are going to apply a simple univariate linear regression with x = ‘date’ as the independent variable and y = ‘stock price' as the dependent variable. 

We’re going to look at historic data of the stock price of Commerzbank AG for the past 18 months. I downloaded the dataset from Yahoo Finance (https://finance.yahoo.com/quote/CBK.MI/history?period1=1454022000&period2=1517180400&interval=1d&filter=history&frequency=1d ) as csv. 
I changed the dataset to a two-column workbook, placed the dates with numbers and rounded up all stock prices to full integers. 

/*---Steps--*/

1. Import of the respective packages
  I’m using Python 3.6 in Spyder, a powerful framework of the Anaconda IDE. 
  We are going to use Pandas to interpret our csv and Numpy for statistical operations. The result will be plotted in           Matplotlib. 

2. Get the data frame
I’m using the ‘read_csv' package of Pandas to import our data set. The manipulated csv consists of 2 columns (‘ClosePrice’ and’Date’) and 394 rows without the column headers. We want to import the two columns as lists and see if we can get the data. Let’s print out the variables to see the data: 

3. Get the regression equation 
The formula of a regression line is:

Y = bX + A

with b as the slope of the regression line and A as the intercept. 
We could certainly let the machine just calculate our regression line for example with scipy.stats.linregress (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html), but for better understanding, let’s quickly calculate regression line equation manually. We’d need both means, standard deviations and a correlation coefficient to calculate the slope and intercept of the regression line. I will use Pearson’s r as a correlation coefficient, as we are examining a univariate dataset of two continuous variables. 

I convert the two lists into arrays to get our regression line and plot the result in a scatter plot.

4. Plot
Looking at the plot, we can see a strong positive relationship with r = 0.97. With the equation of the regression line

y = 0.02044x + 4.97535

we can now predict the stock price for future dates.

5. Evaluation
Let’s assume, we want to know the predicted future price of the stock 1 month from now, because we’re owning a bunch of Commerzbank stocks and want to sell them with a put option on Feb 26, 2018 because we expect the price to rise. Integrating x = 430 in the equation, we get the predicted stock value of 13,76$. 

On a second scenario, we want to invest longterm, because we heard some rumours of the EZB lowering the EURIBOR constantly. We are interested in a 30% net profit on our asset and therefore looking at the predicted stock price 3 years from now. We set x = 400 + 780 = 1180 (780: 52 weeks * 5 trading days per week) and get a predicted stock value of y = 29,09$. That’s an predicted profit of over 100% so we’re going in.
