$('#btn').click(function (){
    $.ajax('/add-post', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'text': $('#new-post').val(),
        },
        'success': function (data){
            document.getElementById('posts').innerHTML += `<h3>${data["post"]}</h3>`;
        }
    })
})
