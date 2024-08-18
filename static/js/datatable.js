$(document).ready(function() {
    $('#negaraTable').DataTable({
        "ajax": {
            "url": "/api/negara",
            "dataSrc": ""
        },
        "columns": [
            { "data": "id_negara" },
            { "data": "nama_negara" },
            { "data": "nama_kawasan" },
            { "data": "nama_direktorat" },
            { "data": "created_at" },
            {
                "data": null,
                "defaultContent": "<button class='delete-btn'>Delete</button>"
            }
        ],
        "paging": true,
        "searching": true
    });

    // Fungsi untuk tombol Delete
    $('#negaraTable tbody').on('click', 'button.delete-btn', function () {
        var data = $('#negaraTable').DataTable().row($(this).parents('tr')).data();
        $.ajax({
            url: '/api/negara/' + data.id_negara,
            type: 'DELETE',
            success: function(result) {
                $('#negaraTable').DataTable().ajax.reload();
            }
        });
    });
});
