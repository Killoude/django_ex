function addRow(table) {
    // Get a reference to the table
    let tableRef = document.getElementById(table);
  
    // Insert a row at the end of the table
    let newRow = tableRef.insertRow(-1);
  
    // Insert a cell in the row at index 0
    let newCell = newRow.insertCell(0);
    let newCell2 = newRow.insertCell(1);
    let newCell3 = newRow.insertCell(2);
    //let newCell4 = newRow.insertCell(3);
    
    newCell.setAttribute("align","center");
    newCell2.setAttribute("align","center");
    newCell3.setAttribute("align","center");
    //newCell4.setAttribute("align","center");

    // Append a text node to the cell
   //let newText = document.createTextNode('New bottom row');
    let codeinput = document.createElement("INPUT");
    let qtyinput = document.createElement("INPUT");
    let pcsinput = document.createElement("INPUT");
    //let deletebutton = document.createElement("BUTTON");

    codeinput.setAttribute("type","text");
    codeinput.setAttribute("name","productcode[]");
    codeinput.setAttribute("class", "autoc");
    codeinput.setAttribute("style","width:100px");
        
    qtyinput.setAttribute("type","text");
    qtyinput.setAttribute("name","qtyinput[]");
    qtyinput.setAttribute("class", "form-control");
    qtyinput.setAttribute("style","width:100px");

    pcsinput.setAttribute("type","text");
    pcsinput.setAttribute("name","pcsinput[]");
    pcsinput.setAttribute("class", "form-control");
    pcsinput.setAttribute("style","width:100px");

    // deletebutton.setAttribute("class", "btn btn-danger");
    // deletebutton.setAttribute("style","width:100px");
    // deletebutton.innerText)

    newCell.appendChild(codeinput);
    newCell2.appendChild(qtyinput);
    newCell3.appendChild(pcsinput);

    //newCell.autocomplete
    //newCell4.appendChild(deletebutton);

  }
  
function deleteRow(table) {
    // Get a reference to the table
    let tableRef = document.getElementById(table);
    // Insert a row at the end of the table
    let newRow = tableRef.deleteRow(-1);
  }
  