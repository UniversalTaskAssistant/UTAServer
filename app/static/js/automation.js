document.addEventListener('DOMContentLoaded', function() {
    const uploadButton = document.getElementById('uploadButton');
    const submitButton = document.getElementById('submitButton');
    const accessToken = sessionStorage.getItem('accessToken');
    //let websocket = new WebSocket(`ws://localhost:8000/ws/automation?token=${accessToken}`);
    let websocket = new WebSocket(`wss://api.apputa.online/ws/automation?token=${accessToken}`);


    websocket.onopen = function(event) {
        console.log('WebSocket Connected');
    };

    websocket.onerror = function(event) {
        console.error('WebSocket Error: ' + event.message);
    };

    websocket.onmessage = function(event) {
        const message = JSON.parse(event.data);
    
        if (message.type && message.type === 'progress') {
            // Update progress bar
            const progressBar = document.getElementById('uploadProgress');
            progressBar.value = message.value;
        } else {
            // Handle other messages
            document.getElementById('result').innerText += event.data + '\n';
        }   
     };

    websocket.onclose = function(event) {
        console.log('WebSocket Closed: ' + event.reason);
    };

    uploadButton.addEventListener('click', function() {
        const file = document.getElementById('fileInput').files[0];
        const xml = document.getElementById('xmlInput').value;
        sendFileAndXml(file, xml);
    });

    submitButton.addEventListener('click', function() {
        const data = document.getElementById('dataInput').value;
        if (websocket && websocket.readyState === WebSocket.OPEN) {
            websocket.send(data);
        }
    });

    function sendFileAndXml(file, xml) {
        if (websocket && websocket.readyState === WebSocket.OPEN) {
            // Send file metadata
            const metadata = { file_size: file.size, xml: xml };
            websocket.send(JSON.stringify(metadata));

            // Start uploading file
            const chunkSize = 1024; // Adjust chunk size as needed
            const reader = new FileReader();
            let offset = 0;

            reader.onload = function(event) {
                if (!event.target.error) {
                    websocket.send(event.target.result);
                    offset += event.target.result.byteLength;
                    readNextChunk();
                } else {
                    console.log('Read error: ' + event.target.error);
                }
            };

            function readNextChunk() {
                if (offset < file.size) {
                    const slice = file.slice(offset, offset + chunkSize);
                    reader.readAsArrayBuffer(slice);
                }
            }

            readNextChunk();
        } else {
            console.log('WebSocket is not connected');
        }
    }
});
