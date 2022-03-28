import gym
from time import time
from TaxiAgent import TaxiSolver

def test_1():

    env = gym.make("Taxi-v3").env
    state = env.reset()
    taxi = TaxiSolver(env.desc, env.decode(state))

    done = False

    start = time()
    path = taxi.path()
    end = time()

    for a in taxi.path():
        state, reward, done, info = env.step(a)

    assert done
    assert (end - start) < 0.05

def test_2():

    env = gym.make("Taxi-v3").env
    state = env.reset()
    taxi = TaxiSolver(env.desc, env.decode(state))

    done = False

    start = time()
    path = taxi.path()
    end = time()

    for a in taxi.path():
        state, reward, done, info = env.step(a)

    assert done
    assert (end - start) < 0.05

def test_3():

    env = gym.make("Taxi-v3").env
    state = env.reset()
    taxi = TaxiSolver(env.desc, env.decode(state))

    done = False

    start = time()
    path = taxi.path()
    end = time()

    for a in taxi.path():
        state, reward, done, info = env.step(a)

    assert done
    assert (end - start) < 0.05

def test_4():

    env = gym.make("Taxi-v3").env
    state = env.reset()
    taxi = TaxiSolver(env.desc, env.decode(state))

    done = False

    start = time()
    path = taxi.path()
    end = time()

    for a in taxi.path():
        state, reward, done, info = env.step(a)

    assert done
    assert (end - start) < 0.05

def test_5():

    env = gym.make("Taxi-v3").env
    state = env.reset()
    taxi = TaxiSolver(env.desc, env.decode(state))

    done = False

    start = time()
    path = taxi.path()
    end = time()

    for a in taxi.path():
        state, reward, done, info = env.step(a)

    assert done
    assert (end - start) < 0.05
