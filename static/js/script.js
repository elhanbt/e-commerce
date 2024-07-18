$('.slider').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay:true,
    autoplaySpeed: 2000,
    pauseOnHover: false,
    cssEase:'ease-out',
    prevArrow: '<span class="sliderarrowleft"><img src="{% static "/imgs/left_arrow.svg" %}" alt="left arrow"/></span>',
    nextArrow: "<span class='sliderarrowright'><img src='{% static /imgs/right_arrow.svg %}' alt='right arrow'/></span>",
});

console.log("hello")


