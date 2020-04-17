$(function () {
    $(":file").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = imageIsLoaded;
            reader.readAsDataURL(this.files[0]);
            var res = detect(this.files[0]);
            
        }
    });
});

function detect(file) {
    var data = new FormData()
    data.append('image', file, 'image')
    var inputF = document.getElementById("lcategory"); 
    fetch('/predict', {
        method: 'POST',
        body: data
    })
        .then(response => response.json() // if the response is a JSON object
        )
        .then((result) => { inputF.value = result.category; } // Handle the success response object
        ).catch(
            error => console.log(error) // Handle the error response object
        );

}

function imageIsLoaded(e) {
    $('#myImg').attr('src', e.target.result);
};