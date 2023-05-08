const inputFile = document.querySelector('#id_img_produto')
const pictureImage = document.querySelector('.picture__image')
const pictureimageTxt = '<img src="../media/{{ post.img_produto }}" width="200">'
pictureImage.innerHTML = pictureimageTxt

inputFile.addEventListener('change', function (e) {
    const inputTarget = e.target
    const file = inputTarget.files[0]

    if (file) {
        const reader = new FileReader()

        reader.addEventListener('load', function (e) {
            const readerTarget = e.target

            const img = document.createElement('img')
            img.src = readerTarget.result
            img.classList.add('picture__img')

            pictureImage.innerHTML = ''
            pictureImage.appendChild(img)
        })

        reader.readAsDataURL(file)
    } else {
        pictureImage.innerHTML = pictureimageTxt
    }
})


document.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        const submit_btn = document.querySelector('#btn_submit')
        submit_btn.click()
    }
})

// const alert_icon = '<i class="fas fa-exclamation-triangle"></i>'
// const submit_btn = document.querySelector('#btn_submit')
// const top_alert_text = document.querySelector('#top_alert_text')

// var alert_text = document.querySelectorAll('.alert')
// var form_input = document.querySelectorAll('.input_form')

// submit_btn.onclick = function () {
//     if (inputFile.value == '') {
//         event.preventDefault()
//         alert_text[0].innerHTML = alert_icon
//     } else {
//         alert_text[0].innerHTML = null
//     }
// }