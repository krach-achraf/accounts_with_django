function search() {
    let nom = document.getElementsByName("nom")[0].value;
    let result = ''
    $.ajax({
            method: 'get',
            url: '/controle/search_clients/' + nom,
            success: function (data) {
                $("#table").empty();
                for (let i = 0; i < data.length; i++) {
                    result += "<tr><td>"
                        + data[i].pk
                        + "</td> <td>"
                        + data[i].fields.nom
                        + "</td><td>"
                        + data[i].fields.prenom
                        + "</td><td></td></tr>"
                }
                $("#table").append(result);
            },
            error: function (error) {
                console.log(error);
            }
        }
    )
}