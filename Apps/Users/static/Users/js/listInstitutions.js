function listInstitutions() {
    $.ajax({
        url: '/users/list_institutions/',
        type: 'get',
        dataType: 'json',
        success: function (response) {
            console.log(response)
            if ($.fn.DataTable.isDataTable('#table_institutions')) {
                $('#table_institutions').DataTable().destroy();
            }
            let tbody = $('#table_institutions tbody');
            tbody.html('');
            for (let i = 0; i < response.length; i++) {
                let row = `<tr class="bg-white w-full border-b border-gray-600 dark:bg-gray-800 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-600">`;
                    row += `<th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">${response[i]['institution_name']}</th>`
                    row += `<td class="px-6 py-4">${response[i]['institution_manager_name']}</td>`
                    row +=
                        `<td class="px-6 py-4">
                            <button type="button" class="px-3 py-2 text-xs font-medium text-center text-white bg-green-700 rounded-lg hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">
                                <svg fill="none" class="w-5 h-5" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"></path>
                                </svg>
                            </button>
                        </td>`
                row += '</tr>';
                tbody.append(row);
            }
            $('#table_institutions').DataTable(dataTableOptions);
        },
        error: function (error) {
            console.log(error)
        }
    });
}

$(document).ready(function () {
    listInstitutions();
})