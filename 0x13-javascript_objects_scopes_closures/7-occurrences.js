#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
    let occurrences = {};
    occurrences.prototype.searchElement = 0;
    for(element of list){
        if(element == searchElement){
            occurrences.prototype.searchElement++;
        }
    }
    return occurrences.prototype.searchElement;
}