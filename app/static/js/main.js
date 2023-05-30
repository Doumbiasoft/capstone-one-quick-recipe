'use strict';

 const BASE_URL = "http://192.168.0.116:5000";

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");
         /*------------------
            Product filter
        --------------------*/
        if ($('#category-filter').length > 0) {
            var containerEl = document.querySelector('#category-filter');
            var mixer = mixitup(containerEl, {
                load: {
                    filter: '.mostpopular'
                }
            });
        }
        $(".categories-filter-section .filter-item ul li").on('click', function () {
            $(".categories-filter-section .filter-item ul li").removeClass('active');
            $(this).addClass('active');
        });
    });
    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    $('.set-html').each(function () {
        var html = $(this).data('html');
        $(this).html(html)
    });

    $('.set-limit').each(function () {
        var html = $(this).data('html');
        var length = 100;
        var trimmedString = html.substring(0, length)+"...";
        $(this).html(trimmedString)
    });




    // Search model
	$('.search-switch').on('click', function() {
		$('.search-model').fadeIn(400);
	});

	$('.search-close-switch').on('click', function() {
		$('.search-model').fadeOut(400,function(){
			$('#search-input').val('');
		});
	});


    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*-------------------
		Category Select
	--------------------- */
    $('#category').niceSelect();

    /*-------------------
		Local Select
	--------------------- */
    $('#tag').niceSelect();

    $("#scrollToTopBtn").click(function() {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
     });

})(jQuery);

// Get the button
let mybutton = document.getElementById("scrollToTopBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > (document.body.scrollHeight/3) || document.documentElement.scrollTop > (document.body.scrollHeight/3)) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
