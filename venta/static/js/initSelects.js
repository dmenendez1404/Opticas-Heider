function initSucursal(val) {
    $.ajax({
        type: "GET",
        url: "/api/sucursales",
    }).done(function (data) {
        $('.option-sucursal').remove();
        $.each(data.results, function (k, v) {
            $('#sucursal').append($('<option>', {
                class: 'option-sucursal',
                value: v.id,
                text: v.nombre
            }));
        });
        $('#sucursal').material_select('destroy');
        $('#sucursal').val(val).change();
        $('#sucursal').material_select();

    });
}

function Sucursal(val) {
    $.ajax({
        type: "GET",
        url: "/api/sucursales",
    }).done(function (data) {
        $('.option-sucursal-' + val).remove();
        $.each(data.results, function (k, v) {
            $('#sucursal' + val).append($('<option>', {
                class: 'option-sucursal-' + val,
                value: v.id,
                text: v.nombre
            }));
        });
        $('#sucursal' + val).material_select('destroy');
        $('#sucursal' + val).material_select();

    });
}

function initColor(val) {
    $.ajax({
        type: "GET",
        url: "/api/colores",
    }).done(function (data) {
        $('.option-color').remove();
        $.each(data.results, function (k, v) {
            $('#color').append($('<option>', {
                class: 'option-color',
                value: v.id,
                text: v.nombre
            }));
        });
        $('#color').material_select('destroy');
        $('#color').val(val).change();
        $('#color').material_select();
    });
}

function Color(val) {
    $.ajax({
        type: "GET",
        url: "/api/colores",
    }).done(function (data) {
        $('.option-color-' + val).remove();
        $.each(data.results, function (k, v) {
            $('#color' + val).append($('<option>', {
                class: 'option-color-' + val,
                value: v.id,
                text: v.nombre
            }));
        });
        $('#color' + val).material_select('destroy');
        $('#color' + val).material_select();
    });
}


function initMarca(val) {
    $.ajax({
        type: "GET",
        url: "/api/marca",
    }).done(function (data) {
        $('.option-marca').remove();
        $.each(data.results, function (k, v) {
            $('#marca').append($('<option>', {
                class: 'option-marca',
                value: v.id,
                text: v.nombre
            }));
        });
        $('#marca').material_select('destroy');
        $('#marca').val(val).change();
        $('#marca').material_select();
    });
}


function initTipoMontura(val) {
    $.ajax({
        type: "GET",
        url: "/api/tipomontura",
    }).done(function (data) {
        $('.option-tipo-montura').remove();
        $.each(data.results, function (k, v) {
            $('#tipo_montura').append($('<option>', {
                class: 'option-tipo-montura',
                value: v.id,
                text: v.nombre
            }));
        });
        $('#tipo_montura').material_select('destroy');
        $('#tipo_montura').val(val).change();
        $('#tipo_montura').material_select();
    });
}

function initMaterialArmadura(val) {
    $.ajax({
        type: "GET",
        url: "/api/materialarmadura",
    }).done(function (data) {
        $('.option-material-armadura').remove();
        $.each(data.results, function (k, v) {
            $('#material_armadura').append($('<option>', {
                class: 'option-material-armadura',
                value: v.id,
                text: v.nombre
            }));
        });
        $('#material_armadura').material_select('destroy');
        $('#material_armadura').val(val).change();
        $('#material_armadura').material_select();
    });
}

function initTipo_Armazon(val) {
    $.ajax({
        type: "GET",
        url: "/api/tipoarmadura",
    }).done(function (data) {
        $('.option-tipo-armazon').remove();
        $.each(data.results, function (k, v) {
            $('#tipo_armazon').append($('<option>', {
                class: 'option-tipo-armazon',
                value: v.id,
                text: v.nombre
            }));
        });
        $('#tipo_armazon').material_select('destroy');
        $('#tipo_armazon').val(val).change();
        $('#tipo_armazon').material_select();
    });
}

function initCristalDer(val) {
    $.ajax({
        type: "GET",
        url: "/api/cristalesgraduados",
    }).done(function (data) {
        // $('.option-cristal-der').remove();
        $.each(data.data, function (j, v) {

            medicionC = v.medicion_cerca;

            if (medicionC != null) {
                medCer = "";
                trat = "";
                dist = 'Cer';
                medCer += dist + "-esf: " + medicionC.esfera + " eje: " + medicionC.eje + " pris: " + medicionC.prisma + "\n ";
            }

            medicionL = v.medicion_lejos;

            if (medicionL != null) {
                medLej="";
                trat = "";
                dist = 'Lej';
                medLej += dist + "-esf: " + medicionL.esfera + " eje: " + medicionL.eje + " pris: " + medicionL.prisma + "\n ";
            }

            $.each(v.tratamientos, function (f, val) {
                trat += val.siglas + " "
            });

            $('#cristalDer').append($('<option>', {
                class: 'option-cristal-der',
                value: v.id,
                text: v.modelo.siglas + " " + v.color.siglas + " (" + medCer + ") "+ " (" + medLej + ")" + " trat: " + trat
            }));
        });
        $('#cristalDer').material_select('destroy');
        $('#cristalDer').val(val).change();
        $('#cristalDer').material_select();
    });
}

// function initCristalIzq(val) {
//     $.ajax({
//         type: "GET",
//         url: "/api/cristalesgraduados",
//     }).done(function (data) {
//         // $('.option-cristal-izq').remove();
//         $.each(data.results, function (j, v) {
//             $.each(v.medicion, function (k, val) {
//                 med = "";
//                 trat = "";
//                 dist = 'Cer';
//                 if (val.lejos) {
//                     dist = 'Lej';
//                 }
//                 med += dist + "-esf: " + val.esfera + " eje: " + val.eje + " pris: " + val.prisma + "\n ";
//             });
//             $.each(v.tratamientos_cristal, function (f, val) {
//                 trat += val.siglas + " ";
//             });
//             $('#cristalIzq').append($('<option>', {
//                 class: 'option-cristal-izq',
//                 value: v.id,
//                 text: v.modelo.siglas + " " + v.color.siglas + " (" + med + ") trat: " + trat
//             }));
//             $('#cristalIzq').material_select('destroy');
//             $('#cristalIzq').val(val).change();
//             $('#cristalIzq').material_select();
//
//         });
//     });
// }


function initCristalIzq(val) {
    $.ajax({
        type: "GET",
        url: "/api/cristalesgraduados",
    }).done(function (data) {
        // $('.option-cristal-izq').remove();
        $.each(data.data, function (j, v) {
             $.each(data.data, function (j, v) {

            medicionC = v.medicion_cerca;



            if (medicionC != null) {
                medCer = "";
                trat = "";
                dist = 'Cer';
                medCer += dist + "-esf: " + medicionC.esfera + " eje: " + medicionC.eje + " pris: " + medicionC.prisma + "\n ";
            }

            medicionL = v.medicion_lejos;

            if (medicionL != null) {
                medLej="";
                trat = "";
                dist = 'Lej';
                medLej += dist + "-esf: " + medicionL.esfera + " eje: " + medicionL.eje + " pris: " + medicionL.prisma + "\n ";
            }

            $.each(v.tratamientos, function (f, val) {
                trat += val.siglas + " "
            });

            $('#cristalIzq').append($('<option>', {
                class: 'option-cristal-der',
                value: v.id,
                text: v.modelo.siglas + " " + v.color.siglas + " (" + medCer + ") "+ " (" + medLej + ")" + " trat: " + trat
            }));
        });
            $('#cristalIzq').material_select('destroy');
            $('#cristalIzq').val(val).change();
            $('#cristalIzq').material_select();

        });
    });
}


function initDoctor(val) {
    $.ajax({
        type: "GET",
        url: "/api/doctor",
    }).done(function (data) {
        $('.option-doctor').remove();
        $.each(data.results, function (k, v) {
            $('#doctor').append($('<option>', {
                class: 'option-doctor',
                value: v.id,
                text: v.usuario.first_name + " " + v.usuario.last_name
            }));
        });
        $('#doctor').material_select('destroy');
        $('#doctor').val(val).change();
        $('#doctor').material_select();
    });
}

function initCliente(val) {
    $.ajax({
        type: "GET",
        url: "/api/cliente",
    }).done(function (data) {
        $('.option-cliente').remove();
        $.each(data.results, function (k, v) {
            $('#cliente').append($('<option>', {
                class: 'option-cliente',
                value: v.id,
                text: v.usuario.first_name + " " + v.usuario.last_name
            }));
        });
        $('#cliente').material_select('destroy');
        $('#cliente').val(val).change();
        $('#cliente').material_select();
    });
}
