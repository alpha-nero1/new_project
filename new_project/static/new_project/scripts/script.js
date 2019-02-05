// Author: Alessandro Alberga
// General website JavaScript (JQuery)

// function called on browser load
$(function() {

    // function ensures the fixed navbar does not overlay site
    $('body').each(function(){
        $(this).css({
            'padding-top' : $('#navbar_main').height() + 'px'
        });
    });


    $('#down_vote').click(function(e){  // down vote called on page
        url = window.location.pathname
        e.preventDefault()

        $.ajax({
            type: "POST",
            url: url,
            data: {
                'amount': -1,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function search_one_success(data) {
                $('#votes').html(data);
            },
                dataType: 'html'
        });
    });

    $('#up_vote').click(function(e){    // up vote called on page
        url = window.location.pathname
        e.preventDefault()

        $.ajax({
            type: "POST",
            url: url,
            data: {
                'amount': 1,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function search_one_success(data) {
                $('#votes').html(data);
            },
                dataType: 'html'
        });
    });

    $('#search_button').click(function(e){  // main page search called
        e.preventDefault()
        if ($('#search_key').val().length > 0) {

        $.ajax({
            type: "POST",
            url: '/home/search/',
            data: {
                'search_key': $('#search_key').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function search_one_success(data) {

                $("#home_container").html(data);
                $("#todaysfeature").html('')
            },
                dataType: 'html'
        });

        }
    });

    $('#tag_button').click(function(e){ // update tags
        e.preventDefault()
        submit_tag()
    });

    $('#tags-input').tagsinput({    // defines what triggers input (13 is space)
        confirmKeys: [13, 188]
    })

    $('#tags-input input').on('keypress', function(e){  // runs on new tag input!
        if (e.keyCode == 13){
          e.keyCode = 188
          e.preventDefault()
        }
    })

function submit_tag() {
    url = '/account/tags/'

    $.ajax({
        type: "POST",
        url: url,
        data: {
            "tags": $('#tag_field').tagsinput('items'),
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function search_one_success(data) {
            $("#tags").html(data)
            $('#tag_field input').val('');
        },
            dataType: 'html'
    });
}

})

