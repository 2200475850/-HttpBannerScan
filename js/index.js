$(function(){
	$('.nav_box').hover(
		function(){
			$(this).find('b').show();
			$(this).find('.inbox').show();
		},
		function(){
			$(this).find('b').hide();
			$(this).find('.inbox').hide();
		}
	);
	$('.nav_box').each(function(index, element) {
        $(this).find('span').eq(1).css({color:'#fff'});
    }).last().css({'border-right':'none'});
	$('#footer').corner('4px');
	if($('#gla')){
		$('.gla_inbox').corner('8px');
		$('#gla_box>ul').roundabout({
			minOpacity:1,
			btnNext: ".next",
			duration: 1000,
			reflect: true,
			btnPrev: '.prev',
			autoplay:true,
			autoplayDuration:5000,
			tilt:0,
			shape: 'figure8'
		});
	}
	$('#sidebar li').eq(0).css({'border-top-color':''});
	$('#sidebar li').each(function(index){
		$(this).hover(
			function(){
				$(this).addClass('li_hover').find('a').css({'color':'#03F'});
			},
			function(){
				$(this).removeClass('li_hover').find('a').css({'color':'#fff'});
			}
		);
	});
	$('.con li:even').css({'background':'#f8fbfc'});
});