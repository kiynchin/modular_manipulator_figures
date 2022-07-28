import tkinter.filedialog as tk
import pickle
import csv

reward_trajectories = []

fnames = tk.askopenfilenames()
for fname in fnames:
    with open(fname, 'r') as logfile:
        logreader = csv.reader(logfile)
        rewards = []
        for row in logreader:
            reward = float(row[1])
            rewards.append(reward)
            if reward >= 9:
                reward_trajectories.append(rewards)
                rewards = []

with open("trajectories.pkl", 'wb') as outfile:
    pickle.dump(reward_trajectories, outfile)
