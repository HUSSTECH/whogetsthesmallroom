var count = 0;
window.createinput = function(){
    field_area = document.getElementById('fields')
    var ul = document.createElement("ul");
    var input = document.createElement("input");
    input.id = 'field'+count;
    input.name = 'field'+count;
    input.type = "number";
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
    document.getElementById("nrooms").value = count;
    
    
}