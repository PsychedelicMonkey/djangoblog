$(document).ready(function(e) {
    var followBtns = document.querySelectorAll('.follow-btn');
    var followerCount = document.getElementById('followers-count');

    followBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            follow(this, followerCount);
        });
    });
});

function follow(btn, count) {
    fetch(btn.dataset.url)
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }
        
        btn.setAttribute('data-url', data.url);
        btn.innerHTML = data.btnLabel;
        count.innerHTML = data.count;
    })
}