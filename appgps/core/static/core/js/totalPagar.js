
function algoritmo() {
    let valor1 = $('#inputInicio').val(),
        valor2 = $('#inputSalida').val(),
        valor3 = $('#inputPrecio').val();
    if (valor1 >= 0 && valor2 >= 0)
        cobro = (valor2 - valor1);
    total = cobro * valor3
    document.formRegistro.totalPago.value = total;

}
