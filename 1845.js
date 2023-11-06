// 1845. Seat Reservation Manager
/*
Design a system that manages the reservation state of n seats that are numbered from 1 to n.
Implement the SeatManager class:
- SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
- int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
- void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
*/

class SeatManager {
    constructor(n) {
        this.lastIdx = 0
        this.unreserved = []
    }
    
    reserve() {
        if (!this.unreserved.length) {
            return ++this.lastIdx
        } else {
            return this.unreserved.pop()
        }
    }
    
    unreserve(seat) {
        if (!this.unreserved.length) {
            this.unreserved.push(seat)
        } else {
            let left = 0
            let right = this.unreserved.length - 1
            while (left <= right) {
                let midPt = Math.floor((left + right) / 2)
                if (seat > this.unreserved[midPt]) {
                    right = midPt - 1
                } else {
                    left = midPt + 1
                }
            }
            this.unreserved.splice(left, 0, seat)
        }
    }
}

/*
 * Your SeatManager object will be instantiated and called as such:
 * var obj = new SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
*/

const obj = new SeatManager(5)
console.log(obj.reserve())
console.log(obj.reserve())
console.log(obj.unreserve(2))
console.log(obj.reserve())
console.log(obj.reserve())
console.log(obj.reserve())
console.log(obj.reserve())
console.log(obj.unreserve(5))