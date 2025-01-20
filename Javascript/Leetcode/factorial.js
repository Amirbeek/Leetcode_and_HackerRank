function fuc(n){
    if (n === 1)  return 1
    return n * fuc(n-1)
}

console.log(fuc(4))