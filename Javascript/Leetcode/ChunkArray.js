var chunk = function(arr, size) {
    if(arr.length === 0 ){
        return arr
    }
    let answer = [];

    for (let i = 0; i < arr.length; i += size) {
        answer.push(arr.slice(i, i + size));
    }
    return answer

};
console.log(chunk([3,5,2,1,4],2))