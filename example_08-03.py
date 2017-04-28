import yaml

if __name__ == '__main__':
    with open('test.yml') as fs2:
        d = yaml.load(fs2)
    
    frameCount = d['frameCount']
    date = d['calibrationDate']
    cameraMatrix2 = d['cameraMatrix']
    distCoeffs2 = d['distCoeffs']
    
    print('frameCount: ', frameCount)
    print('calibration date: ', date)
    print('camera matrix: ', cameraMatrix2)
    print('distortion coeffs: ', distCoeffs2)
    
    features = d['features']
    
    for i in range(len(features)):
        print('feature #{}: x={}, y={}, lbp={}'.format(
                i, features[i]['x'], features[i]['y'],
                features[i]['lbp']))
