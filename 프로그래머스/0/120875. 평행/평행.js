function solution(dots) {
    const point1 = dots[0]
    const point2 = dots[1]
    const point3 = dots[2]
    const point4 = dots[3]
    
    function cal(po1, po2) {
        return (po1[1] - po2[1]) / (po1[0] - po2[0])
    }
    
    // point1 point2 + point3 point4
    if (cal(point1, point2) === cal(point3, point4)) {
        return 1
    }
    // point1 point3 + point2 point4
    if (cal(point1, point3) === cal(point2, point4)) {
        return 1
    }
    // point1 point4 + point2 point3
    if (cal(point1, point4) === cal(point2, point3)) {
        return 1
    }
    
    return 0
}