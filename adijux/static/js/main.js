$(function () {

    $('.fancy').fancybox({
        padding:0,
        margin:0
    });

    $('.cont_menu li a').click(function(){
        $('.cont_menu li').removeClass('active');
        $(this).parent().addClass('active');
        $('.sw').hide(0);
        $($(this).attr('href')).show(0);
        return false;
    });

    $('.select:not(".big") a').click(function(){
        $('#'+$(this).parents('.select').attr('rel')).val($(this).text());
        $(this).parents('.select').find('ul').slideToggle(200);
        $(this).parents('.select').find('span').text($(this).text());
        return false;

    });

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


    $('.dop-parameters span').click(function () {
        $(this).parent().find('.plashka-dop').fadeIn(200);

    });

    $('.plashka-dop .close').click(function () {
        $(this).parent().fadeOut(200);


    });

    $('.item label input').change(function () {
        $('*[name=' + $(this).attr('name') + ']').each(function(){$(this).parent().removeClass('active');});
        $(this).parent().toggleClass('active');
        $('#'+$(this).parents('.form-item').attr('rel')).val($(this).val());
    });

    $('#datepicker').datepicker({
        numberOfMonths:1,
        minDate:0,
        onSelect: function(d,t) {
            var d1 = new Date(parseInt(d.split('.')[2]),parseInt(d.split('.')[1])-1,parseInt(d.split('.')[0]));
            var d2 = $("#datepicker2").datepicker("getDate");
            if (d2 < d1) {
                $("#datepicker2" ).datepicker("setDate", d);
                d2 = d1;
            }
            if (d2 > d1) {
               while (d2 > d1) {
                   d2.setDate(d2.getDate() - 1);
                   var m = d2.getMonth(), day = d2.getDate(), y = d2.getFullYear();
                   if($.inArray(day + '-' + (m+1) + '-' + y, disabledDays) != -1) {
                       $("#datepicker2" ).datepicker("setDate", d);
                       d2 = d1;
                   }

               }
            }
            d1 = new Date(parseInt(d.split('.')[2]),parseInt(d.split('.')[1])-1,parseInt(d.split('.')[0]));
            d2 = $("#datepicker2").datepicker("getDate");
            $('#id_date').val(d1.getDate()+ '.' + d1.getMonth() + '.' + d1.getFullYear() + '-' +d2.getDate()+ '.' + d2.getMonth() + '.' + d2.getFullYear());
        },
        beforeShowDay: disableDates
    });

    $('#datepicker2').datepicker({
        numberOfMonths:1,
        minDate:0,
        onSelect: function(d,t) {
            var d2 = new Date(parseInt(d.split('.')[2]),parseInt(d.split('.')[1])-1,parseInt(d.split('.')[0]));
            var d1 = $("#datepicker").datepicker("getDate");
            if (d2 < d1) {
                $("#datepicker" ).datepicker("setDate", d);
                d1 = d2;
            }
            if (d2 > d1) {
                while (d2 > d1) {
                    d2.setDate(d2.getDate() - 1);
                    var m = d2.getMonth(), day = d2.getDate(), y = d2.getFullYear();
                    if($.inArray(day + '-' + (m+1) + '-' + y, disabledDays) != -1) {
                        $("#datepicker" ).datepicker("setDate", d);
                        d1 = d2;
                    }

                }
            }
            d2 = new Date(parseInt(d.split('.')[2]),parseInt(d.split('.')[1])-1,parseInt(d.split('.')[0]));
            d1 = $("#datepicker").datepicker("getDate");
            $('#id_date').val(d1.getDate()+ '.' + d1.getMonth() + '.' + d1.getFullYear() + '-' +d2.getDate()+ '.' + d2.getMonth() + '.' + d2.getFullYear());
        },
        beforeShowDay: disableDates
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

    if ($('#rightnomer').height() < $('.booking').height()) $('#rightnomer').height($('.booking').height());
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




/* utility functions */
function disableDates(date) {
    var m = date.getMonth(), d = date.getDate(), y = date.getFullYear();
    //console.log('Checking (raw): ' + m + '-' + d + '-' + y);
    for (i = 0; i < disabledDays.length; i++) {
        if($.inArray(d + '-' + (m+1) + '-' + y, disabledDays) != -1) {
            //console.log('bad:  ' + (m+1) + '-' + d + '-' + y + ' / ' + disabledDays[i]);
            return [false];
        }
    }
    //console.log('good:  ' + (m+1) + '-' + d + '-' + y);
    return [true];
}

function sendBook(){
    $('#form_book input, #form_book textarea').each(function(){

        $($(this).attr('rel')).val($(this).val());
    });
    $('#bookingform').submit();
}


var map;
    $(document).ready(function(){
      map = new GMaps({
        div: '#map',
        zoom: 16,
        lat: 44.045895,
        lng: 41.766216
      });
      map.addMarker({
        lat: 44.045895,
        lng: 41.766216,
        title: 'Адиюх-Пэлас',
        infoWindow: {
        content: '<p>369400, Россия</p><p>Карачаево-Черкесская Республика</p> <p>А. Хабез,ул. Умара Хабекова, 124а</p>'
        }
      });
    });