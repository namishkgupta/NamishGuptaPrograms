var avg17 = getColumn("US Household Income", "2017 Average Income");
var avg18 = getColumn("US Household Income", "2018 Average Income");
var med17 = getColumn("US Household Income", "2017 Median Income");
var med18 = getColumn("US Household Income", "2018 Median income");
var change = getColumn("US Household Income","Percent change in real median income ");
var options = getColumn("US Household Income", "Characteristic of Homeowner");
var val17 = '';
var val18 = '';
setProperty("incomeSelector", "options", options);
var similar = 0;

function close(number, list) {
  var smallestDiff = Math.abs(number - list[0]);
  var closest = 0;
  for (var i = 1; i < list.length; i++) {
    var currentDiff = Math.abs(number - list[i]);
    if (currentDiff < smallestDiff) {
      smallestDiff = currentDiff;
      closest = i;
    }
  }
  similar = list[closest];
}








onEvent("incomeSelector", "change", function( ) {
	var index = options.indexOf(getText('incomeSelector'));
	setText("2017Avg",'$'+avg17[index]);
	setText("2017Med",'$'+med17[index]);
	setText("2018Avg",'$'+avg18[index]);
	setText("2018Med",'$'+med18[index]);
	setText("percentChange",change[index]+'% Change');

	
});

onEvent("calc", "click", function( ) {
  val17 = getText("Own2017");
  val18 = getText("Own2018");
	var diff = (Number(val17)-Number(val18));
  var div = (diff/Number(val17));
  var final = -1*(div * 100);
  if(final>0){
    setText("change",'+' + final.toString()+'%');
  }
  else{
    setText("change",final.toString()+'%');
  }
  
});

onEvent("calc2", "click", function( ) {
  val17 = getText("secondOwn17");
  val18 = getText("secondOwn18");
	var diff = (Number(val17)-Number(val18));
  var div = (diff/Number(val17));
  var final = -1*(div * 100);
  if(final>0){
    setText("change2",'+' + final.toString()+'%');
  }
  else{
    setText("change2",final.toString()+'%');
  }
  close(val18,med18);
  
  //var index = med18.indexOf(similar);
  //var dem ="" + (options[index]);
  setText('demo','The closest Median 2018 income to yours is: '+'$'+similar);  
  
});
onEvent("next", "click", function( ) {
	setScreen("screen3");
});
onEvent("back", "click", function( ) {
	setScreen('screen1');
  
});