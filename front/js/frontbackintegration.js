$(function() {
    
    $.ajax({
        url: 'http://localhost:5000/listar_cachorros',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function() {
            alert("Não foi possível resgatar os dados, verifique arquivos Backend");
        }
    });

    function listar (Cachorro {
        for (var i in Cachorro) { //i = posição no vetor
            lin = '<tr>' + // elabora linha com os dados do Cachorro
              '<td>' + Cachorro[i].Nome  + '</td>' + 
              '<td>' + Cachorro[i].Raca  + '</td>' + 
              '<td>' + Cachorro[i].Idade + '</td>' + 
              '<td>' + Cachorro[i].Dono  + '</td>' + 
              '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaCachorros').append(lin);
        }
    }
});