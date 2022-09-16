function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function like(type, id, url) {
    $.ajax({
        type: 'POST',
        url: url,
        data: { 'type': type, 'id': id },
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        success: function (response) {
            if (document.getElementById(type[0] + 'like' + id).value == 'Like') {
                document.getElementById(type[0] + 'like' + id).value = 'Liked'
                document.getElementById(type[0] + 'like' + id).src = DJANGO_STATIC_URL + 'images/liked.png'
                document.getElementById(type[0] + 'likecount' + id).innerHTML = Number(document.getElementById(type[0] + 'likecount' + id).innerHTML) + 1
                if (document.getElementById(type[0] + 'dislike' + id).value == 'Disliked') {
                    document.getElementById(type[0] + 'dislike' + id).value = 'Dislike'
                    document.getElementById(type[0] + 'dislike' + id).src = DJANGO_STATIC_URL + 'images/dislike.png'
                    document.getElementById(type[0] + 'dislikecount' + id).innerHTML = Number(document.getElementById(type[0] + 'dislikecount' + id).innerHTML) - 1
                }
            }
            else {
                document.getElementById(type[0] + 'like' + id).value = 'Like'
                document.getElementById(type[0] + 'like' + id).src = DJANGO_STATIC_URL + 'images/like.png'
                document.getElementById(type[0] + 'likecount' + id).innerHTML = Number(document.getElementById(type[0] + 'likecount' + id).innerHTML) - 1
            }
        }
    })
}


function dislike(type, id, url) {
    $.ajax({
        type: 'POST',
        url: url,
        data: { 'type': type, 'id': id },
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        success: function (response) {
            if (document.getElementById(type[0] + 'dislike' + id).value == 'Dislike') {
                document.getElementById(type[0] + 'dislike' + id).value = 'Disliked'
                document.getElementById(type[0] + 'dislike' + id).src = DJANGO_STATIC_URL + 'images/disliked.png'
                document.getElementById(type[0] + 'dislikecount' + id).innerHTML = Number(document.getElementById(type[0] + 'dislikecount' + id).innerHTML) + 1
                if (document.getElementById(type[0] + 'like' + id).value == 'Liked') {
                    document.getElementById(type[0] + 'like' + id).value = 'Like'
                    document.getElementById(type[0] + 'like' + id).src = DJANGO_STATIC_URL + 'images/like.png'
                    document.getElementById(type[0] + 'likecount' + id).innerHTML = Number(document.getElementById(type[0] + 'likecount' + id).innerHTML) - 1
                }
            }
            else {
                document.getElementById(type[0] + 'dislike' + id).value = 'Dislike'
                document.getElementById(type[0] + 'dislike' + id).src = DJANGO_STATIC_URL + 'images/dislike.png'
                document.getElementById(type[0] + 'dislikecount' + id).innerHTML = Number(document.getElementById(type[0] + 'dislikecount' + id).innerHTML) - 1
            }
        }
    })
}