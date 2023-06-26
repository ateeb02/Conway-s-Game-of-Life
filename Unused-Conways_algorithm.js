export function define_array(rows, columns, element)
{
    let array = [];
    for (let i=0; i<rows; i++)
    {
        let temp = [];
        for (let j=0; j<columns; j++)
        {
            temp[j] = element;
        }
        array[i] = temp;
    }
    return array
}

//Displays the matrix in a readable structure
export function print_array(array)
{
    for (let i=0; i<array.length; i++)
    {
        console.log(array[i])
    }
}

//Access any element of the data structure
export function access(row, column, array)
{
    let temp = array[row];
    return temp[column];
}

//Edit a specific element of the daata structure
export function edit(row, column, array, replace)
{
    let temp = array[row];
    temp[column] = replace;
}

//To check the neighbours of each element of matrix
export function check_neighbours(x, y, array)
{
    let rows = array.length;
    let columns = array[0].length;
    let counter = 0;
    if (x == 0 & y == 0) //Top left corner
    {
        counter += access(x+1, y, array);
        counter += access(x, y+1, array);
        counter += access(x+1, y+1, array);
    }

    else if (x == rows-1 & y == columns-1) //Bottom right corner
    {
        counter += access(x-1, y, array);
        counter += access(x, y-1, array);
        counter += access(x-1, y-1, array);
    }

    else if (x == 0 & y != 0 & y != columns-1) //Top edge
    {
        counter += access(x+1, y, array);
        counter += access(x, y+1, array);
        counter += access(x, y-1, array);
        counter += access(x+1, y-1, array);
        counter += access(x+1, y+1, array);
    }

    else if (x == rows-1 & y != 0 & y != columns-1) //Bottom edge
    {
        counter += access(x-1, y, array);
        counter += access(x, y+1, array);
        counter += access(x, y-1, array);
        counter += access(x-1, y-1, array);
        counter += access(x-1, y+1, array);
    }

    else if (x != 0 & x != rows-1 & y == 0) //Left edge
    {
        counter += access(x-1, y, array);
        counter += access(x-1, y+1, array);
        counter += access(x, y+1, array);
        counter += access(x+1, y, array);
        counter += access(x+1, y+1, array);
    }

    else if (x != 0 & x != rows-1 & y == columns-1) //Right edge
    {
        counter += access(x-1, y, array);
        counter += access(x-1, y-1, array);
        counter += access(x, y-1, array);
        counter += access(x+1, y, array);
        counter += access(x+1, y-1, array);
    }

    else if (x != 0 & x != rows-1 & y != 0 & y != columns-1) //Entire middle part
    {
        counter += access(x-1,y-1, array);
        counter += access(x-1,y, array);
        counter += access(x-1,y+1, array);
        counter += access(x,y-1, array);
        counter += access(x,y+1, array);
        counter += access(x+1,y-1, array);
        counter += access(x+1,y, array);
        counter += access(x+1,y+1, array);
    }

    return counter
}

//Scan each element for neighbours & store the data in a new matrix
export function scan(array)
{
    let rows = array.length;
    let columns = array[0].length;
    let result = define_array(rows,columns, 0);
    for (let i=0; i<rows; i++)
    {
        for (let j=0; j<columns; j++)
        {
            edit(i,j,result,check_neighbours(i,j,array));
        }
    }
    return result
}

//updates the array according to neighbour data
export function update(array)
{
    let rows = array.length;
    let columns = array[0].length;
    let data = [];
    data = scan(array);
    for (let i=0; i<rows; i++)
    {
        for (let j=0; j<columns; j++)
        {
            //Continuation
            if ((access(i,j,data) == 2 | 3) & access(i,j,array) == 1)
            {
                edit(i,j,array,1);
            }
            //Regeneration
            if (access(i,j,data) == 3 & access(i,j,array) ==  0)
            {
                edit(i,j,array,1);
            }
            //Over population
            if (access(i,j,data) < 2 | (access(i,j,data) > 3) & (access(i,j,array) == 1))
            {
                edit(i,j,array,0);
            }
        }
    }
}

