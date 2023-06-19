#!/usr/bin/node
esrever = function (list){
    let j = list.length-1;
    let i = 0;
        while(i < j){
            let temp = list[i];
            list[i] = list[j];
            list[j] = temp;
            i++;
            j--;
        }
        return list;
}