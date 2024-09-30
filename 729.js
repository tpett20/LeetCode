// 729. My Calendar I
/*
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
Implement the MyCalendar class:
- MyCalendar() Initializes the calendar object.
- boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
*/

class MyCalendar {
    constructor() {
        this.events = []
    }

    book(start, end) {
        let flr = 0
        let ceil = this.events.length - 1
        while (flr <= ceil) {
            let mid = Math.floor((flr + ceil) / 2)
            const event = this.events[mid]
            const evtStart = event[0]
            const evtEnd = event[1]
            if (start >= evtEnd) {
                flr = mid + 1
            } else if (end <= evtStart) {
                ceil = mid - 1
            } else {
                return false
            }
        }
        this.events.splice(flr, 0, [start, end])
        return true
    }
}

const testCase = new MyCalendar()
console.log(testCase.book(5, 10))
console.log(testCase.book(7, 80))
console.log(testCase.book(11, 15))
console.log(testCase.book(2, 3))