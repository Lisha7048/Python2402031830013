import tkinter as tk

# Main game window
root = tk.Tk()
root.title("Adventure Game")
root.geometry("500x300")

story = tk.StringVar()
story.set("🧙‍♂️ Welcome to the Magical Forest Adventure!\n\nYou're on a quest to find the lost treasure.\n\nChoose a path:")

# Function to update story
def choice1(path):
    if path == "cave":
        story.set("You enter the cave... 🕸️ It's dark and spooky.\nA dragon appears!\nDo you want to fight or run?")
        button1.config(text="Fight", command=lambda: cave("fight"))
        button2.config(text="Run", command=lambda: cave("run"))
    else:
        story.set("You walk into the meadow 🌸 and find a talking tree.\nIt asks: 'Do you seek wisdom or riches?'")
        button1.config(text="Wisdom", command=lambda: meadow("wisdom"))
        button2.config(text="Riches", command=lambda: meadow("riches"))

def cave(action):
    if action == "fight":
        story.set("You bravely fight the dragon and win! 🐉💪\nYou find the treasure hidden behind the dragon! 🎉💰")
    else:
        story.set("You run back safely but miss the treasure. 😢\nGame Over.")
    end_game()

def meadow(answer):
    if answer == "wisdom":
        story.set("The tree grants you eternal wisdom. 🌳🧠\nYou leave the forest a wiser adventurer.")
    else:
        story.set("The tree vanishes and the ground opens beneath you! 😱\nYou fall into a pit. Game Over.")
    end_game()

def end_game():
    button1.config(text="Play Again", command=restart)
    button2.config(text="Exit", command=root.quit)

def restart():
    story.set("🧙‍♂️ Welcome to the Magical Forest Adventure!\n\nYou're on a quest to find the lost treasure.\n\nChoose a path:")
    button1.config(text="Enter Cave", command=lambda: choice1("cave"))
    button2.config(text="Walk into Meadow", command=lambda: choice1("meadow"))

# GUI Layout
tk.Label(root, textvariable=story, wraplength=450, justify="left", font=("Arial", 12)).pack(pady=20)

button1 = tk.Button(root, text="Enter Cave", width=20, command=lambda: choice1("cave"))
button1.pack(pady=5)

button2 = tk.Button(root, text="Walk into Meadow", width=20, command=lambda: choice1("meadow"))
button2.pack(pady=5)

root.mainloop()
