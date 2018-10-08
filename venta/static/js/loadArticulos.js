
  function loadArticulos() {
            var myConvertedData = {};
            $('.option-articulos').remove();
            $.ajax({
                type: "GET",
                url: "/api/articulo",
            }).done(function (data) {
                $.each(data.results, function (index, value) {
                    myConvertedData[value.codigo + " "] = null;
                });
                $('.chips-autocomplete-articulos').material_chip({
                    autocompleteOptions: {
                        data: myConvertedData,
                        minLength: 0
                    },
                });

                $('.chips-articulos').on('chip.add', function (e, chip) {
                    // you have the added chip here
                    // $('.option-tratamientos').remove();

                    $.each(data.results, function (index, value) {
                        if (chip.tag == value.codigo) {
                            chip.id = value.id;
                            addArticulo(value);
                            $('#SelectArticulos').append('<option selected class="option-articulos" value="' + value.id + '"></option>');
                        }
                    });
                    var data1 = $('.chips-autocomplete-articulos').material_chip('data');
                    if (chip.id == undefined) {
                        data1.splice(data1.length - 1, 1);
                    }
                    $('.chips-autocomplete-articulos').material_chip({
                        data: data1,
                        autocompleteOptions: {
                            data: myConvertedData,
                            minLength: 0
                        }
                    });
                    //console.log(data1);
                });
                $('.chips-articulos').on('chip.delete', function (e, chip) {
                    // you have the added chip here
                    $('option.option-articulos[value="' + chip.id + '"]').remove();
                    costo = parseFloat($('#' + chip.id).children().eq(4).text());
                    console.log(costo);
                    addSubtotal(costo * -1);
                    $('#' + chip.id).remove();
                    $('#carrito').ajax.reload();
                });
            });
        }