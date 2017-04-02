var colours= ["red", "blue", "yellow", "purple", "green", "brown", "black", "white", "orange"];
//
var noLeds=7;
var degrees=10;
var ledWidth=2;
var ledGap=6;
var currColor="red";
var currColorBox="";

$(document).ready(function(){
    //Create colour array
    //Can add width adaptation later
    for(var i=0; i< colours.length; i++){
      var newColor = document.createElement( "div" );
      newColor.style.backgroundColor=colours[i];
      if(i==0){
        newColor.style.borderColor="grey";
        currColorBox=newColor;
      }
      $("#colour-frame").append( newColor);
    }
    var ratio=$('#led-frame').height()/$('#led-frame').width();
    for(var deg=0; deg< (360/degrees); deg++){
      for(var led=1; led<noLeds; led++){
        var newLed= document.createElement( "div" );
        var pos_x= 50-(ledWidth/2)+ ledGap*led*Math.cos(Math.PI *deg*degrees/180)*ratio;
        var pos_y= 50-(ledWidth/2)+ ledGap*led*Math.sin(Math.PI*deg*degrees/180);
       
        newLed.style.left=pos_x+"%";
        newLed.style.bottom=pos_y+"%";
        $('#led-frame').append( newLed );
      }
    }
    $("#led-frame div").hover(function(){

          this.style.backgroundColor=currColor;
          console.log("oh shit");

    });

    $("#colour-frame div").click(function(){
       currColor=this.style.backgroundColor;
       console.log(currColor);
       currColorBox.style.borderColor="black";
       this.style.borderColor="grey";
       currColorBox=this;
    });
    $("#submit").click(function(){
        console.log("here we go");
        var data=[];
        $( "#led-frame div").each(function( index ) {
          data.push(this.style.backgroundColor);
        });
        $.post("/", data);
    });

    
});
