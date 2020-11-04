#!/usr/bin/node


/*
  This file is responsible for laoding the posts associated
  with each profile and loading them as the user scrolls
*/

let profile = window.location.href;
profile = profile.slice(profile.lastIndexOf("/") + 1).replace('-', ' ');


function setupPage () {
    // Sets up the page, loading profile info and first page of posts
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
            getPosts(0);
        }
    });
}

function getPosts (page) {
    // Gets all posts with page numbe as input
    $.ajax ({
	type: 'GET',
	url: 'http://onlymemes.biz/api/posts/' + profile.id + '/' + page,
	contentType: 'application/json',
	dataType: 'json',
	data: JSON.stringify({}),
	success: function (data, status) {
	    for (let i = 0; i < data.length; i++) {
		if ('ending' in data[i]) {
		    return (0);
		}
		$('.posts').append(`<div id="${data[i].id}">`);
		if (data[i].media) {
			$(`#${data[i].id}`).append('<img src=' + data[i].media + '></div>');
		} else {
			$(`#${data[i].id}`).append(data[i].text + '</div>');
		}
	    }
        }
    });
    return (1);
}


document.addEventListener('DOMContentLoaded', function () {
    // Waits for the page to load and runs a setup
    setupPage();
    let i = 1;
    $(window).scroll(function() {
	// Detects when user scrolls and adds content
	if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
	    let newVar = getPosts(i);
	    if (newVar === 0) {
		return;
	    }
	    i = i + 1;
        }
    });
});
