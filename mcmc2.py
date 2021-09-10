import numpy as np
from numba import jit, jitclass, int8, int64, float64


np.random.seed()


ride_wait_times = np.array([42, 10, 25, 18, 33])

transition_prob = np.array([
    [0.23, 0.10, 0.19, 0.23, 0.25],
    [0.12, 0.07, 0.18, 0.42, 0.21],
    [0.30, 0.08, 0.16, 0.24, 0.22],
    [0.40, 0.12, 0.15, 0.09, 0.24],
    [0.09, 0.09, 0.28, 0.11, 0.43]
])

# print(np.cumsum(transition_prob, axis=1))

num_trials = 100

spec = [
    ('ride', int8),
    ('time', int64),
    ('num_rides', int64)
]

@jit(nopython=True)
def weighted_random_choice(probs):
    """Pick a random number with weights in probs"""
    # Verify probs is normalized
    assert np.sum(probs) == 1

    cs = np.cumsum(probs)

    r = np.random.random()

    ret = np.where(cs <= r)[0].shape[0]
    #print(ret)

    return ret

@jitclass(spec)
class Rider(object):
    def __init__(self):
        self.ride = 2
        self.time = 0.
        self.num_rides = 0

    def go_to_next_ride(self):
        probs = transition_prob[self.ride]
        #next_ride = np.random.choice(range(5), p=probs)
        next_ride = weighted_random_choice(probs)

        self.time += ride_wait_times[next_ride] + 5
        if next_ride == self.ride:
            self.time -= 5
        self.ride = next_ride
        self.num_rides += 1

    def amuse(self):
        self.go_to_next_ride()
        while not(self.ride == 2):
            self.go_to_next_ride()
        return self.time

@jit(nopython=True)
def experiment(int64: num_trials) -> float:
    avg = 0
    for i in range(num_trials):
        avg += Rider().amuse()
    return float(avg) / float(num_trials)

if __name__ == "__main__":
    # parktimes = [Rider().amuse()[0] for _ in range(num_trials)]
    pt = experiment(num_trials)
    print(f"Mean time in park: {pt}")
    #for _ in range(5):
    #   weighted_random_choice(transition_prob[0])
