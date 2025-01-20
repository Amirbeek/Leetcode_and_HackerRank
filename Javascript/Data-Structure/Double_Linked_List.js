
 class Node {
     constructor(value ) {
            this.value = value;
            this.next = null
            this.prev = null
     }
 }

 class DoubleLinkedList {
     constructor(value) {
         const newNode = new Node(value);
         this.head  = newNode;
         this.tail = newNode;
         this.length = 1
     }
     push(value){
         const newNode = new Node(value);
         if (!this.head){
             this.head = newNode;
             this.tail = newNode;
         }else{
             this.tail.next = newNode
             newNode.prev = this.tail
             this.tail = newNode
         }
         this.length++
         return this
     }
    pop(){
        if (this.length === 0)return undefined
        let temp = this.tail;
        if (this.length === 1){
            this.head = null
            this.tail = null
        }else{
            this.tail = this.tail.prev
            this.tail.next = null;
            temp.prev = null
        }
        this.length--;
        return temp
    }
    unshift(value){
        const newNode = new Node(value);
        if (!this.head){
            this.head = newNode
            this.tail = newNode
        }else{
            newNode.next  = this.tail
            this.tail.prev = newNode
            this.head = newNode
        }
        this.length++
        return this
    }
    ///
    shift(){
        if (!this.head){
             return undefined
        }
        let  temp =  this.head
        if (this.length === 1){
            this.head = null
            this.tail = null
        }else{
            this.head = this.head.next
            this.head.prev= null
            temp.next = null
        }
        this.length--
        return this
    }
     get(index) {
         if (index < 0 || index >= this.length) return undefined; // fix the boundary check
         let temp;
         if (index < this.length / 2) {
             temp = this.head;
             for (let i = 0; i < index; i++) {
                 temp = temp.next;
             }
         } else {
             temp = this.tail;
             for (let i = this.length - 1; i > index; i--) { // fix the loop condition
                 temp = temp.prev;
             }
         }
         return temp;
     }

     set(index, value){
         let temp = this.get(index);
         if (temp){
             temp.value = value
             return true
         }
         return false

    }


    insert(index, value){
        if (index === 0) return this.unshift(value);
        if (index === this.length) return this.push(value)
        if (index < 0 || index >= this.length) return false
        const newNode = new Node(value);
        const before = this.get(value - 1)
        const after = before.next
        before.next = newNode
        newNode.next = after
        after.prev =newNode
        newNode.prev = before
        this.length++
        return true
    }
    remove(index){
        if (index === 0 )return this.shift()
        if (index === this.length-1) return this.pop()
        if (index < 0 || index >= this.length) return undefined

        const temp = this.get(index);

        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = null
        temp.prev = null

        this.length--
        return temp
    }
 }

 const newList = new DoubleLinkedList(0);
 newList.push(1);
 newList.push(3);
 newList.push(4);
 newList.push(9);
 // console.log(newList/;
 console.log(newList.shift())
