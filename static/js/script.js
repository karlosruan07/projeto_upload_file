
function Mostar() {
    var nometxt = window.document.getElementById('nome')
    var impresso_txt = window.document.getElementById('impresso')
    
    var nome = String(nometxt.value)
    
    if (nometxt.value.length == 0) {
        window.alert('Entrada inválida, tente novamente !')
    } else {
        impresso_txt.innerHTML = `Seu nome é <strong>${nome}</strong>`
    }
    

}