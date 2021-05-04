$('#gallery').children().each(function(e) {
    var post = $(this);
    var img = post.children()[0];

    img.addEventListener('mouseover', function(e) {
        if (post.children()[1].style.display == 'block') {
            return;
        }
        img.style.boxShadow = '0px 6px 9px rgba(0, 0, 0, 0.35), 0px 6px 9px rgba(0, 0, 0, 0.35)';
    });

    img.addEventListener('mouseout', function(e) {
        img.style.boxShadow = '0px 3px 6px rgba(0, 0, 0, 0.15), 0px 3px 6px rgba(0, 0, 0, 0.15)';
    });

    img.addEventListener('click', function(e) {
        window.location = this.dataset.url;
    });
});