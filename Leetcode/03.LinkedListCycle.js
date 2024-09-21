var linkedListCycle = function (head) {
    let slow = head
    let fast = head
    while (slow !== null && fast === null && fast.next === null) {
        slow = slow.next
        fast = slow.next.next
        if (slow === fast) {
         return true
        }
    }
    return false
}