 function binarySearch(arr, target) {
        let leftIndex = 0;
        let rightIndex = arr.length - 1;
        while (leftIndex <= rightIndex) {
            let middleIndex = Math.floor((rightIndex + leftIndex) / 2);
            console.log('left: ' + arr[leftIndex], " middle :" + arr[middleIndex], " last: " + arr[rightIndex])
            if (target === arr[middleIndex]){
                return middleIndex;
            }
            if (target < arr[middleIndex]){
                rightIndex = middleIndex - 1;
            }else{
                leftIndex  = middleIndex + 1;
            }
        }
        return -1;
    }

    console.log(binarySearch([-5,1,2,3,5,7,10],10));
    console.log(binarySearch([0,1,2,3,5,7,10],5));
    console.log(binarySearch([0,1,2,3,5,7,10],2));