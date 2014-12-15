function Aquabrim(){	// constructor
	this.config = {};	// configuration object.
}
Aquabrim.prototype.fillWaterLevelTank = function(waterLevel,elementReference){

}
Aquabrim.prototype.fillWaterLevelGrid = function(elementReference){
	$(elementReference).find("span").each(function(){
		var fillgridto = $(this).attr("fillgridto");
		if(fillgridto){
			$(this).css("width",fillgridto);	// fill gradient width.
		}
	})
}
Aquabrim.prototype.Blink = function(element){
	setInterval(function(){
		$(element).fadeOut(50);
		$(element).fadeIn(50);
	},800);
}
var objAquaBrim = new Aquabrim();
objAquaBrim.fillWaterLevelGrid("#gridLevelTankLevel");
objAquaBrim.Blink('.blink');