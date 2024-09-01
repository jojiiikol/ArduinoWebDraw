let COLS_SIZE = 8
let ROWS_SIZE = 8
let matrix = makeMatrix(COLS_SIZE, ROWS_SIZE)

function sendMatrix() {
    fetch("web", {
        method: "POST",
        headers: {
                    'Content-Type': 'application/json'
            },
        body: getMatrixValue()
    })
    .then(response => console.log(getMatrixValue()))
    .catch((error) => console.log(error));
}


function makeMatrix(rows, cols){
    let matrix = [];
    for (let row = 0; row < rows; row++) {
        matrix[row] = []
        for (let col = 0; col < cols; col++) {
            let button = document.createElement('input')
            button.setAttribute('type', 'checkbox')
            button.setAttribute('class', 'pixel')
            matrix[row][col] = button
        }
    }
    return matrix
}
function showMatrix() {
    let element = document.getElementById("matrix");
    for (let row = 0; row < ROWS_SIZE; row++) {
        for (let col = 0; col < COLS_SIZE; col++) {
            element.append(matrix[row][col]);
        }
        element.append(document.createElement('br'))
    }
}

function getMatrixValue() {
    var image = {};
    for (let row = 0; row < ROWS_SIZE; row++) {
        image[row] = [];
        for (let col = 0; col < COLS_SIZE; col++) {
            image[row].push((matrix[row][col].checked === true) ? 1 : 0)
        }
    }
    let jsonMatrix = {image};
    return JSON.stringify(jsonMatrix);
}


