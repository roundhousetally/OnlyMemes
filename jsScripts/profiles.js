#!/usr/bin/node

function getProfile () {
    $.ajax ({
	type: 'GET',
	url: 'http://0.0.0.0:5000/api/profiles',
	contentType: 'application/json',
	dataType: 'json',
	data: JSON.stringify({}),
	success: function (data, status) {
	    for (let i = 0; i < data.length; i++) {
		let pr = '<a href="onlymemes.biz/p/${data[i].name}" class=temp></a>'
		$('.profilebox').append('<div class="profilecard cheese"></div>');
		$('.profilebox .cheese').append(pr);
		$('.cheese').removeClass('cheese');
		$('.temp').append('<div class="profilename"><h1>' +
				  data[i].name + '</h1></div>');
		$('.temp').append('<div class="profim"></div>');
		$('.temp .profim').append('<img src=' + data[i].pfp + ' class="image">');
		$('.temp .profim').append('<div class="overlay"></div>');
		$('.temp .overlay').append('<div class="descr">' + data[i].description + '</div>');
		$('.temp').removeClass('temp');
	    }
	}
    });
}

document.addEventListener('DOMContentLoaded', function () {
    getProfile()
});
