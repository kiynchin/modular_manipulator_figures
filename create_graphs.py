import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with open("reward_trajectories.pkl", 'rb') as logfile:
    reward_trajs = pickle.load(logfile)

with open("training_data_sizes.pkl", 'rb') as logfile:
    training_groups = pickle.load(logfile)

avg_rewards = [np.mean(rewards) for rewards in reward_trajs] 
episode_lengths = [len(rewards) for rewards in reward_trajs]

log_data = {"Reward Trajectories" : reward_trajs,
            "Training Set Group" : training_groups,
            "Mean Episode Reward" : avg_rewards,
            "Episode Length" : episode_lengths}
        
log_df = pd.DataFrame(log_data)
pass

