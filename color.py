class Color:

  def __init__(self):
    self.all_colors = self.initialize_colors()

  def initialize_colors(self):
    all_colors = [
      '#e6194b',
      '#3cb44b',
      '#ffe119',
      '#4363d8',
      '#f58231',
      '#911eb4',
      '#46f0f0',
      '#f032e6',
      '#bcf60c',
      '#fabebe',
      '#e6beff',
      '#9a6324',
      '#fffac8',
      '#800000',
      '#aaffc3',
      '#808000',
      '#000075',
      '#808080',
      '#000000',
      "#fb447b",
      "#ffb2fa",
      "#614f89",
      "#c58e2d",
      "#0072b9",
      "#435e00",
      "#0089c3",
      "#691d00",
      '#ffd8b1',
      "#257c2f",
      "#00e9ff",
      "#c6f7f2",
      '#008080',
      "#2d0600",
      "#009776",
      "#4f1b00",
      "#00828d",
      "#774064",
      "#64ad31",
    ]

    return all_colors
    
  def divide_chunks(self, array, n):
    for i in range(0, len(array), n): 
      yield array[i:i + n]

  def randomize_colors(self, colors):
    randomized = []

    while len(colors) > 0:
      for color_group in colors:
        if (len(color_group) == 0):
          colors.remove(color_group)
          break
        color = color_group[0]
        randomized.append(color)
        color_group.remove(color)

    return randomized