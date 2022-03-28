import gym
from TaxiAgent import TaxiSolver

env = gym.make("Taxi-v3").env
state = env.reset()
env.render()
taxi = TaxiSolver(env.desc, env.decode(state))

done = False

for a in taxi.path():
    state, reward, done, info = env.step(a)
    env.render()
if done:
    print("Soube encontrar a solucao correta")
else:
    print("Não soube encontrar a solução")
