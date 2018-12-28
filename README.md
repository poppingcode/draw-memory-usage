# draw-memory-usage
Draw trends in memory usage for a process


## trends_thread_visualization.py
First, you should install psutil, which can query the resources occupied by a process.then install visdom to visualize the data.
pip install psutil
pip install visdom

## Execution steps
- 1.python -m visdom.server    <-Start Visdom Visual Services
- 2.python trends_thread_visualization.py --thread PID  <-PID is the process you want to query.
- 3.input ip:8097 in web   <-You can click in the box of the existing interface(the name I set is "test".For convenience, you can set your own project name when executing py_files.)
- 4.Then the curve will be drawn in real time.(The time interval for query is 1 second) 
