# Importing the matplotlib.pyplot
import matplotlib.pyplot as plt
from variables import Variables
from datetime import datetime


class Chart:

  def __init__(
    self,
    filename,
    execution_log,
    real_processors,
    processors_number,
    colors
  ):
    self.filename = filename
    self.execution_log = execution_log
    self.procs_number = processors_number
    self.real_processors = real_processors
    self.notional_procs = processors_number - real_processors
    self.duration = Variables.END_SIM - Variables.START_SIM
    self.colors = colors
    self.height = self.procs_number * Variables.SPACING + Variables.PADDING

  def processors_positions(self):
    position = 15
    positions = []

    for i in range(self.procs_number):
      positions.append(position)
      position += Variables.SPACING
   
    return positions
  
  def processors_labels(self):
    labels = []

    for i in range(self.real_processors):
      labels.append('P%d' % (i + 1))

    for j in range(self.real_processors, self.real_processors + self.notional_procs):
      labels.append('NP%d' % (j + 1))
    
    return labels

  def setup_chart(self, gnt, positions):
    # Declaring a figure "gnt"
    
    # Setting Y-axis limits
    gnt.set_ylim(0, self.height)
    
    # Setting X-axis limits
    gnt.set_xlim(Variables.START_SIM, Variables.END_SIM)
    
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('time')
    gnt.set_ylabel('Processors')
    
    # Setting ticks on y-axis
    gnt.set_yticks(positions)
    # Labelling tickes of y-axis
    gnt.set_yticklabels(self.processors_labels())
    
    # Setting graph attribute
    gnt.grid(True)

    return gnt

  def fill_chart(self, data, gnt, positions):
    TIME_INDEX = 0
    PROCESSOR_EXECUTION_INFO = 1
    SERVER_INDEX = 1
    TASK_INDEX = 2

    colors = {}

    for i in range(len(data)-1):
      current_time = data[i][TIME_INDEX]
      next_time = data[i+1][TIME_INDEX]
      if (current_time >= Variables.START_SIM and next_time <= Variables.END_SIM):
        execution_info = data[i][PROCESSOR_EXECUTION_INFO]
        for j in range(len(execution_info)):
          # Slave running
          object_color = 'white'
          border = 'white'
          if (len(execution_info[j]) == 3):
            object_color = self.colors[execution_info[j][TASK_INDEX]]
            border = self.colors[execution_info[j][SERVER_INDEX]]

            if (j > self.real_processors - 1):
              gnt.text(
                (next_time + current_time)/2, positions[j] + 5,
                'Master: %d' % execution_info[j][SERVER_INDEX], 
                ha='center', 
                va='center',
                color='white',
              )
          
          gnt.broken_barh(
            [(current_time, next_time)],
            (positions[j], Variables.BAR_HEIGHT),
            facecolors = object_color,
            edgecolor = border,
            linewidth=3
          )
              



  def save_chart(self):
    fig, gnt = plt.subplots()

    positions = self.processors_positions()

    self.setup_chart(gnt, positions)
    self.fill_chart(self.execution_log, gnt, positions)
    
    datetime_string = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
    
    fig.set_size_inches(Variables.FIG_WIDTH, Variables.FIG_HEIGHT)
    plt.savefig("./charts/{}-{}.png".format(
      self.filename,
      datetime_string
    ))