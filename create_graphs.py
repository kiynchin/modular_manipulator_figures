import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with open("reward_trajectories.pkl", 'rb') as logfile:
    reward_trajs = pickle.load(logfile)

with open("training_data_sizes.pkl", 'rb') as logfile:
    training_groups = pickle.load(logfile)

avg_rewards = [np.mean(rewards) for rewards in reward_trajs] 
episode_lenghts = [len(rewards) for rewards in reward_trajs]
pass


