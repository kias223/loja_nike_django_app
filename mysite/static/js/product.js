const buyNowBtn = document.getElementById('buy-now-btn')
const addTocartBtn = document.getElementById('add-tocart-btn')

var alertContainer = document.querySelector('.alert-container')
var alertTextP = document.querySelector('.alert-text')
var modelo = document.querySelector('#modelo').innerHTML
var preco = document.querySelector('#preco').innerHTML
var checkboxes = document.getElementsByName('TM')
var sizeChoice
var alertText

const sizesFunc = () => {
    for (let checkbox of checkboxes) {
        checkbox.checked && (sizeChoice = checkbox.value)
    }
}

const alertFunc = () => {
    !sizeChoice && (alertText = 'escolha um tamanho')
    alertContainer.classList.add('start')

    setTimeout(() => {
        alertContainer.classList.remove('start')
    }, 3000)

    alertTextP.innerHTML = alertText
}

const buyFunc = () => {
    var date = new Date()
        .toDateString()
        .slice(4, -5)
    var dateDay = parseInt(date.slice(4)) + 2
    var dateDelete = `${date.slice(0, 4)}${dateDay}`

    const product_choice = {
        modelo: modelo,
        preço: preco,
        parcelas: parcelas,
        tamanho: sizeChoice,
        img_url: img,
        quantidade: '1',
        modelo_id: modelo_id,
        date_delete: dateDelete
    }

    if (sizeChoice) {
        if (!localStorage.getItem('productChoice' + id + sizeChoice)) {
            localStorage.setItem('productChoice' + id + sizeChoice, JSON.stringify(product_choice))
            window.location.reload()
        } else {
            alertText = 'produto já esta no carrinho'
            alertFunc()
        }
    }
}

buyNowBtn.addEventListener('click', () => {
    sizesFunc()
    !sizeChoice && alertFunc()
    buyFunc()
    sizeChoice && (window.location.href = "http://127.0.0.1:8000/cart/")
})

addTocartBtn.addEventListener('click', () => {
    sizesFunc()
    !sizeChoice && alertFunc()
    buyFunc()
})