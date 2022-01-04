# CS106A - Lecture 16 - Drawing


# Applied Math
# - Showing drawing examples on canvas
def draw_oval(canvas, left, top, width, height):
  canvas.fill_oval(left + 20, top + 20,      # x, y
                    width - 40, height - 40, # w, h
                    color='yellow')