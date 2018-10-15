$(function() {
    $('.line').formset();
    var multiply = $(".multiply");

    var array = [];
    var sum = 0;
    $('.multiply').each(function() {
        array.push($(this).text());
    });

    for (var i = 0; i < array.length; i++) {
        var entry = parseFloat(array[i])
        sum += entry;
    }

    var total = ('#total');
    $(total).html(sum + " €");



    var totalProduct = $(".totalProduct");

    var arrayProduct = [];
    var sumProduct = 0;
    $('.totalProduct').each(function() {
        arrayProduct.push($(this).text());
    });


    for (var i = 0; i < arrayProduct.length; i++) {
        var entryProduct = parseFloat(arrayProduct[i])
        sumProduct += entryProduct;
    }

    var totalProd = ('#totalProd');
    $(totalProd).html(sumProduct);

    $.fn.editable.defaults.mode = 'inline';
    $('#client').editable({

    });

    $('#statut').editable({
        source:
              {value: 1, text: 'PROCESS'},
              {value: 2, text: 'RECALL'},
              {value: 3, text: 'DONE'}
           ]
    });

    $('#product').editable({

    });

    $('#quantity').editable({

    });
});
