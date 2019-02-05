// Author: Alessandro Alberga
// JavaScript (JQuery) specifically for content pages

// function called on browser load
$(function() {

    $('#comment_button').click(function(e){ // comment button trigger
        comment(e)
    })


    $("#new_comment").on('keypress', function (e) {    // comment enter trigger
        if (e.keyCode == 13) {
            comment(e)
            console.log('called')
        }
    });


    function comment (e) { // function performs the commenting
        e.preventDefault()
        url = window.location.pathname
        var comment = $('#new_comment').val()   // stored comment value

        if (comment.length > 0) {

        $.ajax({
            method: "POST",
            url: (url + 'new_comment/'),
            data: {
                'comment': comment,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function search_one_success(data) {
                $("#comments").html(data);
            },
                dataType: 'html'
        });

        }
    }
})