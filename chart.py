# Importing the matplotlib.pyplot
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from variables import Variables
from datetime import datetime


class Chart:

  def __init__(
    self,
    filename,
    execution_log,
    real_processors,
    processors_number,
    tasks_number,
    colors
  ):
    self.filename = filename
    self.execution_log = execution_log
    self.procs_number = processors_number
    self.real_processors = real_processors
    self.notional_procs = processors_number - real_processors
    self.colors = colors
    self.tasks_number = tasks_number
    self.duration = Variables.END_SIM - Variables.START_SIM
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

    for i in range(len(data)-1):
      current_time = data[i][TIME_INDEX]
      next_time = data[i+1][TIME_INDEX]
      if (current_time >= Variables.START_SIM and next_time <= Variables.END_SIM):
        execution_info = data[i][PROCESSOR_EXECUTION_INFO]
        for j in range(len(execution_info)):
          # Slave running
          object_color = 'white'
          border = None
          execution_length = len(execution_info[j])
          is_notional_processor = j > self.real_processors - 1

          if (execution_length == 4):
            object_color = self.colors[execution_info[j][TASK_INDEX]]

            if (is_notional_processor):
              border = self.colors[execution_info[j][SERVER_INDEX]]
              gnt.text(
                (next_time + current_time)/2, positions[j] + 5,
                'M%d' % execution_info[j][SERVER_INDEX], 
                ha='center', 
                va='center',
                color='white',
              )

              gnt.broken_barh(
                [(current_time, next_time - current_time)],
                (positions[execution_info[j][-1]], Variables.BAR_HEIGHT),
                facecolors = 'white',
                edgecolor = border,
                linewidth=3
              )


            gnt.broken_barh(
              [(current_time, next_time - current_time)],
              (positions[j], Variables.BAR_HEIGHT),
              facecolors = object_color,
              edgecolor = border,
              linewidth=3
            )
              
  def color_legends(self, tasks_number):
    leg_colors = []
    for i in range(tasks_number):
      leg_colors.append(mpatches.Patch(
        color=self.colors[i],
        label='T%d' % i)
      )
    
    return leg_colors


  def save_chart(self):
    fig, gnt = plt.subplots()

    positions = self.processors_positions()
    color_legend = self.color_legends(self.tasks_number)


    self.setup_chart(gnt, positions)
    self.fill_chart(self.execution_log, gnt, positions)
    gnt.legend(handles=color_legend, bbox_to_anchor=(1.1, 1))
    
    datetime_string = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
    
    fig.set_size_inches(Variables.FIG_WIDTH, Variables.FIG_HEIGHT)
    plt.savefig("./charts/{}-{}.png".format(
      self.filename,
      datetime_string
    ))