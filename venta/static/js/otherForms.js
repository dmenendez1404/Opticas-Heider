/**
 * Created by Daniel on 12/12/2017.
 */
$('#sucursal-div').on('click', 'a', function () {
    name = $(this).attr('name');
    if (name == 'update-sucursal') {
        $('#type').val('edit');
        $.ajax({
            type: "GET",
            url: "/api/sucursales/" + $("#sucursal").val() + "/",
        }).done(function (data) {
            $('#nombre-sucursal').val(data.nombre);
            $('#direccion-sucursal').val(data.direccion);
        });
    }
    else {
        $('#nombre-sucursal').val("");
        $('#direccion-sucursal').val("");
    }
});

$('#form-sucursal').on('submit', function (e) {
    e.preventDefault();
    $this = $(this);
    type = $('#type').val();
    method = 'POST';
    url = '/api/sucursales/';
    if (type == 'edit') {
        method = 'PUT';
        url = '/api/sucursales/' + $('#sucursal').val() + '/';
    }
    $.ajax({
        url: url,
        type: method,
        data: $this.serialize(),
    }).success(function (data, textStatus, jqXHR) {
        initSucursal(data['id']);
        $('#addSucursal').modal('close');
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

$('#tipo-armazon-div').on('click', 'a', function () {
    name = $(this).attr('name');
    if (name == 'update-tipo-armazon') {
        $('#type').val('edit');
        $.ajax({
            type: "GET",
            url: "/api/tipoarmadura/" + $("#tipo_armazon").val() + "/",
        }).done(function (data) {
            $('#nombre-armadura').val(data.nombre);
            $('#descripcion-armadura').val(data.descripcion);
        });
    }
    else {
        $('#nombre-armadura').val("");
        $('#descripcion-armadura').val("");
    }
});

$('#form-tipo-armazon').on('submit', function (e) {
    e.preventDefault();
    $this = $(this);
    type = $('#type').val();
    method = 'POST';
    url = '/api/tipoarmadura/';
    if (type == 'edit') {
        method = 'PUT';
        url = '/api/tipoarmadura/' + $('#tipo_armazon').val() + '/';
    }
    $.ajax({
        url: url,
        type: method,
        data: $this.serialize(),
    }).success(function (data, textStatus, jqXHR) {
        initTipo_Armazon(data['id']);
        $('#addTipoArmazon').modal('close');
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

$('#tipo-montura-div').on('click', 'a', function () {
    name = $(this).attr('name');
    if (name == 'update-tipo-montura') {
        $('#type').val('edit');
        $.ajax({
            type: "GET",
            url: "/api/tipomontura/" + $("#tipo_montura").val() + "/",
        }).done(function (data) {
            $('#nombre-montura').val(data.nombre);
            $('#descripcion-montura').val(data.descripcion);
        });
    }
    else {
        $('#nombre-montura').val("");
        $('#descripcion-montura').val("");
    }
});

$('#form-tipo-montura').on('submit', function (e) {
    e.preventDefault();
    $this = $(this);
    type = $('#type').val();
    method = 'POST';
    url = '/api/tipomontura/';
    $('#type').val('edit');
    if (type == 'edit') {
        method = 'PUT';
        url = '/api/tipomontura/' + $('#tipo_montura').val() + '/';
    }
    $.ajax({
        url: url,
        type: method,
        data: $this.serialize(),
    }).success(function (data, textStatus, jqXHR) {
        initTipoMontura(data['id']);
        $('#addTipoMontura').modal('close');
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

$('#marca-div').on('click', 'a', function () {
    name = $(this).attr('name');
    if (name == 'update-marca') {
        $('#type').val('edit');
        $.ajax({
            type: "GET",
            url: "/api/marca/" + $("#marca").val() + "/",
        }).done(function (data) {
            $('#nombre-marca').val(data.nombre);
            $('#descripcion-marca').val(data.descripcion);
            $('#siglas-marca').val(data.siglas);
        });
    }
    else {
        $('#nombre-marca').val("");
        $('#descripcion-marca').val("");
        $('#siglas-marca').val(data.siglas);
    }
});

$('#form-marca').on('submit', function (e) {
    e.preventDefault();
    $this = $(this);
    method = 'POST';
    type = $('#type').val();
    url = '/api/marca/';
    if (type == 'edit') {
        method = 'PUT';
        url = '/api/marca/' + $('#marca').val() + '/';
    }
    $.ajax({
        url: url,
        type: method,
        data: $this.serialize(),
    }).success(function (data, textStatus, jqXHR) {
        initMarca(data['id']);
        $('#addMarca').modal('close');
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

$('#material-armadura-div').on('click', 'a', function () {
    name = $(this).attr('name');
    if (name == 'update-material-armadura') {
        $('#type').val('edit');
        $.ajax({
            type: "GET",
            url: "/api/materialarmadura/" + $("#material_armadura").val() + "/",
        }).done(function (data) {
            $('#nombre-material').val(data.nombre);
            $('#descripcion-material').val(data.descripcion);
        });
    }
    else {
        $('#nombre-material').val("");
        $('#descripcion-material').val("");
    }
});

$('#form-material-armadura').on('submit', function (e) {
    e.preventDefault();
    $this = $(this);
    type = $('#type').val();
    method = 'POST';
    url = '/api/materialarmadura/';
    if (type == 'edit') {
        method = 'PUT';
        url = '/api/materialarmadura/' + $('#material_armadura').val() + '/';
    }
    $.ajax({
        url: url,
        type: method,
        data: $this.serialize(),
    }).success(function (data, textStatus, jqXHR) {
        initMaterialArmadura(data['id']);
        $('#addMaterialArmadura').modal('close');
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

$('#color-div').on('click', 'a', function () {
    name = $(this).attr('name');
    if (name == 'update-color') {
        $('#type').val('edit');
        $.ajax({
            type: "GET",
            url: "/api/colores/" + $("#color").val() + "/",
        }).done(function (data) {
            $('#nombre-color').val(data.nombre);
            $('#siglas-color').val(data.siglas);
        });
    }
    else {
        $('#nombre-color').val("");
        $('#descripcion-color').val("");
    }
});
$('#form-color').on('submit', function (e) {
    e.preventDefault();
    $this = $(this);
    method = 'POST';
    url = '/api/colores/';
    type = $('#type').val();
    if (type = 'edit') {
        method = 'PUT';
        url = "/api/colores/" + $("#color").val() + "/";
    }
    $.ajax({
        url: url,
        type: method,
        data: $this.serialize(),
    }).success(function (data, textStatus, jqXHR) {
        initColor(data['id']);
        $('#addColor').modal('close');
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});