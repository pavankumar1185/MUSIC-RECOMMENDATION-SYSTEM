document.getElementById('recommendBtn').addEventListener('click', function () {
	// Get input values
	var artist = document.getElementById('artistInput').value
	var genre = document.getElementById('genreInput').value
	var area = document.getElementById('areaInput').value

	// Make a POST request to the /recommend endpoint
	fetch('/recommend', {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({
			artist: artist,
			genre: genre,
			area: area,
		}),
	})
		.then((response) => response.json())
		.then((data) => {
			// Display recommended tracks
			// var recommendationsDiv = document.getElementById('recommendations')
			// recommendationsDiv.innerHTML = '<h2>Recommended Tracks</h2>'
			// var recommendedTracksList = document.createElement('ul')
			// data.forEach(function (track) {
			// 	var listItem = document.createElement('li')
			// 	listItem.textContent = track
			// 	recommendedTracksList.appendChild(listItem)
			// })
			// recommendationsDiv.appendChild(recommendedTracksList)
			console.log(data)
		})
		.catch((error) => {
			console.error('Error:', error)
		})
})

function playSong(song) {
	// Redirect to Google search for the recommended song
	window.open('https://www.google.com/search?q=' + encodeURIComponent(song))
}
