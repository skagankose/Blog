$(document).ready(function() {

    // Set GeneralText buttons
    $('.text-type-adjuster').on('click', function() {
        $('#file-form').hide();
        $('.text-type-adjuster').removeClass("active");
        $(this).addClass("active");
        var item_type = this.id;
        $('#text-type-input').val(item_type);
        $('#text-form').show();
    })

    $('#text-cancel').on('click', function() {
        $('.text-type-adjuster').removeClass("active");
        $('#text-form').hide();
    })

    // Set GeneralFile buttons
    $('.file-type-adjuster').on('click', function() {
        $('#text-form').hide();
        $('.file-type-adjuster').removeClass("active");
        $(this).addClass("active");
        var file_type = this.id;
        $('#file-type-input').val(file_type);
        $('#file-form').show();
    })

    $('#file-cancel').on('click', function() {
        $('.file-type-adjuster').removeClass("active");
        $('#file-form').hide();
    })

})