$(document).ready(function() {

    // set cattegory buttons
    $('.category-text').on('click', function() {
                    // .mouseover(function() {

        $('.category-text').removeClass("active");
        $(this).addClass("active");
        var category_text  = this.id;
        $('#category-text-input').val(category_text);
    })

    // ajax search for category of posts
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

    $("#search").keyup(function(event){
        if(event.keyCode == 13){
            $("#buttonSearch").click();
        }
    });


    // ajax search for title of posts
    $('#buttonSearch').on('click',function () {

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
