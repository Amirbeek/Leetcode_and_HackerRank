class HashTable {
    constructor(size = 7) {
      this.dataMap = new Array(size);
    }
    _hash(key) {
      let hash = 0;
      for (let i = 0; i < key.length; i++) {
        hash = (hash + key.charCodeAt(i) * 23) % this.dataMap.length;
      }
      return hash;
    }

    set(key, value) {
      let index = this._hash(key);
      // If the spot at this index is empty, create a new array to handle collisions
      if (!this.dataMap[index]) {
        this.dataMap[index] = [];
      }
      // Add the key-value pair
      this.dataMap[index].push([key, value]);
      return this
    }

    get(key){
      let index = this._hash(key)
      if (this.dataMap[index]){
        for (let i = 0; i < this.dataMap[index].length; i++) {
          if (this.dataMap[index][i][0] === key){
            return this.dataMap[index][i][1]
          }
        }
      }
      return undefined
    }
      getKey(key){
          let index = this._hash(key)
          let array = []
          if (this.dataMap[index]){
              for (let i = 0; i < this.dataMap[index].length; i++) {
                  if (this.dataMap[index][i][1] === key){
                      array.push(this.dataMap[index][i][0])
                  }
              }
          }
          return array
      }

    keys() {
      let allKeys = [];
      for (let i = 0; i < this.dataMap.length; i++) {
        // Only proceed if this.dataMap[i] exists (is not undefined)
        if (this.dataMap[i]) {
          for (let j = 0; j < this.dataMap[i].length; j++) {
            allKeys.push(this.dataMap[i][j][0]); // Push the key at index 0 of each key-value pair
          }
        }
      }
      return allKeys;
    }
    getValues() {
          return Array.from(this.dataMap.values());
      }
  }
  // O(N2)
  function itemInCommon(arr1, arr2) {
      for (let i = 0; i < arr1.length; i++) {
          for (let j = 0; j < arr2; j++) {
              if (arr1[i] === arr2[j]) return true
          }
      }
      return false
  }
  // O(N)
  function itemInCommon2(arr1, arr2) {
      let obj = {}
      for (let i = 0; i < arr1.length; i++) {
          obj[arr1[1]] = true
      }
      for (let i = 0; i < arr2.length; i++) {
          if (obj[arr2[j]]) return true
      }
      return false
  }


  function findDuplicates(arr) {
      if (arr.length === 0) {
          return [];
      }

      let numCount = new HashTable(arr.length - 1);

      for (let i = 0; i < arr.length; i++) {
          numCount.set(arr[i], (numCount.get(arr[i]) || 0) + 1);
      }

      return numCount.getKey(2); // Assuming `getKey` returns keys with a value of 2
  }
  // findDuplicates([1, 2, 3, 4, 4, 5, 6, 6])
  //   +=====================================================+
  //   |                WRITE YOUR CODE HERE                 |
  //   | Description:                                        |
  //   | - This function finds the first non-repeating       |
  //   |   character in a string.                            |
  //   |                                                     |
  //   | Return type: string/null                            |
  //   | - Returns the first non-repeating character if      |
  //   |   found, otherwise returns null.                    |
  //   |                                                     |
  //   | Tips:                                               |
  //   | - You can use either a Map or an object to count    |
  //   |   the occurrences of each character.                |
  //   | - Example with Map:                                 |
  //   |   charCounts.set(c, (charCounts.get(c) || 0) + 1);  |
  //   | - Example with object:                              |
  //   |   charCounts[c] = (charCounts[c] || 0) + 1;         |
  //   +=====================================================+

  function firstNonRepeatingChar(str) {
      if (str.length === 0) {
          return -1;
      }
      if (str.length === 1) {
          return str;
      }

      let charCounts = {};

      for (let i = 0; i < str.length; i++) {
          charCounts[str[i]] = (charCounts[str[i]] || 0) + 1;
      }

      for (let i = 0; i < str.length; i++) {
          if (charCounts[str[i]] === 1) {
              return i;
          }
      }

      return -1;
  }


  // console.log(firstNonRepeatingChar('aabbcde'))
  // findDuplicates([1, 2, 3, 4, 4, 5, 6, 6])
  let hasMap = new HashTable();

  function groupAnagrams(arr) {
      const hashTable = new HashTable();

      // Loop through each string in the input array
      for (let str of arr) {
          hashTable.set(str, str);
      }

      // Get and return the grouped anagrams
      return hashTable.getValues();
  }

  console.log(groupAnagrams(['abc', 'cab', 'bca', 'xyz', 'zyx']))
  // groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])

  // console.log(hasMap)/