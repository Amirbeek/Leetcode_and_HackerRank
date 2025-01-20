const coordinates = [[0,0],[0,1],[0,-1]];


const checkStraightLine = function(coordinates) {
    let  first = coordinates[0][0] + 1;
    let second = coordinates[0][1] + 1;
    let result = false;
    for (let x = 0; x < coordinates.length; x++) {
        let F = coordinates[x][0];
        let S = coordinates[x][1];
        if (x >= 1 ){
            console.log(F + "===" + first + "  " + S + "===="+ second)
            // console.log(F === first && S === second)
            if (F === first && S === second){
                first = coordinates[x][0] + 1;
                second = coordinates[x][1] +1;
                result = true;
            }else {
                result = false
            }
        }
    }
    return result
};
console.log(checkStraightLine(coordinates))