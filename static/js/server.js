var count = 0;

function getInternetExplorerVersion()
// Returns the version of Internet Explorer or a -1
// (indicating the use of another browser).
{
  var rv = -1; // Return value assumes failure.
  if (navigator.appName == 'Microsoft Internet Explorer')
  {
    rv = 1;
  }
  return rv;
}

window.createinput = function(){
    var ver = getInternetExplorerVersion(); //Check if running IE
    field_area = document.getElementById('fields')
    var ul = document.createElement("ul");
    var input = document.createElement("input");
    input.id = 'field'+count;
    input.name = 'field'+count;
    if( ver === -1 ) //execute line if not IE
    {
        input.type = "number";
    }
    input.min = "0";
    input.step = "any";
    input.required = true; 

    ul.appendChild(input);
    field_area.appendChild(ul);
    
    //create the removal link
    var removalLink = document.createElement("button");
    removalLink.className = "btn btn-danger";

    removalLink.onclick = function(){
        this.parentNode.parentNode.removeChild(this.parentNode)
        count--
        document.getElementById("nrooms").value = count;   
    }
    var removalText = document.createTextNode('X');
    removalLink.appendChild(removalText);
    ul.appendChild(removalLink);

    count++  
}