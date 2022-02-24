function checkQuantily() {
    getQuantily = document.getElementById('quantily')
    quantily = getQuantily.value
    if(quantily < 0){
        document.getElementById('quantily').value = 0
    }
        
    }
