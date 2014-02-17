var data = [
  {
          "Brouwerij":"'t Hofbrouwerijke in opdracht van Brouwerij Het Nest",
              "Freq":1
                    },
                      {
                              "Brouwerij":"'t Hofbrouwerijke voor bierfirma Montaignu",
                                  "Freq":1
                                        },
                                          {
                                                  "Brouwerij":"'t Hofbrouwerijke voor Brouwerij Montaigu",
                                                      "Freq":1
                                                            }];

console.log(data);
console.log(data[1]);
console.log(data[1].Brouwerij);

var w = 600;
var h = 600;
var bw = w / data.length;
var bh = h / 20;

for ( var i = 0; i < data.length; i++ ) {
  var rect = new Rectangle(i*bw, h, h-bw,data[i].Freq*bh)
  console.log(rect)
}



