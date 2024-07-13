document.addEventListener('DOMContentLoaded', function() {
    manipularFormulario();
});
async function carregarAnimais(){
    /*
    axios.get('http://127.0.0.1:8000/animais')
    .then(response => console.log(response.data));
    */
    /*
    O método para obter informações do backend é o get, a sintexe ficando:
    axios.get('url-do-back')

    Obs.:O . then() é usado para manipular o resultado (ou erro) de uma Promise.
    Ele permite que você especifique o que fazer quando a Promise é resolvida
    (quando a operação assíncrona é bem-sucedida) ou quando é rejeitada
    (quando ocorre um erro).

    Nocaso ele está sendo utilizado para imprimir o response.data(conteúdo do
    reponse) no console
    */
    const response = await axios.get('http://127.0.0.1:8000/animais');
    // await é para aguadar a requisição, já que ela acontece de forma
    //assíncrona, por isso o uso do 'async' antes de function
    const animais = response.data; //foi criado uma constante que receberá a
    //lista de conteúdos da response

    const listaHtml = document.getElementById('tabelaAnimal');
    //foi criado uma constante que recebe o elemento <tbody id="tabelaAnimal">

    listaHtml.innerHTML = '' //zerando a tabela para quando acontecer o submit a
     //tabela não duplicar as linhas com as informações anteriores

    var index = 1;
    animais.forEach(animal => {
    /*Para cada animal da lista animais, será criado um elemento tr
    que terá como texto as informações dos animais para cada respectiva coluna,
    e por último esse tr é adicionado como filho do listaHtml que é um
    <tbody id="tabelaAnimal">, ou seja o corpo da tabela
    */
        const item = document.createElement('tr');
        item.innerHTML =
        `<th scope="row">${index}</th>
        <td>${animal.nome}</td>
        <td>${animal.cor}</td>
        <td>${animal.idade}</td>
        <td>${animal.sexo}</td>`;

        index += 1;
        listaHtml.appendChild(item);});
}

function manipularFormulario(){
    const formularioAnimal = document.getElementById("form-animal");
    const inputNome = document.getElementById("animalNome");
    const inputCor = document.getElementById("animalCor");
    const inputIdade = document.getElementById("animalIdade");
    const inputSexo = document.getElementById("animalSexo");

    formularioAnimal.onsubmit = async (event) => {
        event.preventDefault() //usado para não dar reload quando o form for
        //submit
        const nomeAnimal = inputNome.value;
        const corAnimal = inputCor.value;
        const idadeAnimal = inputIdade.value;
        const sexoAnimal = inputSexo.value;

        await axios.post('http://127.0.0.1:8000/animais',{ //método post do
        //axios para cadastrar um novo animal
            nome: nomeAnimal,
            idade: idadeAnimal,
            sexo: sexoAnimal,
            cor: corAnimal
        })
        carregarAnimais(); //Esta função foi chamada novamente para recarregar
        // a tabela logo após o submit, para vermos a atualização do novo
        //cadastro
    }
}

function app(){
    console.log("Ok, função");
    carregarAnimais();
}

app();
