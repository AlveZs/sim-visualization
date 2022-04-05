from color import Color
from chart import Chart
import glob
import json
import os

path = './inputs/*'
    
files = glob.glob(path)
print(files)

for name in files: 
    current_file = open(name, 'r')
    duration, processors_number, real_processors, tasks_number = [int(n) for n in current_file.readline().split()]
    execution_log = json.loads(current_file.readline())
    filename = os.path.basename(name).split('.')[0]

    colors = Color().all_colors
    chart = Chart(
        filename = filename,
        execution_log = list(execution_log),
        processors_number = processors_number,
        real_processors = real_processors,
        tasks_number = tasks_number,
        colors = colors
    )

    chart.save_chart()