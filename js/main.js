// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});
// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video'
        , 'type': 'text-html'
        , 'src': sourceUrl
        , 'frameborder': 0
    }));
});
// Animate in the movies when the page loads
$(document).ready(function () {
    $('.movie-tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
    });
    // Add active class when nav button is clicked
    if ($('span#main').length) {
        $("ul.navbar-nav li:nth-child(1)").addClass("active");
    }
    else if ($('span#upload').length) {
        $("ul.navbar-nav li:nth-child(2)").addClass("active");
    }
});