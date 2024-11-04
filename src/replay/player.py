import tkinter as tk
from tkinter import ttk, filedialog
from utils.file_manager import load_experiment_results
import time
import threading

class ReplayPlayer:
    def __init__(self, root, results=None):
        self.root = root
        self.results = results if results else {}
        self.states = self.results.get("state_tracker", [])
        self.current_index = 0
        self.playing = False
        self.playback_speed = 1.0
        self.total_iterations = len(self.states)
        self.filename = "No file loaded" 
        self.setup_ui()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def setup_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Filename label
        self.filename_label = tk.Label(self.frame, text=f"File: {self.filename}", font=("Arial", 12))
        self.filename_label.pack(pady=5)

        # Iteration label
        self.iteration_label = tk.Label(self.frame, text="Iteration: 0", font=("Arial", 11))
        self.iteration_label.pack(pady=5)

        # Canvas for cube
        self.canvas = tk.Canvas(self.frame, width=1000, height=400)
        self.canvas.pack()

        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Scale(
            self.frame, from_=0, to=max(0, self.total_iterations - 1),
            orient="horizontal", variable=self.progress_var, command=self.on_seek
        )
        self.progress_bar.pack(fill="x", pady=10)

        # Play/Pause button
        self.play_button = tk.Button(self.frame, text="Play", command=self.toggle_play)
        self.play_button.pack(side="left")

        # Speed slider
        self.speed_label = tk.Label(self.frame, text="Speed:")
        self.speed_label.pack(side="left")
        self.speed_var = tk.DoubleVar(value=1.0)
        self.speed_scale = ttk.Scale(
            self.frame, from_=0.1, to=2.0,
            orient="horizontal", variable=self.speed_var, command=self.on_speed_change
        )
        self.speed_scale.pack(side="left")

        # Load button
        self.load_button = tk.Button(self.frame, text="Load Experiment", command=self.load_experiment)
        self.load_button.pack(side="right")

        # Init thread
        self.replay_thread = threading.Thread(target=self.replay)
        self.replay_thread.daemon = True

    def toggle_play(self):
        if not self.states:
            print("No experiment loaded. Please load an experiment first.")
            return

        self.playing = not self.playing
        if self.playing:
            self.play_button.config(text="Pause")
            if not self.replay_thread.is_alive():
                self.replay_thread = threading.Thread(target=self.replay)
                self.replay_thread.start()
        else:
            self.play_button.config(text="Play")

    def replay(self):
        while self.playing and self.current_index < self.total_iterations:
            if not self.root.winfo_exists():
                break
            self.display_state(self.states[self.current_index])
            self.current_index += 1
            self.progress_var.set(self.current_index)
            self.iteration_label.config(text=f"Iteration: {self.current_index}")
            time.sleep(1 / self.playback_speed)
            if self.current_index >= self.total_iterations:
                self.playing = False
                self.play_button.config(text="Play")

    def display_state(self, state):
        self.canvas.delete("all")
        layer_spacing_x = 200
        padding_x = 40
        cell_size = 30

        for layer_idx, layer in enumerate(state):
            x_offset = padding_x + layer_idx * layer_spacing_x
            for i in range(len(layer)):
                for j in range(len(layer[i])):
                    x = j * cell_size + x_offset
                    y = i * cell_size + 50
                    self.canvas.create_text(x, y, text=str(layer[i][j]), font=("Arial", 10))

    def on_seek(self, value):
        if self.states:
            self.current_index = int(float(value))
            self.display_state(self.states[self.current_index])
            self.iteration_label.config(text=f"Iteration: {self.current_index}")

    def on_speed_change(self, value):
        self.playback_speed = float(value)

    def load_experiment(self):
        filename = filedialog.askopenfilename(initialdir="assets/results", title="Select Experiment File", filetypes=[("JSON files", "*.json")])
        if filename:
            loaded_results = load_experiment_results(filename)
            if loaded_results:
                self.filename = filename.split("/")[-1]
                self.filename_label.config(text=f"Filename: {self.filename}")
                self.results = loaded_results
                self.states = self.results.get('state_tracker', [])
                self.total_iterations = len(self.states)
                self.progress_bar.config(to=max(0, self.total_iterations - 1))
                self.current_index = 0
                self.display_state(self.states[self.current_index])
                self.iteration_label.config(text="Iteration: 0")

    def on_close(self):
        self.playing = False
        self.root.destroy()

def main():
    root = tk.Tk()
    root.title("Diagonal Magic Cube Replay Player")
    player = ReplayPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
