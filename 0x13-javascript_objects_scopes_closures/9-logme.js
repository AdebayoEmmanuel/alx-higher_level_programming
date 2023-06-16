exports.logMe = function (item){
    this.prototype.count = 0;
    let cnt = this.prototype.count;
    let obj = {cnt : item};
    this.prototype.count++;
    return obj

}