"""
this class created for core data generating functions
"""
import numpy as np


class Core:
    def __init__(self):
        print("default ctor")

    @staticmethod
    def stationary(mean=20, scale=10, size=100):
        """
        mean:  center of a distribution
        scale: width of the distribution
        """
        stat = np.random.normal(mean, scale, size)
        stat = np.rint(stat)
        return stat

    @staticmethod
    def trendy(k=3, b=3, size=100):
        func = lambda x, k, b: (k * x + b)
        linear = np.array([func(x, k, b) for x in range(1, size + 1)])
        return linear

    @staticmethod
    def const(const=3, size=100):
        return Core.trendy(0, const, size)

    @staticmethod
    def __noise(noise_per=5, amplitude=10, size=100):
        import time
        np.random.seed(int(time.time()))
        noise_per /= 100
        noise_high = amplitude
        noise_low = -1 * amplitude
        randoms = np.random.randint(low=noise_low, high=noise_high, size=(int(size * noise_per)))
        noise = np.array([0] * int(size * round(1 - noise_per, 2)))
        noise = np.concatenate((noise, randoms))
        if len(noise) != size:
            noise = np.append(noise, np.random.randint(low=noise_low, high=noise_high))
        np.random.shuffle(noise)
        return noise

    @staticmethod
    def near_trendy(k=3, b=3, noise_percent=5, amplitude=3, size=100):
        tr = Core.trendy(k, b, size)
        nc = Core.__noise(noise_per=noise_percent, size=size, amplitude=amplitude)
        near_t = tr + nc
        return near_t

    @staticmethod
    def near_constant(const=5, noise_percent=5, amplitude=5, size=100):
        return Core.near_trendy(k=0, b=const, noise_percent=noise_percent, amplitude=amplitude, size=size)

    @staticmethod
    def trend_stationary(k=3, b=3, mean=10, scale=10, size=100):
        linear = Core.trendy(k=k, b=b, size=size)
        stat = Core.stationary(mean=mean, scale=scale, size=size)
        return linear + stat
