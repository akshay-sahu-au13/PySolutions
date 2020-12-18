// Hamming Distance Algorithm
// Create a JavaScript program that generates the difference of two strings using
// Hamming distance algorithm.

function hammingDistance(str1,str2){

    var count = 0;
  
  
    if (str1.length === str2.length){
  
      for (var i = 0; i < str1.length; i++){
        if (str1[i].toLowerCase() != str2[i].toLowerCase()){
          count++;
        }
        else {
          continue;
        }
      }
    }
    else {
      console.log('Enter the string of equal length');
    }
    console.log(count);
  }
  
  var distance = hammingDistance('JavascriptWithAttainu', 'JavaPythonWithAttainu');
  