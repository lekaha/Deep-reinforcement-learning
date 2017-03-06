# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:49:35 2017

@author: Kuanho
"""

import gym
env = gym.make('MountainCarContinuous-v0')
for i_episode in range(10):
    observation = env.reset()
    for t in range(10):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.render(close=True)