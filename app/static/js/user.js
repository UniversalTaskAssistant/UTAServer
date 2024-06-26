document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("createUserForm").addEventListener("submit", function(event) {
        event.preventDefault();
        createUser();
    });

    document.getElementById("getUserForm").addEventListener("submit", function(event) {
        event.preventDefault();
        getUser();
    });

    document.getElementById('loginForm').addEventListener('submit', async function(event) {
        event.preventDefault();
        login();
    });

    document.getElementById('deleteUserForm').addEventListener('submit', async function(event) {
        event.preventDefault();
        await deleteUser();
    });

    document.getElementById('refreshTokenButton').addEventListener('click', function(event) {
        refreshAccessToken();
    });

    document.getElementById('fetchTaskButton').addEventListener('click', function(event) {
        fetchTaskList();
    });

    document.getElementById("setupUserForm").addEventListener("submit", function(event) {
        event.preventDefault();
        setupUser();
    });

    document.getElementById("fetchConversationForm").addEventListener("submit", function(event) {
        event.preventDefault();
        fetchConversation();
    });

    document.getElementById("fetchAllConversationPreviewForm").addEventListener("submit", function(event) {
        event.preventDefault();
        fetchAllConversationPreview();
    });

    document.getElementById("fetchAllTaskForm").addEventListener("submit", function(event) {
        event.preventDefault();
        fetchAllPreviousTask();
    });

    document.getElementById("fetchAppListForm").addEventListener("submit", function(event) {
        event.preventDefault();
        setAppRecommendTask();
    });

    document.getElementById('declarationButton').addEventListener('click', function() {
        window.location.href = '/declaration.html';
    });

    document.getElementById('automationButton').addEventListener('click', function() {
        window.location.href = '/automation.html';
    });

    document.getElementById('chatButton').addEventListener('click', function() {
        window.location.href = '/chat.html';
    });

    document.getElementById('queryRAIButton').addEventListener('click', function() {
        window.location.href = '/queryrai.html';
    });
});
const accessToken = sessionStorage.getItem('accessToken');
function createUser() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch("/users/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, email, password })
    })
    .then(response => response.json())
    .then(data => showResult(data))
    .catch(error => console.error("Error:", error));
}

async function deleteUser() {
    const email = document.getElementById('deleteEmail').value;
    const password = document.getElementById('deletePassword').value;

    try {
        const response = await fetch('/users/delete', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'username': email,
                'password': password
            })
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        document.getElementById('result').textContent = 'User deletion successful.';
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'User deletion failed';
    }
}

function getUser() {
    const useruuid = document.getElementById("userUUId").value;

    fetch("/users/by-uuid/" + useruuid, {
        headers: {
            "Authorization": `Bearer ${accessToken}` 
        },})
    .then(response => response.json())
    .then(data => showResult(data))
    .catch(error => console.error("Error:", error));
}

function setupUser() {
    const userData = document.getElementById("userData").value;
    const accessToken = sessionStorage.getItem('accessToken');

    try {
        const parsedData = JSON.parse(userData);

        fetch("/users/setup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${accessToken}` 
            },
            body: JSON.stringify(parsedData)
        })
        .then(response => response.json())
        .then(data => showResult(data))
        .catch(error => console.error("Error:", error));
    } catch (error) {
        console.error("Invalid JSON:", error);
    }
}

function fetchConversation() {
    const convData = document.getElementById("convData").value;
    const accessToken = sessionStorage.getItem('accessToken');

    try {
        const parsedData = JSON.parse(convData);

        fetch("/conversation", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${accessToken}` 
            },
            body: JSON.stringify(parsedData)
        })
        .then(response => response.json())
        .then(data => showResult(data))
        .catch(error => console.error("Error:", error));
    } catch (error) {
        console.error("Invalid JSON:", error);
    }
}

function fetchAllConversationPreview() {
    const allConvData = document.getElementById("allConvData").value;
    const accessToken = sessionStorage.getItem('accessToken');

    try {
        const parsedData = JSON.parse(allConvData);

        fetch("/allconversationpreview", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${accessToken}` 
            },
            body: JSON.stringify(parsedData)
        })
        .then(response => response.json())
        .then(data => showResult(data))
        .catch(error => console.error("Error:", error));
    } catch (error) {
        console.error("Invalid JSON:", error);
    }
}

function fetchAllPreviousTask() {
    const allTaskData = document.getElementById("allTaskData").value;
    const accessToken = sessionStorage.getItem('accessToken');

    try {
        const parsedData = JSON.parse(allTaskData);

        fetch("/allprevioustask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${accessToken}` 
            },
            body: JSON.stringify(parsedData)
        })
        .then(response => response.json())
        .then(data => showResult(data))
        .catch(error => console.error("Error:", error));
    } catch (error) {
        console.error("Invalid JSON:", error);
    }
}

function setAppRecommendTask() {
    const appListData = document.getElementById("appListData").value;
    const accessToken = sessionStorage.getItem('accessToken');

    try {
        const parsedData = JSON.parse(appListData);

        fetch("/setapprecommendtask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${accessToken}` 
            },
            body: JSON.stringify(parsedData)
        })
        .then(response => response.json())
        .then(data => showResult(data))
        .catch(error => console.error("Error:", error));
    } catch (error) {
        console.error("Invalid JSON:", error);
    }
}

function showResult(data) {
    const resultDiv = document.getElementById("result");
    resultDiv.textContent = JSON.stringify(data, null, 2);
}

async function login() {
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    try {
        const response = await fetch('/users/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'username': email,
                'password': password
            })
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const data = await response.json();
        sessionStorage.setItem('accessToken', data.token.access_token);
        sessionStorage.setItem('refreshToken', data.token.refresh_token);
        document.getElementById('result').textContent = 'Login successful. Token: ' + data.token.access_token;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'Login failed';
    }
}

async function refreshAccessToken() {
    try {
        const refreshToken = sessionStorage.getItem('refreshToken');
        const response = await fetch('/users/refreshtoken', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ refresh_token: refreshToken }) // Sending agent_name in the request body
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('New Access Token:', data.access_token);

        // Save the new access token for future requests
        sessionStorage.setItem('accessToken', data.access_token);

        // Update the UI or inform the user
        document.getElementById('result').textContent = 'Token refreshed successfully.' + data.access_token;
    } catch (error) {
        console.error('Error refreshing access token:', error);
        document.getElementById('result').textContent = 'Error refreshing token.';
    }
}

async function fetchTaskList() {
    try {
        const accessToken = sessionStorage.getItem('accessToken');

        if (!accessToken) {
            throw new Error('Access token not found. Please login first.');
        }

        const response = await fetch('/tasklist', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${accessToken}` 
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const taskList = await response.json();

        console.log('Fetched Task List:', taskList);
        document.getElementById('result').textContent = 'Task list: ' + JSON.stringify(taskList);

    } catch (error) {
        console.error('Error fetching task list:', error);
    }
}
