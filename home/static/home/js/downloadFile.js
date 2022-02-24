function exportData(){
    
    /* Get the HTML data using Element by Id */
    var table = document.getElementById("tblStocks");
 
    /* Declaring array variable */
    var rows =[];
 
      //iterate through rows of table
    for(var i=0,row; row = table.rows[i];i++){
        //rows would be accessed using the "row" variable assigned in the for loop
        //Get each cell value/column from the row
        column2 = row.cells[1].innerText;
        column3 = row.cells[2].innerText;
        column4 = row.cells[3].innerText;
        column5 = row.cells[4].innerText;
      
 
    /* add a new records in the array */
        rows.push(
            [
                column2,
                column3,
                column4,
                column5,
             
            ]
        );
 
        }
        alert("Bạn có đồng ý tải tableProduct?")
        csvContent = "data:text/csv;charset=utf-8,";
         /* add the column delimiter as comma(,) and each row splitted by new line character (\n) */
        rows.forEach(function(rowArray){
            row = rowArray.join(",");
            csvContent += row + "\r\n";
        });
 
        /* create a hidden <a> DOM node and set its download attribute */
        var encodedUri = encodeURI(csvContent);
        var link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "Product.csv");
        document.body.appendChild(link);
         /* download the data file named "Stock_Price_Report.csv" */
        link.click();
}