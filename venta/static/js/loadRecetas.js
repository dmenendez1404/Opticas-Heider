
   function loadRecetas(id) {
            var myConvertedData = {};
            $('.option-recetas').remove();
            url = "/api/receta/";
            if (id)
                url = "/api/receta/?cliente=" + id;
            $.ajax({
                type: "GET",
                url: url,
            }).done(function (data) {
                $.each(data.data, function (index, value) {
                    myConvertedData[value.numero + " "] = null;
                });
                $('.chips-autocomplete-recetas').material_chip({
                    autocompleteOptions: {
                        data: myConvertedData,
                        minLength: 0
                    },
                });

                $('.chips-recetas').on('chip.add', function (e, chip) {
                    // you have the added chip here
                    //$('.option-tratamientos').remove();
                    i = 0;
                    $.each(data.data, function (index, value) {
                        if (chip.tag == value.numero) {
                            i++;
                            chip.id = value.id;
                            $('#SelectRecetas').append('<option selected class="option-recetas" value="' + value.id + '"/>');
                        }
                    });
                    console.log(i);
                    var data1 = $('.chips-autocomplete-recetas').material_chip('data');
                    if (chip.id == undefined) {
                        data1.splice(data1.length - 1, 1);
                    }
                    $('.chips-autocomplete-recetas').material_chip({
                        data: data1,
                        autocompleteOptions: {
                            data: myConvertedData,
                            minLength: 0
                        }
                    });
                    console.log(data1);
                });
                $('.chips-recetas').on('chip.delete', function (e, chip) {
                    // you have the added chip here
                    $('option.option-recetas[value="' + chip.id + '"]').remove();
                });
            });
        }