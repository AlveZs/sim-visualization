# Simulation log visualization
## An application for generate gannt chart for simulation logs

### Follow this steps to generate:

* Add logs file in "inputs" folder
* Run command: `python3 main.py`

# Log file format
```
{simulation_duration} {processors_number} {real_processors_number}

[
    [{time_of_sim}, {PROC1_EXECUTION} ... {PROCN_EXECUTION}]
]
```

# Variables

change the `variables.py` class attributes for customize chart