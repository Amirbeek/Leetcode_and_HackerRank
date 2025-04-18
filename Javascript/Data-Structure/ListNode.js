
 class Node {
     constructor(value ) {
        this.value = value;
        this.next = null
     }
 }

 class LinkedList {
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
             this.tail = this.head;
         }else{
             this.tail.next = newNode
             this.tail = newNode
         }
         this.length++
         return this
     }
     pop(){
         //Agar list empty bolsa
        if (!this.head ){
            return undefined
         }


        // temp va pre elementiga head valuesini beramiz
        let temp = this.head;
        let pre = this.head;

        // temp next false bolgungacham loop ishlidi yani null bolganigacham
        while(temp.next){
            //buyerda pre elementiga temp value sini beramaniz
            pre = temp;

            // buyerda tempni keyingi elementni next valusini tekshirishga jonatdik
            temp = temp.next
        }
        // buyerda tailni pre qiymatini berib , next tiga null ni beramiz , bu bizga taildan keyingi valuni yoqotishimizga imkon  berad
        this.tail =  pre;
        this.tail.next = null;
        this.length--
        if (this.length === 0){
            this.head = null
            this.tail = null
        }
        return temp
     }


     unshift(value){
         const newNode = new Node(value);
         if (!this.head){
             this.head = newNode
             this.tail = newNode
         }else {
             // newNode.next = this.head;
             // this.head = newNode
             let temp = this.head;
             this.head = newNode;
             this.head.next = temp;
         }

         this.length++
         return this
     }
     shift(){
         if (!this.head)return undefined;
         //head ni saqladik
         let temp = this.head;
         // bu yerda head this.head ni keyingi valusiga teng boldi
         this.head = this.head.next;
         // bu yerda length kamaytirildi
         this.length--
         //agar size 0 ga teng bolsa tail null boladi
         if (this.length === 0){
             this.tail = null
         }
         // va temp next null bladi
         temp.next = null
         return temp
     }
     get(index){
         if (index < 0 || index >= this.length){
             return undefined
         }
         let temp = this.head
         for (let i = 0; i < index; i++) {
             temp = temp.next
         }
         return temp
     }
     middle(){
         const middle = Math.floor((this.length-1) /2);
         console.log(middle);
         let temp = this.head
         for (let i  = 0 ; i < middle; i++){
             temp = temp.next;
             if (i === middle-1){
                 this.head = temp.next
                 this.length = middle
             }
         }
         return this
     }
     set(index , value){
         let temp = this.get(index);
         if (temp){
             temp.value = value
             return true
         }
         return false;
     }
     insert(index, value) {
         if (index < 0 || index > this.length) return false;
         if (index === 0) return !!this.unshift(value); // Add to the start
         if (index === this.length) return !!this.push(value); // Add to the end

         // Insert in the middle
         const newNode = new Node(value);
         const prev = this.get(index - 1); // Get the previous node

         if (!prev) return false; // This handles cases where `get` returns null/undefined

         newNode.next = prev.next; // Set the new node's next to be the previous node's next
         prev.next = newNode; // Set the previous node's next to be the new node
         this.length++;
         return true;
     }

     remove(index){
         if (index  === 0) return this.shift();
         if (index === this.length -1)  return  this.pop();
         if (index < 0 || index > this.length) return false;

         const before = this.get(index - 1);
         const temp = before.next;

         before.next = temp.next
         temp.next = null;

         this.length--;
         return temp;
     }
     reverse(){
         let prev = null;
         let temp = this.head;
         this.head = this.tail;
         this.tail = temp;
         let next = temp.next;


         for (let i = 0; i < this.length; i++) {
             next = temp.next;
             temp.next = prev;
             prev = temp;
             temp = next;
         }
         return this
     }
     findMiddleNode(){
         if(this.length === 0){
             return  null
         }
         if(this.length === 1){
             return this.head
         }
         let slow = this.head;
         let fast = this.head;
         while(fast.next){
             slow = slow.next;
             fast = slow.next;
         }
         return slow
     }

     hasLoop(){
         if(this.length === 0 || this.length === 1 ){
             return false
         }

         let slow = this.head;
         let fast = this.head;


         while(slow != null
         && fast != null
         && fast.next != null){
             slow = slow.next
             fast = fast.next.next

             if(slow === fast){
                 return true
             }
         }

         return false
     }

     findKthFromEnd(k){
         if(k === 0 || k < 0){
             return null
         }
         if(k === 1){
             return this.tail.value
         }
         let temp = this.head;
         let pre = this.head;
         let num = 0;
         while(temp.next){
             temp = temp.next;
             if(num === k-1){
                 pre = pre.next;
             }
             num++;
         }
         return pre.value
     }

 }

 const newList = new LinkedList(0);
 newList.push(1);
 newList.push(3);
 newList.push(4);
 newList.push(9);
 console.log(newList.findKthFromEnd(3));
 console.log(newList)
