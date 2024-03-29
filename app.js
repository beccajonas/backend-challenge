const socket = io.connect('http://localhost:5555');

// Function to fetch players from the server
function fetchPlayers() {
	fetch('http://localhost:5555/players')
		.then((res) => res.json())
		.then((players) => {
			let playersDiv = document.getElementById('players');
			playersDiv.innerHTML = players
				.map((player) => `<p>${player.id} | Player: ${player.username}</p>`)
				.join('');
		})
		.catch((error) => console.error('Error fetching players:', error));
}

// Function to fetch lobbies from the server
function fetchLobbies() {
	fetch('http://localhost:5555/lobbies')
		.then((res) => res.json())
		.then((lobbies) => {
			let lobbiesDiv = document.getElementById('lobbies');
			lobbiesDiv.innerHTML = lobbies
				.map((lobby) => `<p>${lobby.id} | Lobby Details: ${lobby.details}</p>`)
				.join('');
		})
		.catch((error) => console.error('Error fetching lobbies:', error));
}

// Fetch players and lobbies when the page loads
window.addEventListener('load', function () {
	fetchPlayers();
	fetchLobbies();
});

// Socket.IO event listeners
socket.on('player_created', function (player) {
	console.log('Received player_created event:', player);
	let playersDiv = document.getElementById('players');
	playersDiv.innerHTML += `<p>${player.id} | Player: ${player.username}</p>`;
});

socket.on('lobby_created', function (lobby) {
	console.log('Received lobby_created event:', lobby);
	let lobbiesDiv = document.getElementById('lobbies');
	lobbiesDiv.innerHTML += `<p>${lobby.id} | Lobby Details: ${lobby.details}</p>`;
});

socket.on('player_joined_lobby', function (data) {
	console.log('Received player_joined_lobby event:', data);
	let activitiesDiv = document.getElementById('activities');
	activitiesDiv.innerHTML += `<p>Player ${data.player_id} joined Lobby ${data.lobby_id}</p>`;
});

socket.on('player_left_lobby', function (data) {
	console.log('Received player_left_lobby event:', data);
	let activitiesDiv = document.getElementById('activities');
	activitiesDiv.innerHTML += `<p>Player ${data.player_id} left Lobby ${data.lobby_id}</p>`;
});

socket.on('game_started', function (data) {
	console.log('Received game_started event:', data);
	let activitiesDiv = document.getElementById('activities');
	activitiesDiv.innerHTML += `<p>${data.message}</p>`;
});
