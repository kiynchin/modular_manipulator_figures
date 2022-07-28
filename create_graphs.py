import pickle
import matplotlib.pyplot as plt

with open("reward_trajectories.pkl", 'rb') as logfile:
    trajectories = pickle.load(logfile)

with open("training_data_sizes.pkl", 'rb') as logfile:
    training_groups = pickle.load(logfile)


