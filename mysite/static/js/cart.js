var cartContainer = document.querySelector('#post_container')
var cartContent = ''

if (localStorage.length != 0) {
    for (let product in localStorage) {
        if (product.includes('productChoice')) {
            var date = new Date()
                .toDateString()
                .slice(4, -5)
            var productId = product
            product = localStorage.getItem(product)
            const productData = JSON.parse(product)

            productData.date_delete == date && (localStorage.removeItem(productId), window.location.reload())

            cartContent += `
            <section class="cart_container">
                <div class="img_product"><img src="${productData.img_url}" alt=""></div>
                <div class="props">
                    <a href="#" id = "${productId}">
                        <img src="/static/icons/trash-solid.svg" alt="">
                    </a>
                    <h1>${productData.modelo}</h1>
                    <p>${productData.preço}</p>
                    <h2>tamanho: ${productData.tamanho}</h2>
                    <div class="quant">
                        <button class="btn_subt"><i class="fas fa-minus" aria-hidden="true"></i></button>
                        <p class="quantN">${productData.quantidade}</p>
                        <button class="btn_sum"><i class="fas fa-plus" aria-hidden="true"></i></button>
                    </div>
                </div>
            </section>
            `
        }
    }
    document.querySelector('#post_container').style.display = 'flex'
}

cartContainer.innerHTML = cartContent
var totalPriceContent = document.querySelector('#total_price')
var totalPrice = 0

if (cartContent) {
    cartContent = document.querySelectorAll('.cart_container')

    cartContent.forEach(element => {
        localStorage.setItem('total_price', 0)
        const sumBtn = element.querySelector('.btn_sum')
        const subtBtn = element.querySelector('.btn_subt')
        const delBtn = element.querySelector('a')
        var productQuant = element.querySelector('.quantN')
        var productData = JSON.parse(localStorage.getItem(delBtn.id))
        var price = productData.preço
            .replace('R$', '')
            .replace(',', '.')

        totalPrice += parseFloat(productData.quantidade) * parseFloat(price)

        const totalPriceContentReajust = () => {
            totalPriceContent.innerHTML = 'R$ ' + totalPrice
                .toFixed(2)
                .replace('.', ',')
        }

        delBtn.addEventListener('click', () => {
            localStorage.removeItem(delBtn.id)
            window.location.reload(true)
        })

        sumBtn.addEventListener('click', () => {
            productQuant.innerHTML = parseInt(productQuant.innerHTML) + 1
            productData.quantidade = productQuant.innerHTML
            localStorage.setItem(delBtn.id, JSON.stringify(productData))
            totalPrice += parseFloat(price)
            totalPriceContentReajust()
        })

        subtBtn.addEventListener('click', () => {
            if (parseInt(productQuant.innerHTML) > 1) {
                productQuant.innerHTML = parseInt(productQuant.innerHTML) - 1
                productData.quantidade = productQuant.innerHTML
                localStorage.setItem(delBtn.id, JSON.stringify(productData))
                totalPrice -= parseFloat(price)
                totalPriceContentReajust()
            }
        })

        totalPriceContentReajust()
    })
} else {
    document.querySelector('main').style.display = 'none'
}