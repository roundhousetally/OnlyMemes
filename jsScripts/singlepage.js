let profile = window.location.href;
profile = profile.slice(profile.lastIndexOf("/") + 1).replace('-', ' ');
function setupPage () {
    $.ajax ({
        type: 'GET',
        url: 'http://onlymemes.biz/api/profiles/' + profile,
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify({}),
        success: function (data, status) {
            $('header').append('<div class="text"></div>');
            $('.text').append('<div class="profilename"></div>');
            $('.text .profilename').append('<h2>' + data.name + '</h2>');
	    $('.text .profilename').append('<a href="onlymemes.biz" class="link"></a>');
            $('.text').append('<div class="imgdesc"></div>');
            $('.imgdesc').append('<div class="profim"></div>');
            $('.profim').append('<img src=' + data.pfp + '>');
            if (data.description != null) {
                $('.imgdesc').append('<div class="descr">' + data.description + '</div>');
            }
            profile = data;
            getPosts();
        }
    });
}

function getPosts () {
    $.ajax ({
	type: 'GET',
	url: 'http://onlymemes.biz/api/posts/' + profile.id,
	contentType: 'application/json',
	dataType: 'json',
	data: JSON.stringify({}),
	success: function (data, status) {
	    for (let i = 0; i < data.length; i++) {
		$('.posts').append(`<div id="${data[i].id}">`);
		if (data[i].media) {
			$(`#${data[i].id}`).append('<img src=' + data[i].media + '></div>');
		} else {
			$(`#${data[i].id}`).append(data[i].text + '</div>');
		}
	    }
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    setupPage();
});
