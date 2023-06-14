function checkForUserData() {
    $.ajax({
        url: '/users/check_user_data/',
        type: 'get',
        dataType: 'json',
        success: function (response) {
            if (response[0]['fields']['is_data_completed'] === false) {
                const notify = document.getElementById('toast-bottom-right')
                notify.classList.remove('hidden')
            } else {
                if ($('#toast-bottom-right').length > 0) {
                    const notify = document.getElementById('toast-bottom-right')
                    notify.classList.add('hidden')
                }
            }
        },
        error: function (error) {
            console.log(error)
        }
    })
}

$(document).ready(function () {
    checkForUserData();
})