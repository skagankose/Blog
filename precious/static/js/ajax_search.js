$(document).ready(function() {

    // Set Category buttons
    $('.category-text').on('click', function() {
                    // .mouseover(function() {

        $('.category-text').removeClass("active");
        $(this).addClass("active");
        var category_text  = this.id;
        $('#category-text-input').val(category_text);
    })

    // Ajax search for Category of Post
    $('.category-text').on('click', function() {
        $.ajax( {

            type: "POST",
            url: "/category_text_search/",
            data: {
                    'category-text-search' : $('#category-text-input').val(),
                    csrfmiddlewaretoken: $('#csrftoken').val()
            }, 
            success: function SearchSuccess(data, textStatus, jqXHR) {
                     $('#category-search-results').html(data); 
            },   
            dataType: 'html' 
        });
    });


    // Ajax search for title of Post
    $('#search').on('keyup',function () {

        $.ajax( {

            type: "POST",
            url: "/post_search/",
            data: {
                    'text_search' : $('#search').val(),
                    csrfmiddlewaretoken: $('#csrftoken').val()
            }, 
            success: function SearchSuccess(data, textStatus, jqXHR) {
                     $('#search_results').html(data); 
            },   
            dataType: 'html' 
        });
    });

});

