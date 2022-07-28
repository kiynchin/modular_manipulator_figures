import tkinter.filedialog as tk
import pickle
import csv

reward_trajectories = []
training_data_sizes = []

fnames = tk.askopenfilenames()
for fname in fnames:
    with open(fname, 'r') as logfile:
        logreader = csv.reader(logfile)
        rewards = []
        data_size = fname.split("_")[2]
        data_size = int(data_size.split(".")[0])
        for row in logreader:
            reward = float(row[1])
            rewards.append(reward)
            if reward >= 9:
                reward_trajectories.append(rewards)
                training_data_sizes.append(data_size)
                rewards = []
        reward_trajectories.append(rewards)
        training_data_sizes.append(data_size)

with open("reward_trajectories.pkl", 'wb') as outfile:
    pickle.dump(reward_trajectories, outfile)

with open("training_data_sizes.pkl", 'wb') as outfile:
    pickle.dump(training_data_sizes, outfile)