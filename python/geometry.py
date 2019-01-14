
def polygon_area(points):
    n = len(points)
    sum1 = sum(
        [points[i][0]*points[i+1][1] + points[n-1][0]*points[0][1] for i in range(1,n-1)]
        )
    sum2 = sum(
        [points[i+1][0]*points[i][1] + points[0][0]*points[n-1][1] for i in range(1,n-1)]
        )
    return 0.5*abs(sum1 - sum2)

