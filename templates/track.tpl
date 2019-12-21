<div>
    <h1>{{track['name']}} - {{track['artists']}}</h1>
    <iframe 
        src="https://open.spotify.com/embed/track/{{track['id']}}" 
        height="380"
        frameborder="0"
        allowtransparency="true"
        allow="encrypted-media">
    </iframe>
    <div style="margin: .5rem 0 .5rem 0">
        <a href="/">SIGUIENTE JUGADOR</a>
    </div>
</div>