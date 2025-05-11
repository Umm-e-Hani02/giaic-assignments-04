import tkinter as tk

# Canvas size
WIDTH = 400
HEIGHT = 400
CELL = 40  # Size of each square box

def draw_boxes(canvas):
    """ Draws blue boxes (grid cells) on the canvas """
    boxes = []
    for y in range(0, HEIGHT, CELL):
        row = []
        for x in range(0, WIDTH, CELL):
            # Draw rectangle (blue cell with white border)
            box = canvas.create_rectangle(x, y, x + CELL, y + CELL, fill="blue", outline="white")
            row.append(box)
        boxes.append(row)
    return boxes

def erase_box(event):
    """ Makes the box white at mouse position (works like an eraser) """
    row = event.y // CELL
    col = event.x // CELL

    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        canvas.itemconfig(grid[row][col], fill="white")

def main():
    global canvas, grid

    # Create window
    window = tk.Tk()
    window.title("Simple Eraser App")

    # Create canvas
    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
    canvas.pack()

    # Draw grid
    grid = draw_boxes(canvas)

    # When mouse is dragged (left click), erase
    canvas.bind("<B1-Motion>", erase_box)

    # Run the app
    window.mainloop()

# Program start point
if __name__ == "__main__":
    main()
