// This jquery function toggles the accordion button color and shadow when a specific accordion button is clicked and unclicked. 
// This allows the user to immediatley see which accordions are expanded and highlights which complaint is being reviewed.
$(document).ready(function() {
    $('.accordion-button').click(function () {
        $(this).toggleClass('accordion-button-clicked');
    });
});


// This function removes the django messages inserted when a user completes an action after 3 seconds.
setTimeout(function () {
    let messages = document.getElementById('django-message');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);