(function($){
	var playerExist = $("#my-player").length ? true : false;
	if(playerExist){
		var player = videojs('my-player');
		player.markers({
			markerStyle: {
				'width':'7px',
				'border-radius': '20%',
				'background-color': '#ff3838'
			},
			markerTip:{
				display: true,
				text: function(marker) {
					return marker.text;
				},
				time: function(marker) {
					return marker.time;
				}
			},
			breakOverlay:{
				display: true,
				displayTime: 3,
				style:{
					'width':'100%',
					'height': 'auto',
					'background-color': 'rgba(0,0,0,0.7)',
					'color': 'white',
					'font-size': '17px'
				},
				text: function(marker) {
					return '<a href="javascript:void(0);" id="overlayDismis" style="color:#fff;float:right;font-weight:bold">x</a>'+
					'<h3 style="color:#fff;margin:0;">'+marker.text + '</h3><p style="margin:0;">' + marker.overlayText+'</p>';
				},
			},
			markers: []
		});
	}
	$(document).on("click", "#overlayDismis", function(){
		$(this).parent().parent().css("visibility", "hidden");
	});
	function getFormatedTime(whereYouAt){
		var minutes = Math.floor(whereYouAt / 60);   
		var seconds = Math.floor(whereYouAt - minutes * 60);
		var x = minutes < 10 ? "0" + minutes : minutes;
    	var y = seconds < 10 ? "0" + seconds : seconds;
    	return x + ":" + y;
	}
	$("#sticker-btn").on("click", function(){
		if ($("#sticker-content").is(":visible") == false) {
			lecturenotelist_check();
		}
		$("#sticker-content").toggle(300);
	});
	$("#sticker-btn-add").on("click", function(){
		if (playerExist) {
			if($("#notelectureadd").is(":visible") == false){
				var currentTime = player.currentTime();
				player.pause();
				$("#notelectureadd small").html(getFormatedTime(currentTime));
				$("#notelectureadd input[name=time]").val(currentTime);
			} else {
				player.play();
			}
		}
		$("#notelectureadd").toggle(300);
	});
	var urlStickerManager = $("#urlStickerManager").val();
	var urlProgressManager = $("#urlProgressManager").val();
	var shownoteseconds = $("#shownoteseconds").val() == 'true';
	var csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
	lecturenotelist_check = function (){
		$.ajax({
			type: "POST",
			url: urlStickerManager,
			dataType: 'json',
			data: {
				csrfmiddlewaretoken: csrfmiddlewaretoken,
				slug: $("#lecture_slug").val(),
				s: "all",
			},
			success: function(data){
				var res = data["data"], output = "";
				$.each(res, function(i, v){
					output += '<li>'+
					  '<a href="javascript:void(0);" onclick="return lecturenotelist_manage(\'edit\', '+v.pk+');" class="sticker-btn-edit"><i class="fa fa-pencil"></i></a>'+
					  '<a href="javascript:void(0);" onclick="return lecturenotelist_manage(\'delete\', '+v.pk+');" class="sticker-btn-delete"><i class="fa fa-times"></i></a>'+
				      '<a href="#">'+
				      	(shownoteseconds ? ('<small>'+getFormatedTime(v.time)+'</small>') : '')+
				        '<h2>'+v.title+'</h2>'+
				        '<p>'+v.note+'</p>'+
				      '</a>'+
				    '</li>';
				    if (playerExist) {
				    	player.markers.add([{
							time: v.time,
							text: v.title,
							overlayText: v.note
						}])
				    }
				});
				$("#notelecturelist").html(output);
			}
		});
	}
	lecturenotelist_check();
	lecturenotelist_manage = function(cmd, index){
		if (cmd == "edit") {
			$.ajax({
				type: "POST",
				url: urlStickerManager,
				dataType: 'json',
				data: {
					csrfmiddlewaretoken: csrfmiddlewaretoken,
					pk: index,
					s: "read"
				},
				success: function(data){
					var res = data["data"], output = "";
					if (res) {
						$("#notelectureadd input[name=title]").val(res.title);
						$("#notelectureadd textarea[name=note]").val(res.note);
						$("#notelectureadd small").html(getFormatedTime(res.time));
						$("#notelectureadd input[name=time]").html(res.time);
						$("#notelectureadd input[name=s]").val("update");
						$("#notelectureadd input[name=pk]").val(res.pk);
					}
					$("#notelectureadd").show(300);
				}
			});
		} else if (cmd == "delete"){
			$.ajax({
				type: "POST",
				url: urlStickerManager,
				data: {
					csrfmiddlewaretoken: csrfmiddlewaretoken,
					s: "read",
					pk: index,
				},
				cache: false,
				dataType: 'json',
				success: function(data){
					var value = data["data"];
					$("#del_name").html(value.title );
					$("#deletemodalform input[name=pk]").val(value.pk);
					$("#deletemodal").modal("show");
				},
				error: function(jqXHR, textStatus, errorThrown){
					toastr.error(JSON.parse(jqXHR.responseText)["message"], {closeButton: true, progressBar: true,});
				}
			});
		} else if (cmd == "watch-lecture"){
			var complete = playerExist ? player.duration() : 100;
			var current  = playerExist ? player.currentTime() : 100;
			$.ajax({
				type: "POST",
				url: urlProgressManager,
				data: {
					csrfmiddlewaretoken: csrfmiddlewaretoken,
					s: cmd,
					slug: $("#lecture_slug").val(),
					complete: complete,
					current: current,
				},
				cache: false,
				dataType: 'json',
				success: function(data){},
			})
		}
	}
	setInterval(function(){lecturenotelist_manage("watch-lecture", -1);}, 5000);
	resetStickerForm = function(){
		$("#notelectureadd input[name=s]").val("add");
		$("#notelectureadd input[name=pk]").val("-1");
		$("#notelectureadd input[name=title]").val("");
		$("#notelectureadd textarea[name=note]").val("");
		$("#notelectureadd").hide(300);
	}
	$("form.sticker-form, #deletemodalform").on("submit", function(e){
		e.preventDefault();
		var serializeform = $(this).serialize();
		var inputs = $(this).find("input, select, button, textarea");
		inputs.prop("disabled", true);
		$.ajax({
			type: "POST",
			url: $(this).attr("action"),
			data: serializeform,
			beforeSend: function(){},
			success: function(data){
				toastr.success(data["message"], {closeButton: true, progressBar: true,});
				inputs.prop("disabled", false);
				$(".modal").modal("hide");
				lecturenotelist_check();
				resetStickerForm();
			},
			error: function(jqXHR, textStatus, errorThrown){
				toastr.error(JSON.parse(jqXHR.responseText)["message"], {closeButton: true, progressBar: true,});
				inputs.prop("disabled", false);
			}
		});
	});
})(jQuery);