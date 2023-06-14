function register(create_form) {
    let formData = new FormData(create_form[0]);
    $.ajax({
        data: formData,
        url: create_form.attr('action'),
        type: create_form.attr('method'),
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            'X-CSRFToken': csrftoken
        },
        processData: false,
        contentType: false,
        success: function (response) {
            create_form.trigger('reset');
            if (response.object === 'UserData') {
                messages(response)
                close_modal('drawer_create')
                checkForUserData()
            }
        },
        error: function (error) {
            let errors = "";
            for (let item in error.responseJSON.error) {
                errors += `<li>${item} - ${error.responseJSON.error[item]}</li>`
            }
            setTimeout(function () {
                Swal.fire({
                    title: `<strong>${error.responseJSON['message']}</strong>`,
                    icon: `${error.responseJSON['icon']}`,
                    html:
                        `<div class="flex p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400" role="alert">
                        <svg aria-hidden="true" class="flex-shrink-0 inline w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"></path></svg>
                        <span class="sr-only">Danger</span>
                        <div style="text-align: start;">
                            <span class="font-medium">Parece que tienes algunos errores:</span>
                                <ul class="mt-1.5 ml-4 list-disc list-inside">
                                    ${errors}
                                </ul>
                        </div>
                    </div>`,
                    showCloseButton: true,
                    cancelButtonText: 'OK',
                })
            }, 250)
        }
    })
}

$(document).on('submit', $('#create_form'), function (event) {
    const create_form = $('#create_form');
    event.preventDefault();
    register(create_form);
})
