def straight_line_or_not(coordinates):
    import numpy as np
    """
        Input is the list of tuples containg the coordiantes.
        Fucntion computes the slope and intercept if the points lies in a straight line.
        If lie straight line return the tuple (slope,intercept) having float values till one deciaml point.
        else, return -1
    """
    # YOUR CODE GOES HERE

    c1 = coordinates[0]
    c2 = coordinates[1]

    x1, y1 = c1
    x2, y2 = c2
    slope = (y2 - y1) / (x2 - x1)

    intercept = y1 - slope * x1 

    for c in coordinates[2:]:
        x, y = c

        if (y - (slope * x + intercept)) != 0:
            return -1

    return (np.round(slope, 1), np.round(intercept, 1))

'''
input: 
[(1.0, 5.0), (-3.0, -3.0), (2.5, 8.0)]
output: 
(2.0, 3.0)
'''
