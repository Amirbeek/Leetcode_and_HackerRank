 class Graph {
    constructor() {
      this.adjacencyList = {}
    }
    addVertex(vertex){
      if (!this.adjacencyList[vertex]){
         this.adjacencyList[vertex] = []
         return true
      }
      return  false
    }
    addEdge(v1, v2){
      if (this.adjacencyList[v1] && this.adjacencyList[v2]){
         this.adjacencyList[v1].push(v2)
         this.adjacencyList[v2].push(v1);
         return true
      }
      return false
    }
    removeEdge(v1, v2){
     if (this.adjacencyList[v1] && this.adjacencyList[v2]){
       this.adjacencyList[v1] = this.adjacencyList[v1].filter(v =>  v !== v2)
       this.adjacencyList[v2] = this.adjacencyList[v2].filter(v =>  v !== v1)
       return true
     }
     return false
    }
    removeVertex(vertex){
      if (!this.adjacencyList[vertex]) return undefined
      while(this.adjacencyList[vertex].length){
        let temp = this.adjacencyList[vertex].pop()
        this.removeEdge(vertex, temp)
      }
      delete this.adjacencyList[vertex]
      return this
    }

  }

  const vertex = new  Graph();
  vertex.addVertex('A');
  vertex.addVertex('B');
  vertex.addVertex('C');
  vertex.addEdge('A','B')
  vertex.addEdge('B','C')
  vertex.addEdge('C','A')
  vertex.removeEdge('A','B')


  console.log(vertex)