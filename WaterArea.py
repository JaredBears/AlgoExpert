def waterArea(heights):
    leftMax = [0] * len(heights)
    rightMax = [0] * len(heights)
    rmax = 0
    lmax = 0
    answer = 0
    i = 0
    j = len(heights) - 1
    while i < len(heights) and j > 0:
        leftMax[i] = lmax
        lmax = max(lmax, heights[i])
        rightMax[j] = rmax
        rmax = max(rmax, heights[j])
        i += 1
        j -= 1
    for i, height in enumerate(heights):
        minSide = min(leftMax[i], rightMax[i])
        if minSide > height:
            answer += minSide - height
    return answer
