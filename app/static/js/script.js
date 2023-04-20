// Define a global variable to store the fetched data
var cardDataArray = [];

function createCard(cardData) {
	// Create the HTML element for the card
	var card = document.createElement('div');
	card.classList.add('card');

	// Add product name to the card
	var name = document.createElement('h3');
	name.innerText = cardData.Produto;
	card.appendChild(name);

	// Add product price to the card
	var price = document.createElement('span');
	price.innerText = 'R$ ' + cardData.Preço;
	card.appendChild(price);

	// Add product description to the card
	var description = document.createElement('p');
	description.innerText = cardData['Avaliação da compra'] + ' estrelas | ' + cardData['Categoria do Produto'];
	card.appendChild(description);

	// Add the card to the page
	var container = document.getElementById('cardAPI');
	container.appendChild(card);
}

async function fetchData() {
	try {
		var consultaCEP = await fetch(`/produtos?regiao=norte&ano=2022`);
		var consultaCEPConvertida = await consultaCEP.json();
		if (consultaCEPConvertida.erro) {
			throw Error('CEP não existente!');
		}
		cardDataArray = consultaCEPConvertida;
	} catch (erro) {
		mensagemErro.innerHTML = `<p>CEP inválido. Tente novamente!</p>`
		console.log(erro);
	}
}

async function updatePagination() {
	// Fetch the data from the server and store it in the global variable
	await fetchData();

	// Get the number of pages
	var numPages = Math.ceil(cardDataArray.length / cardsPerPage);

	// Get the HTML element of the pagination
	var pagination = document.querySelector('.pagination');

	// Clear the current pagination
	pagination.innerHTML = '';

	// Add "Previous" button
	var prevButton = document.createElement('li');
	prevButton.innerHTML = '<a href="#" aria-label="Anterior"><span aria-hidden="true">&laquo;</span></a>';
	prevButton.classList.add('prev');

	// Add event listener for the "Previous" button
	prevButton.addEventListener('click', function () {
		var currentPage = parseInt(document.querySelector('.pagination .active').innerText);
		if (currentPage > 1) {
			goToPage(currentPage - 1);
		}
	});

	pagination.appendChild(prevButton);

	// Add page number buttons
	for (var i = 1; i <= numPages; i++) {
		var pageButton = document.createElement('li');
		pageButton.innerHTML = '<a href="#">' + i + '</a>';
		if (i === 1) {
			pageButton.classList.add('active');
		}

		// Add event listener for the page number button
		pageButton.addEventListener('click', function () {
			goToPage(parseInt(this.innerText));
		});

		pagination.appendChild(pageButton);
	}

	// Add "Next" button
	var nextButton = document.createElement('li');
	nextButton.innerHTML = '<a href="#" aria-label="Próximo"><span aria-hidden="true">&raquo;</span></a>';
	nextButton.classList.add('next');

	// Add event listener for the "Next" button
	nextButton.addEventListener('click', function () {
		var activeElement = document.querySelector('.pagination .active');
		if (activeElement !== null) {
			var currentPage = parseInt(activeElement.innerText);
			if (currentPage < numPages) {
				goToPage(currentPage + 1);
			}
		}
	});

	pagination.appendChild(nextButton);
}

function goToPage(page) {
	// Get the HTML element of the pagination
	var pagination = document.querySelector('.pagination');

	// Get the HTML element of the card container
	var container = document.getElementById('cardAPI');

	// Calculate the start and end indexes of the cards to display
	var start = (page - 1) * cardsPerPage;
	var end = Math.min(start + cardsPerPage, cardDataArray.length);

	// Remove all existing cards from the container
	container.innerHTML = '';

	// Add the cards to the container
	for (var i = start; i < end; i++) {
		createCard(cardDataArray[i]);
	}

	// Update the active page button
	var activeButton = pagination.querySelector('.active');
	if (activeButton !== null) {
		activeButton.classList.remove('active');
	}
	var pageButton = pagination.querySelector('li:nth-child(' + (page + 1) + ')');
	if (pageButton !== null) {
		pageButton.classList.add('active');
	}
}


var cardsPerPage = 10
updatePagination()