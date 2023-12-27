# wealth-disparity-project
Wealth disparity Python project that charts the current wealth disparity in the United States. This
application helps highlight the gap in net income in the United States.

### Starting a virtual environment
```commandline
pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
```

### Running the project
```commandline
pip install -r requirements.txt
python current_wd_chart.py
```

### Future Expansion
We can take the data from dfa-networth-levels.csv and extrapolate a predictive model
of net worth changes within the population, demonstrating a potential worsening
of wealth disparity in the United States. This may be achieved with a Monte Carlo simulation
with a high number of datapoints, however further research is required.
