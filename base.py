from data import HistoricCSVDataHandler
from strategy import BuyAndHoldStrategy
from portfolio import NaivePortfolio
from execution import SimulatedExecutionHandler

import event
import queue
import time, datetime

startdate = datetime.datetime(2018,6,25)
#startdate=datetime.datetime.strptime(stdate, '%Y-%m-%d %H:%M:%S')
global events
events = queue.Queue()
# Declare the components with respective parameters
bars = HistoricCSVDataHandler(events,'C:\\Users\\jinji\\Desktop\\event-driven',['SPY'])
strategy = BuyAndHoldStrategy(bars,events)
port = NaivePortfolio(bars, events,startdate ,100000)
broker = SimulatedExecutionHandler(events)

while True:
    # Update the bars (specific backtest code, as opposed to live trading)
    if bars.continue_backtest == True:
        bars.update_bars()
    else:
        break
    
    # Handle the events
    while True:
        try:
            event = events.get(False)
        except queue.Empty:
            break
        else:
            if event is not None:
                if event.type == 'MARKET':
                    strategy.calculate_signals(event)
                    port.update_timeindex(event)

                elif event.type == 'SIGNAL':
                    port.update_signal(event)

                elif event.type == 'ORDER':
                    broker.execute_order(event)

                elif event.type == 'FILL':
                    port.update_fill(event)
    print("done")
    # 10-Minute heartbeat
    time.sleep(0.1)

print(port.output_summary_stats())