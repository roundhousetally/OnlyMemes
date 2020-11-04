#!/usr/bin/node


/*
  This file is ran when the OnlyMemes
  home page is loaded, loading all profiles
 */


function getProfile () {
    /* The goal of this function is to get
       a list of all profiles and load them
       all in dynamically
     */
    $.ajax ({
	type: 'GET',
	url: 'http://onlymemes.biz/api/profiles',
	contentType: 'application/json',
	dataType: 'json',
	data: JSON.stringify({}),
	success: function (data, status) {
	    for (let i = 0; i < data.length; i++) {
		// Gives each profile a temp class to make is accessible
		let pr = '<a href="p/' + data[i].name.replace(' ', '-') + '" class="temp"></a>'
		$('.profilebox').append('<div class="profilecard cheese"></div>');
		$('.profilebox .cheese').append(pr);
		$('.cheese').removeClass('cheese');
		$('.temp').append('<div class="profilename"><h1>' +
				  data[i].name + '</h1></div>');
		$('.temp').append('<div class="profim"></div>');
		$('.temp .profim').append('<img src=' + data[i].pfp + ' class="image">');
		$('.temp .profim').append('<div class="overlay"></div>');
		$('.temp .overlay').append('<div class="descr">' + data[i].description + '</div>');
		// Removing the temp variable to be reused
		$('.temp').removeClass('temp');
	    }
	}
    });
}


document.addEventListener('DOMContentLoaded', function () {
    // Waits for buffer to load and runs
    getProfile()
});
