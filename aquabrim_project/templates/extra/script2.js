{% load staticfiles %}
        var on_off=0;
		var hold=0;
		var voltage=0;
		var time_out=0;

		var lvl = 1;

		var voltage_val;
		var timeout_val;

		var x; //variable changes value to indicate which regulator is used first

		var image_empty;
		var image_full;
		var image_warning;

		//change the image from on to off and vice versa; also change their respective variable state -- 1 for 'on'/green, 0 for 'off'/red
		function diffImage(img) 
		{
		   if(img.src.match(/on/)) {
		   	
		   	img.src = "{% static  "css/off.png" %}";

		   	if(img.alt="on_off_status") { 
		   		on_off=0; 
		   		
		   	}
		   	if(img.alt="hold_status") { 
		   		hold=0;
		   		
		   		
		   	}
		   	if(img.alt="voltage") voltage=0;
		   	if(img.alt="time_out") time_out=0;
		   	
		   }

		   else 
		   	{
		   		
		   		img.src = "images/on.png";

		   		if(img.alt="on_off_status") {
		   			on_off=1;
		   			
		   		}
			    if(img.alt="hold_status") {
			    	hold=1;
			    	
		   		}
			   	if(img.alt="voltage") voltage=1;
			   	if(img.alt="time_out") time_out=1;
			   	
		   	}

		   	
	
		}

 $(document).ready(function(){

 	$('.cs_knob').trigger('configure', {
    	'change': function (v1) {
        voltage_val = v1;
    }
});
        $('.cs_knob2').trigger('configure', {
    	'change': function (v2) {
         timeout_val = v2;
         //alert('new value' + v2);
    }
});


function changeknobval(val){
                        $('.level')
                        .val(val)
                        .trigger('change');
                    }


        $(document).ready(
                                function() { changeknobval(lvl);
                                if(lvl==100)
								{
									image_warning = document.getElementById('warning'); 
									image_warning.src = "images/warning.png";
									image_full = document.getElementById('full'); 
									image_full.src = "images/on.png";
									

									
								} 

								else if(lvl==0)
								{
									image_empty = document.getElementById('empty'); 
									image_empty.src = "images/on.png";
								}
                    });




    });




/*if(on_off == 1)
{
	
	if(hold == 0)
	{
		if(voltage == 1)
		{
			$(".cs_knob").trigger('configure', {readOnly : false }); 
   			

		}
		if(time_out==1)
		{
			
   			$(".cs_knob2").trigger('configure', {readOnly : false });
		}
	}
}
*/

        

		
		
    	

    	



		


                    

