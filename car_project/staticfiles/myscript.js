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
            
            if (true) {
                //alert("You clicked on a row!");
                const cellIndex = Array.from(this.cells).indexOf(event.target.closest('td'));
                if (cellIndex === 0) {
                    // Only toggle if the actual target is not the checkbox
                    if (event.target.type !== 'checkbox') {
                        const checkbox = event.target.closest('td').querySelector('input[type="checkbox"]');
                        if (checkbox) {
                            checkbox.checked = !checkbox.checked;
                        }
                    }

                    //Get the Average Price and Average Kelometers from all selected checkboxes
                    const checkboxes = document.querySelectorAll('#cartable_datatable input[type="checkbox"]:checked');
                    const avgDisplay = document.getElementById('avegage_value');

                    let totalPrice = 0;
                    let totalKm = 0;
                    let count = checkboxes.length;

                    checkboxes.forEach(cb => {
                        totalPrice += parseFloat(cb.dataset.price);
                        totalKm += parseFloat(cb.dataset.km);
                    });

                    // alert(count);
                    // alert(`Total Price: € ${totalPrice.toFixed(0)} | Total KM: ${totalKm.toFixed(0)}`);

                    if (count > 0) {
                        const avgPrice = (totalPrice / count).toFixed(0);
                        const avgKm = (totalKm / count).toFixed(0);
                        avgDisplay.innerText = `Avg Price= € ${avgPrice} | Avg KM= ${avgKm}`;
                    } else {
                        avgDisplay.innerText = "Avg Price= € 0 | Avg KM= 0";
                    }

                    // if (count > 0) {
                    //     const avgPrice = totalPrice / count;
                    //     const avgKm = totalKm / count;

                    //     console.log(`Average Price: ${avgPrice}`);
                    //     console.log(`Average KM: ${avgKm}`);
                    // } else {
                    //     console.log("No checkboxes selected.");
                    // }

                    return;
                }
            }
            
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

// $(document).ready(function() {
//     $('.filter_cars').multiSelect();
// });

function showFullText(cell){
    cell.classList.toggle("expanded");
}