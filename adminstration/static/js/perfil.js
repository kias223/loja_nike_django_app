const cpf_input = document.querySelector('#id_cpf')
const cep_input = document.querySelector('#id_cep')
const telefone_input = document.querySelector('#id_numero_telefone')


cpf_input.addEventListener('keypress', (e) => {
    var input_length = cpf_input.value.length

    if (input_length == 3 | input_length == 7) {
        cpf_input.value += '.'
    }

    if (input_length === 11) {
        cpf_input.value += '-'
    }


    var cpf_validation = cpf_input.value.replace(/\.|-/g, '')
    console.log(typeof (e.key))
    var num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


    if (isNaN(e.key)) {
        e.preventDefault()
    }

})


cep_input.addEventListener('keypress', (e) => {
    var input_length = cep_input.value.length

    if (input_length === 5) {
        cep_input.value += '-'
    }

    var cep_validation = cep_input.value.replace('-', '')

    if (isNaN(e.key)) {
        e.preventDefault()
    }

    if (isNaN(cep_validation)) {
        e.preventDefault()
    }

})

telefone_input.addEventListener('keypress', (e) => {
    var input_length = telefone_input.value.length

    if (input_length == 0) {
        telefone_input.value += '('
    }

    if (input_length == 3) {
        telefone_input.value += ') '
    }

    if (input_length == 9) {
        telefone_input.value += '-'
    }

    var telefone_validation = telefone_input.value
        .replace('(', '')
        .replace(') ', '')
        .replace('-', '')

    if (isNaN(telefone_validation)) {
        e.preventDefault()
    }

})
