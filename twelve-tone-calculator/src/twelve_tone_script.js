/*****************************************************************************
* Calculate the entire table given the initial row 
******************************************************************************/
function twelveToneCalculation(row, start) {
    // Begin by removing start from every member of the row to generate the easy 
    // 0 - 11 for calculation
    let chosenRow = row.map(musicalSubtraction, start);
    // Find inversion row
    let inversion = findInversion(chosenRow);
    // Calculate the full grid using the original and inversion rows
    let finishedGrid = generateTable(chosenRow, inversion, row, start);
    // Return the completed 2D array for display with React
    return finishedGrid;
}

/*****************************************************************************
* Find the inversion of P0 to generate the starting pitches of the other rows
******************************************************************************/
function findInversion(toneRow) {
    let inversion = Array(toneRow.length);
    inversion[0] = toneRow[0];
    for (let i = 1; i < toneRow.length; i++ ) {
        inversion[i] = 12 - toneRow[i];
    }
    return inversion;
}

/*****************************************************************************
* Modulus for note pitch subtraction
******************************************************************************/
function musicalSubtraction(pitch1, pitch2) {
    return (pitch1 - pitch2) % 12;
}

/*****************************************************************************
* Modulus for note pitch addition
******************************************************************************/
function musicalAddition(pitch1, pitch2) {
    return (pitch1 + pitch2) % 12;
}

/*****************************************************************************
* Generate each of the additional rows based on their relation to P0
******************************************************************************/
function generateTable(chosenRow, inversion, originalRow, start) {
    // Create multidimensional array with the originalRow array taking place of table[0]
    table = Array(12);
    for (let i = 0; i < 12; i++) {
        if (i == 0)
            table [i] = originalRow;
        else
            table[i] = Array[12];
    }

    // Generate the table row by row
    for (let row = 1; row < 12; row++)
    {
        let difference = musicalAddition(chosenRow[0], inversion[row]);
        // Set the initial column of the row based on the inversion
        table[row][0] = musicalAddition(inversion[row], start);
        // Generate the row based on the difference between the current inversion 
        // point and the original row and save relative to the original row values
        for (let col = 1; col < 12; col++) {
            table[row][col] = musicalAddition(musicalAddition(chosenRow[col],difference), start);
        }
    }
    return table;
}
