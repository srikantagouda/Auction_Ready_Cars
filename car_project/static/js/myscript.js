$("#searchbox").on("input change", function () {
    var value = $(this).val().toLowerCase();
    $(".table_filter tr").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
});



// table-interactions.js
// table-interactions.js
document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('tbody.table_filter tr');
    rows.forEach(row => {
        row.addEventListener('click', function() {
            // Remove 'selected-car' class from all rows
            rows.forEach(r => r.classList.remove('selected-car'));
            // Add 'selected-car' class to the clicked row
            this.classList.add('selected-car');

            //Remove the Heading with ID:
            //$('#all_image_list_header').remove();

            var currentid = this.id.split('_')[1];
            var imageUrlString = $('#carimages_' + currentid).val();
            
            // Clear the image container
            $('#selected_car_images').empty();

            // Create img tags for each URL and append to the container
            // Split the string by commas
            var imageUrls = imageUrlString.split(',');
            imageUrls.forEach(function(url) {
                
                // Set the image source
                var imageUrl = `/media/${url}`;
                //$('#imageContainer').empty().append(`<img src="${imageUrl}" class="img-fluid" alt="Car Image">`);
                var imgTag = $('<img>').attr('src', imageUrl).addClass('img-fluid mb-2');
                $('#selected_car_images').append(imgTag);
            });

        });
    });
});

$(document).ready(function() {
    $('.js-example-basic-single').multiSelect();

});

function showFullText(cell){
    cell.classList.toggle("expanded");
}