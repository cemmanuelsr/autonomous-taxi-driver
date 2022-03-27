import gym
from TaxiAgent import TaxiAgent
from utils import *

env = gym.make("Taxi-v3").env
state = env.reset()
env.render()

taxi_row, taxi_col, pass_idx, dest_idx = env.decode(state)
print(taxi_row, taxi_col, pass_idx, dest_idx)

pass_row, pass_col = find_row_col(env.desc, pass_idx)
print(pass_row, pass_col)

#   taxi = TaxiAgent(env.desc, env.decode(state))
#   done = None

#    for a in taxi.path():
#        state, reward, done, info = env.step(a)
#        env.render()
#    if done:
#        print("Soube encontrar a solucao correta")
#    else:
#        print("Não soube encontrar a solução")

