import gym
from time import time
from TaxiAgent import TaxiSolver

print('Estado Inicial:')
env = gym.make("Taxi-v3").env
state = env.reset()
env.render()
taxi = TaxiSolver(env.desc, env.decode(state))
print('\n\n')

print('Começando busca:')

start = time()
path = taxi.path()
end = time()

print(f'Levou {end - start} segundos para procurar uma solução')
if (len(path) > 0):
    print("Soube encontrar a solucao correta")
else:
    print("Não soube encontrar a solução")

for a in path:
    state, reward, done, info = env.step(a)
    env.render()

