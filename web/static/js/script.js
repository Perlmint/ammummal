// constants
var LOADING_DELAY = 150;

// global variables
var debug = true;
var _log = [];

// useful tools
function log(message, value) {
	var activity = {
		message: message
	};
	if(typeof(value) != "undefined") {
		activity.value = value;
	}
	_log.push(activity);
	if(debug) {
		if(typeof(value) != "undefined") {
			console.log(message + ":\n", value);
		} else {
			console.log(message);
		}
	}
}
function dump(target, source, keys) {
	if(typeof(keys) == "object" && typeof(keys.length) == "number") {
		for(var i in keys) {
			var key = keys[i];
			if(key in source) {
				target[key] = angular.copy(source[key]);
			} else {
				target[key] = null;
			}
		}
	} else {
		for(var key in source) {
			target[key] = angular.copy(source[key]);
		}
	}
	return target
}

// global UI functions
var loading = {};
loading.start = function(callback){
	var $loading = $("#loading-cover");
	if($loading.length) {
		$loading.show();
		$loading.css("opacity", 1);
	}
	if(typeof(callback) == "function") {
		setTimeout(callback, LOADING_DELAY);
	}
};
loading.finish = function(callback){
	var $loading = $("#loading-cover");
	if($loading.length) {
		$loading.css("opacity", 0);
		setTimeout(function(){
			$loading.hide();
			if(typeof(callback) == "function") {
				callback();
			}
		}, LOADING_DELAY);
	}
};

// service logics
function message(text) {
	$("#home-message").text(text);
}
function onSubmit() {
	var content_length = $("#home-content").val().length;
	if(content_length > 10000) {
		message("글자수가 너무 마나용");
		return false;
	} else {
		loading.start();
		return true;
	}
}

// trigger
$(document).ready(function(e){
	log("@theeluwin");
});
