# event-driven back-testing framework
This is a general event-driven backtesting framework.
1. Receive data from data vendor and convert raw data into desired form. (DataHandler Class)
2. Generate signals based on strategies. (Strategy Class)
3. Generate orders for the portfolio based on the signals. (Portfolio Class)
4. Execute orders. (ExecuteOrder Class)
5. Track successful orders and generate performance metrics for the portfolio. (Portfolio Class)


The following image shows the logic of the framework.

![image](https://user-images.githubusercontent.com/71861810/123497078-859a7f80-d5f9-11eb-957f-37cb721ab5ad.png)
