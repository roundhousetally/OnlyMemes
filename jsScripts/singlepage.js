#!/usr/bin/node

let profilenm = window.location.href.slice(window.location.href.lastIndexOf("/")+ 1)

function getProfile () {
    $.ajax ({
	type: 'GET',
	url: 'http://0.0.0.0:5000/api/posts/${profilenm}',
	contentType: 'application/json',
	dataType: 'json',
	data: JSON.stringify({}),
	success: function (data, status) {
	$('header').append('<div class="text">');
	$('header').append('<div class="profilename">');
	$('.text .profilename').append('<h2>' + data[i].name + '</h2></div>');
	$('.text').append('<div class="imgdesc">');
	$('.imgdesc').append('<div class="profim">');
	$('.profim').append('<img src=' + data[i].pfp + '></div>');
	$('.imgdesc').append('<div class="descr">' + data[i].description + '</div>');
	$('.imgdesc').append('</div');
	$('.text').append('/div>');
	    for (let i = 0; i < data.length; i++) {
		$('.posts').append('<div id="${data[i].id}">');
		if (data[i].media) {
			$('#${data[i].id}').append('<img src=' + data[i].media + '></div>');
		}else {
			$('#${data[i].id}').append(data[i].text + '</div>');
		}
	
}}});}

document.addEventListener('DOMContentLoaded', function () {
    getProfile()
});
