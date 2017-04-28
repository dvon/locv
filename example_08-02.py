import numpy
import random
import time
import yaml  # Requires pyyaml package.

if __name__ == '__main__':
    d = {}

    d['framecount'] = 5
    d['calibrationDate'] = time.localtime()
    d['cameraMatrix'] = numpy.array(
            [[1000, 0, 320], [0, 1000, 240], [0, 0, 1]],
            dtype='float64')
    d['distCoeffs'] = numpy.array(
            [0.1, 0.01, -0.001, 0, 0], dtype='float64')

    m = []
    
    for i in range(3):
        x = random.getrandbits(10) % 640  # Takes 10 bits to
                                          # represent 640.
        y = random.getrandbits(9) % 480

        lbp = random.getrandbits(8) % 256
        lbp = [int(b) for b in bin(lbp)[2:]]
        lbp = [0] * (8 - len(lbp)) + lbp
        
        m.append({'x': x, 'y': y, 'lbp': lbp})
    
    d['features'] = m

    with open('test.yml', 'w') as fs:
        yaml.dump(d, fs)
