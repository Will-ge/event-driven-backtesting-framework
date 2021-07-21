# event-driven back-testing framework
This is a general event-driven backtesting framework.
1. Receive data from data vendor and convert raw data into desired form. (DataHandler Class)
2. Generate signals based on strategies. (Strategy Class)
3. Generate orders for the portfolio based on the signals. (Portfolio Class)
4. Execute orders. (ExecuteOrder Class)
5. Track successful orders and generate performance metrics for the portfolio. (Performance Class)

The following image shows the logic of the framework.
<p align="centre">
  <img src="./backtesting framework.png"> </img>
</p>
