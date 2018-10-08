/**
 * Created by Daniel on 18/12/2017.
 */

            function initSucursalCristal(val) {
                $.ajax({
                    type: "GET",
                    url: "/api/sucursales",
                }).done(function (data) {
                    $('.option-sucursal').remove();
                    $.each(data.results, function (k, v) {
                        $('#sucursalCristal').append($('<option>', {
                            class: 'option-sucursal-cristal',
                            value: v.id,
                            text: v.nombre
                        }));
                    });
                    $('#sucursalCristal').material_select('destroy');
                    $('#sucursalCristal').val(val).change();
                    $('#sucursalCristal').material_select();

                });
            }

            function initModeloCristal(val) {
                $.ajax({
                    type: "GET",
                    url: "/api/modelo",
                }).done(function (data) {
                    $('.option-modelo-cristal').remove();
                    $.each(data.results, function (k, v) {
                        $('#modeloCristal').append($('<option>', {
                            class: 'option-modelo-cristal',
                            value: v.id,
                            text: v.nombre
                        }));
                    });
                    $('#modeloCristal').material_select('destroy');
                    $('#modeloCristal').val(val).change();
                    $('#modeloCristal').material_select();
                });
            }

            function initMaterialCristal(val) {
                $.ajax({
                    type: "GET",
                    url: "/api/materialcristal",
                }).done(function (data) {
                    $('.option-material-cristal').remove();
                    $.each(data.results, function (k, v) {
                        $('#materialCristal').append($('<option>', {
                            class: 'option-material-cristal',
                            value: v.id,
                            text: v.nombre
                        }));
                    });
                    $('#materialCristal').material_select('destroy');
                    $('#materialCristal').val(val).change();
                    $('#materialCristal').material_select();
                });
            }

            function initColorCristal(val) {
                $.ajax({
                    type: "GET",
                    url: "/api/colores",
                }).done(function (data) {
                    $('.option-color-cristal').remove();
                    $.each(data.results, function (k, v) {
                        $('#colorCristal').append($('<option>', {
                            class: 'option-color-cristal',
                            value: v.id,
                            text: v.nombre
                        }));
                    });
                    $('#colorCristal').material_select('destroy');
                    $('#colorCristal').val(val).change();
                    $('#colorCristal').material_select();
                });
            }

            function initMedCerca(val) {
                $('.option-med-cerca').remove();
                $texto = 'esf:' + val.esfera + ' cil:' + val.cilindro + ' eje:' + val.eje + ' pris:' + val.prisma + ' alt:' + val.altura;
                $('#medicion_cerca').append($('<option>', {
                    class: 'option-med-cerca',
                    value: val.id,
                    text: $texto
                }));

                $('#medicion_cerca').material_select('destroy');
                $('#medicion_cerca').val(val).change();
                $('#medicion_cerca').material_select();
            }

            function initMedLejos(val) {
                $('.option-med-lejos').remove();
                $texto = 'esf:' + val.esfera + ' cil:' + val.cilindro + ' eje:' + val.eje + ' pris:' + val.prisma + ' alt:' + val.altura;
                $('#medicion_lejos').append($('<option>', {
                    class: 'option-med-lejos',
                    value: val.id,
                    text: $texto
                }));

                $('#medicion_lejos').material_select('destroy');
                $('#medicion_lejos').val(val).change();
                $('#medicion_lejos').material_select();
            }


            function initLabCristal(val) {
                $('#laboratorioCristal').val(val).change();
                document.getElementById('laboratorioCristal').checked = false;
                if (val) {
                    document.getElementById('laboratorioCristal').checked = true;
                }
            }

            function loadTratamientos(tratamientos) {
                var myConvertedData = {};
                var myConvertedData2 = [];
                $('.option-tratamientos').remove();
                $.each(tratamientos, function (index, value) {
                    myConvertedData2[index] =
                        {
                            tag: value.nombre,
                            id: value.id
                        };
                    $('#SelectTratamientos').append('<option selected class="option-tratamientos" value="' + value.id + '"></option>')
                });
                $.ajax({
                    type: "GET",
                    url: "/api/tratamientocristal",
                }).done(function (data) {

                    $.each(data.results, function (index, value) {
                        myConvertedData[value.nombre] = null;

                    });
                    $('.chips-autocomplete').material_chip({
                        autocompleteOptions: {
                            data: myConvertedData,
                            limit: 5,
                            minLength: 0
                        },
                        data: myConvertedData2
                    });

                    $('.chips').on('chip.add', function (e, chip) {
                        // you have the added chip here
                        $('.option-tratamientos').remove();
                        $.each(data.results, function (index, value) {
                            if (chip.tag == value.nombre) {
                                chip.id = value.id;
                                $('#SelectTratamientos').append('<option selected class="option-tratamientos" value="' + value.id + '"></option>')
                            }
                        });

                        var data1 = $('.chips-autocomplete').material_chip('data');
                        if (chip.id == undefined) {
                            data1.splice(data1.length - 1, 1);
                        }
                        $('.chips-autocomplete').material_chip({
                            data: data1,
                            autocompleteOptions: {
                                data: myConvertedData,
                                limit: 5,
                                minLength: 0
                            }
                        });
                        //console.log(data1);
                    });
                    $('.chips').on('chip.delete', function (e, chip) {
                        // you have the added chip here
                        $('option.option-tratamientos[value="' + chip.id + '"]').remove();

                    });


                });

            }