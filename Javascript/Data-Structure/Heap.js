class Heap{
        #heap = []
        insert(value){
            this.#heap.push(value);
            let current =  this.#heap.length - 1;
            while (current > 0 && this.#heap[current] > this.#heap[this.#parent(current)]){
                this.#swap(current , this.#parent(current))
                current = this.#parent(current)
            }
        }

        remove(){
            if (this.#heap.length === 0){
                return null
            }
            if (this.#heap.length === 1){
                return this.#heap.pop()
            }

            const maxValue = this.#heap[0];
            this.#heap[0] = this.#heap.pop()

            this.#sinkDown(0)
            return maxValue
        }


        #sinkDown(index)   {
            let maxIndex = index
            let size = this.#heap.length

            while (true){
                let left =this.#leftChild(index)
                let right = this.#rightChild(index)
                if (this.#heap[left] > this.#heap[maxIndex]  && left < size){
                    maxIndex = left
                }
                if (this.#heap[right] > this.#heap[maxIndex] && right < size){
                    maxIndex = right
                }
                if (maxIndex !== index){
                    this.#swap(index, maxIndex)
                    index  = maxIndex
                }else{
                    return
                }
            }
        }

        getHeap(){
            return[...this.#heap] // so reason we are using ... this give us copy of the array,
        }
        #leftChild(index){
            return 2 * index + 1
        }
        #rightChild(index){
            return 2 * index + 2
        }
        #parent(index){
            return Math.floor((index -1) / 2)
        }
        #swap(index1, index2){
            [this.#heap[index1], this.#heap[index2]] = [this.#heap[index2], this.#heap[index1]]
        }

    }


    const myHeap = new Heap()
    myHeap.insert(99)
    myHeap.insert(72)
    myHeap.insert(61)
    myHeap.insert(58)
    console.log(myHeap.getHeap())

    myHeap.insert(100)
    console.log(myHeap.getHeap())


    myHeap.insert(75)
    console.log(myHeap.getHeap())
    console.log("Remove")

    myHeap.remove()
    console.log(myHeap.getHeap())
