class Color:

  def __init__(self):
    self.all_colors = self.initialize_colors()

  def initialize_colors(self):
    all_colors = [
      "#642867",
      "#00eb00",
      "#0064ff",
      "#a5ff00",
      "#ba6aff",
      "#30ef2a",
      "#003bb1",
      "#00bd00",
      "#d10091",
      "#00ea8e",
      "#c62ea4",
      "#008300",
      "#002188",
      "#c2d44b",
      "#9c3095",
      "#007c00",
      "#ff5fac",
      "#00ffdd",
      "#df0066",
      "#00ffff",
      "#ff4c26",
      "#00f6ff",
      "#b40000",
      "#00f5ff",
      "#ad2c00",
      "#00edff",
      "#fb447b",
      "#64ad31",
      "#ffb2fa",
      "#257c2f",
      "#614f89",
      "#c58e2d",
      "#0072b9",
      "#435e00",
      "#0089c3",
      "#691d00",
      "#00e9ff",
      "#410000",
      "#c6f7f2",
      "#2d0600",
      "#009776",
      "#4f1b00",
      "#00828d",
      "#774064",
      "#003600",
      "#28474e",
      "#002d00",
      "#00725b",
      "#001d00",
      "#00341e"
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