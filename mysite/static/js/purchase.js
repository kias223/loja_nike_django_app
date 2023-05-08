
var cart = document.querySelector('#user_cart')
var totalParcels = document.querySelector('#total_parcels')
const send_btn = document.querySelector('#send_btn')
var parcelSelect = ''
var parcels = []
var totalPrice = 0
const perfil_data = document.querySelector('.perfil_data')
var alert01 = document.querySelector('.alert')


var Tamanho = ''
var Modelo = ''
var Quantidade = ''
var Img_url = ''
var Modelo_id = ''


if (perfil_data) {
    perfil_data.addEventListener('click', () => {
        perfil_data.classList.toggle('on')
        alert01.innerHTML.length > 0 && (alert01.innerHTML = '')
    })
}

for (let data in localStorage) {
    if (data.includes('productChoice')) {
        const user_choice = JSON.parse(localStorage.getItem(data))
        var price = parseFloat(
            user_choice.preço
                .replace('R$', '')
                .replace(',', '.')
        )

        parcels.push(user_choice.parcelas)
        totalPrice += user_choice.quantidade * price

        cart.innerHTML += `
            <div class="user_cart_container">
                <div class="user_cart_img">
                    <img src="${user_choice.img_url}" >
                    <p>${user_choice.preço}</p>
                </div>

                <div class="user_cart_props">
                    <p>${user_choice.modelo}</p>
                    <p>tamanho: ${user_choice.tamanho}</p>
                    <p>quantidade ${user_choice.quantidade}</p>
                </div>
            </div>
        `

        Tamanho += ',' + user_choice.tamanho
        Modelo += ',' + user_choice.modelo
        Quantidade += ',' + user_choice.quantidade
        Img_url += ',' + user_choice.img_url
        Modelo_id += ',' + user_choice.modelo_id
    }

}


var sum = 0
for (let parcel of parcels) {
    sum += parseInt(parcel)
}

parcels = parseInt(sum / parcels.length)

for (let i = 1; i <= parcels; i++) {
    var parcelas_value = (totalPrice / i)
        .toFixed(2)
        .replace('.', ',')

    parcelSelect += `<option value="${i}x de R$ ${parcelas_value}" >${i}x de R$ ${parcelas_value}</option>`
}


totalParcels.innerHTML = `
    <p>total: R$ ${totalPrice.toFixed(2).replace('.', ',')}</p>
    <p>em até
        <select id="product_parcels">
        ${parcelSelect}
        </select>
    </p>
`

var data_hora = new Date()
data_hora = `${data_hora.getDate()}/${(data_hora.getMonth() + 1).toString().padStart(2, '0')}/${data_hora.getFullYear()} ${data_hora.getHours()}:${data_hora.getMinutes().toString().padEnd(2, '0')}`


if (send_btn) {
    send_btn.onclick = function () {
        if (perfil_data.classList.contains('on') == true) {
            const token = document.getElementsByName('csrfmiddlewaretoken')[0].value

            const purchase_data = {
                tamanho: Tamanho.slice(1),
                img_url: Img_url.slice(1),
                modelo: Modelo.slice(1),
                modelo_id: Modelo_id.slice(1),
                preco_total: totalPrice.toFixed(2),
                valor_parcelas: product_parcels.value,
                quantidade: Quantidade.slice(1),
                user_name: user_name,
                user_id: parseInt(user_id),
                data_hora: data_hora
            }

            fetch('http://127.0.0.1:8000/adminstration/purchase-apiview/', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": token,
                },
                body: JSON.stringify(purchase_data),
            })


            localStorage.clear()
            window.location.href = "http://127.0.0.1:8000/"
        } else {
            alert01.innerHTML = '!confirme endereço'
        }
    }
}