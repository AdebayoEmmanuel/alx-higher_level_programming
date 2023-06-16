exports.logMe = function (item){
    this.count = 0;
    let cnt = this.count;
    let obj = {cnt : item};
    this.count++;
    return obj

}