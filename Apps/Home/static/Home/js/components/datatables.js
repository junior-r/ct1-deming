const dataTableOptions = {
    columnDefs: [],
    lengthMenu: [ [10, 25, 50, 100, -1], [10, 25, 50, 100, "Todos"] ],
    pagingType: "full_numbers",
    processing: true,
    Paginate: true,
    pageLength: 10,
    destroy: true,
    language: {
        lengthMenu: "<span class='text-gray-900 dark:text-white'>Mostrar _MENU_ registros por página</span>",
        zeroRecords: "<span class='text-gray-900 dark:text-white'>Ningún registro encontrado</span>",
        info: "<span class='text-gray-900 dark:text-white'>Mostrando de _START_ a _END_ de un total de _TOTAL_ registros</span>",
        infoEmpty: "<span class='text-gray-900 dark:text-white'>Ningún registro encontrado</span>",
        infoFiltered: "<span class='text-gray-900 dark:text-white'>(filtrados desde _MAX_ registros totales)</span>",
        search: "<span class='text-gray-900 dark:text-white'>Buscar:</span>",
        loadingRecords: "<span class='text-gray-900 dark:text-white'>Cargando...</span>",
        paginate: {
            first: "Primero",
            last: "Último",
            next: "Siguiente",
            previous: "Anterior"
        }
    }
};