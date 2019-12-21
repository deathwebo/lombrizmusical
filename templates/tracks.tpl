<div>
    % for track in tracks:
        <div>
            <h4>{{track['name']}} - {{track['artists']}}</h4>
            <div style="margin: .5rem 0 .5rem 0">
                <a href="/{{track['id']}}">SELECCIONAR</a>
            </div>
            <iframe 
                src="https://open.spotify.com/embed/track/{{track['id']}}" 
                height="380"
                frameborder="0"
                allowtransparency="true"
                allow="encrypted-media">
            </iframe>
        </div>
    % end
</div>