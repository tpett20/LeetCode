// 1184. Distance Between Bus Stops
/*
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.
The bus goes along both directions i.e. clockwise and counterclockwise.
Return the shortest distance between the given start and destination stops.
*/

var distanceBetweenBusStops = function(distance, start, destination) {
    if (start === destination) return 0
    let i = start
    let fwdDist = 0
    while (i % distance.length !== destination) {
        fwdDist += distance[i % distance.length]
        i++
    }
    i = start
    let revDist = 0
    while (i !== destination) {
        i--
        if (i === -1) {
            i = distance.length - 1
        }
        revDist += distance[i]
    }
    return Math.min(fwdDist, revDist)
};

console.log(distanceBetweenBusStops([1,2,3,4], 0, 1))