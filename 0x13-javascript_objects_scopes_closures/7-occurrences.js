#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
    let occurrences = {};
    occurrences.searchElement = 0;
    for(element of list){
        if(element == searchElement){
            occurrences.searchElement++;
        }
    }
    return occurrences.searchElement;
}