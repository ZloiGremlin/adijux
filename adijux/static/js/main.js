$(function () {
    setInterval(function () {
        $('.loading').animate({opacity:0.3}, 500, function () {
            $('.loading').animate({opacity:0.8}, 500);
        });
    }, 1000);

    $('.turn').click(function () {
        if (!$(this).is('.active')) {
            $(this).addClass('active');
            $(this).text('Развернуть описание');
            $(this).parents('.bottom').animate({height:'160px'}, 200);
        }
        else {
            $(this).removeClass('active');
            $(this).text('Свернуть описание');
            $(this).parents('.bottom').animate({height:$(this).parents('.bottom').attr('height')+'px'}, 200);
        }
    });

    $('.select span').click(function () {
        $(this).parent().find('ul').slideToggle(200);

    });

    $('#photonum a').click(function(){
        $('#rightnomer').css('background-image', 'url('+$(this).attr('href')+')');
        return false;
    });


});


function setWindowSize() {
    var w_height = $(window).height(),
        text = $('.right'),
        bl = text.find('.bottom'),
        sc = text.find('.scroll'),
        pattrn = $('#uzor');

    pattrn.height(w_height);
    bl.height(w_height - 75 - 73 - 67 - 40 -75);
    if (bl.height() < 380) bl.height(380);
    bl.attr('height', bl.height());
    sc.height(bl.height() - bl.find('.head').height() - 100);
    $('#rightnomer, #infonomer').css('height', $('#uzor').height()-73);

    $('.right.content .scroll').height(w_height - 75 - 73 - 60 - 75 - $('.right.content h1').height());
}

function selectSlide(index) {
    $('.photo img').animate({opacity:0}, 300, function(){
        $('.photo').html('<img src="'+$('#bgs img:eq('+index+')').attr('src')+'"/>');
        if ($('.photo').width() > $('.photo img').width()) $('.photo img').css('width', '100%');
        $('.photo img').animate({opacity:1}, 500);
    });
}



function showGallery() {
    $('.preloader').fadeOut(300);
    $('.logo').animate({top:-75}, 500);
    $('.thumbnails, .squares').fadeIn(1000);
    selectSlide(0);
    setInterval(nextSlide, 10000);
}

function nextSlide() {
    var ac = $('.thumbnails li.active');
    ac.removeClass('active');
    if (ac.next().is('li')) {
        ac.next().addClass('active');
    }
    else {
        $('.thumbnails li:eq(0)').addClass('active');
    }
    selectSlide(parseInt($('.thumbnails li.active').attr('rel')));
    return false;
}

function prevSlide() {
    var ac = $('.thumbnails li.active');
    ac.removeClass('active');
    if (ac.prev().is('li')) {
        ac.prev().addClass('active');
    }
    else {
        $('.thumbnails li:last').addClass('active');
    }
    selectSlide(parseInt($('.thumbnails li.active').attr('rel')));
    return false;
}

$(function () {
    setWindowSize();
    $(window).resize(setWindowSize);

    $('.scroll').jScrollPane({
        verticalDragMinHeight:67,
        autoReinitialise:true,
        autoReinitialiseDelay:50,
        verticalDragMaxHeight:67

    });

    var sp = $('#bgs img').size(),
        ci = 0;


    $('#bgs img').load(function(){
        ci++;
        if (ci == sp) showGallery();
    });

    $('.thumbnails li a').click(function(){});

    $('.thumbnails li').click(function(){
        if (!$(this).hasClass('active')) {
            $('.thumbnails li').removeClass('active');
            $(this).addClass('active');
            selectSlide(parseInt($(this).attr('rel')));
        }
        return false;
    });
    $('#arr-prev').click(prevSlide);
    $('#arr-next').click(nextSlide);
});