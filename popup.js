
document.addEventListener('DOMContentLoaded', () => {
    // Query the active tab when the popup opens
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const currentTab = tabs[0];
        if (currentTab) {
            const url = currentTab.url;
            const result = getRedditInfo(url);
            // Update the analyze button based on the page type
            if (result && result.type === 'user') {
                updateAnalyzeButtonForUserPage(true);
            } else {
                updateAnalyzeButtonForUserPage(false);
            }
        }
    });
});

// Function to update the button state based on whether it's a user page or subreddit page
function updateAnalyzeButtonForUserPage(isUserPage) {
    const analyzeButton = document.getElementById("analyze-button");

    if (isUserPage) {
        // Change button text or style for user page
        analyzeButton.textContent = "Analyze User Profile";
        analyzeButton.classList.add("active"); // Add any styles for active state
    } else {
        // Default button state for subreddit page or any other page
        analyzeButton.textContent = "Analyze This Subreddit";
        analyzeButton.classList.remove("active"); // Remove any specific styles
    }
}

function formatJson(data) {
    console.log("Data received by formatJson:", data); // Log the structure of data
    console.log("Data type:", typeof data);

    const container = document.createElement("div");
    container.className = "json-output";

    // If data has a "message" key, use that as the main content if it's an object
    if (data.message) {
        try {
            data = typeof data.message === 'string' ? JSON.parse(data.message) : data.message;
        } catch (error) {
            console.error("Error parsing data.message:", error);
            container.textContent = "An error occurred: Unsupported data format in message.";
            return container;
        }
    }

    if (typeof data === 'object' && data !== null) {
        // If data is an object, handle each key-value pair
        for (const username in data) {
            const userContainer = document.createElement("div");
            userContainer.className = "main-item";

            // Display username as a heading
            const usernameHeading = document.createElement("span");
            usernameHeading.className = "list-heading";
            usernameHeading.textContent = username;
            userContainer.appendChild(usernameHeading);

            // Create a sub-list for Games and Game Genres
            const subList = document.createElement("ul");
            subList.className = "sub-list";

            if (data[username].Games) {
                const gamesLi = document.createElement("li");
                gamesLi.className = "sub-heading";
                gamesLi.textContent = "Games:";

                const gamesUl = document.createElement("ul");
                gamesUl.className = "array-list";

                data[username].Games.forEach(game => {
                    const gameLi = document.createElement("li");
                    gameLi.className = "array-item";
                    gameLi.textContent = game;
                    gamesUl.appendChild(gameLi);
                });

                gamesLi.appendChild(gamesUl);
                subList.appendChild(gamesLi);
            }

            if (data[username]["Game Genres"]) {
                const genresLi = document.createElement("li");
                genresLi.className = "sub-heading";
                genresLi.textContent = "Game Genres:";

                const genresUl = document.createElement("ul");
                genresUl.className = "array-list";

                data[username]["Game Genres"].forEach(genre => {
                    const genreLi = document.createElement("li");
                    genreLi.className = "array-item";
                    genreLi.textContent = genre;
                    genresUl.appendChild(genreLi);
                });

                genresLi.appendChild(genresUl);
                subList.appendChild(genresLi);
            }

            userContainer.appendChild(subList);
            container.appendChild(userContainer);
        }
    } else {
        console.error("Unsupported data type or format:", data);
        container.textContent = "Unsupported data format";
    }

    return container;
}

function formatSingleUserJson(username, data) {
    console.log("Data received by formatJson:", data); // Log the structure of data
    console.log("Data type:", typeof data);

    const container = document.createElement("div");
    container.className = "json-output";

    const usernameHeader = document.createElement("h2"); // Create a larger header (h1)
    usernameHeader.className = "username-header"; // Add a class for styling (optional)
    usernameHeader.textContent = username; // Set the username as text content
    container.appendChild(usernameHeader); // Append it to the container

    // If data has a "message" key, use that as the main content if it's an object
    console.log("Data received:", data);
    if (data.message) {
        try {
            data = typeof data.message === 'string' ? JSON.parse(data.message) : data.message;
        } catch (error) {
            console.error("Error parsing data.message:", error);
            container.textContent = "An error occurred: Unsupported data format in message.";
            return container;
        }
    }

    if (typeof data === 'object' && data !== null) {
        // Handle "Gaming" section
        if (data.Gaming) {
            const gamingContainer = document.createElement("div");
            gamingContainer.className = "gaming-section";

            const gamingHeading = document.createElement("span");
            gamingHeading.className = "list-heading";
            gamingHeading.textContent = "Gaming";

            gamingContainer.appendChild(gamingHeading)

            // Create a sub-list for Games and Game Genres
            const subList = document.createElement("ul");
            subList.className = "sub-list";

            if (data.Gaming.Games) {
                const gamesLi = document.createElement("li");
                gamesLi.className = "sub-heading";
                gamesLi.textContent = "Games:";

                const gamesUl = document.createElement("ul");
                gamesUl.className = "array-list";

                data.Gaming.Games.forEach(game => {
                    const gameLi = document.createElement("li");
                    gameLi.className = "array-item";
                    gameLi.textContent = game;
                    gamesUl.appendChild(gameLi);
                });

                gamesLi.appendChild(gamesUl);
                subList.appendChild(gamesLi);
            }

            if (data.Gaming["Game Genres"]) {
                const genresLi = document.createElement("li");
                genresLi.className = "sub-heading";
                genresLi.textContent = "Game Genres:";

                const genresUl = document.createElement("ul");
                genresUl.className = "array-list";

                data.Gaming["Game Genres"].forEach(genre => {
                    const genreLi = document.createElement("li");
                    genreLi.className = "array-item";
                    genreLi.textContent = genre;
                    genresUl.appendChild(genreLi);
                });

                genresLi.appendChild(genresUl);
                subList.appendChild(genresLi);
            }

            if(data["Gaming Summary"]) {
                const gamingSummary = document.createElement("li");
                gamingSummary.className = "sub-heading";
                gamingSummary.textContent = "Gaming Summary";

                const summaryUl = document.createElement("ul");
                summaryUl.className = "array-list";
                const summaryLi = document.createElement("li");
                summaryLi.className = "array-item";
                summaryLi.textContent = data["Gaming Summary"]
                summaryUl.appendChild(summaryLi);
                gamingSummary.appendChild(summaryUl);
                
                subList.appendChild(gamingSummary)
            }

            gamingContainer.appendChild(subList);
            container.appendChild(gamingContainer);            
            
        }
        //Non Gaming Interests
        if(data["Non Gaming Interests"]) {
            const nongamingContainer = document.createElement("div");
            nongamingContainer.className = "nongaming-section";

            const nongamingHeading = document.createElement("span");
            nongamingHeading.className = "list-heading";
            nongamingHeading.textContent = "Non-Gaming Interests";

            nongamingContainer.appendChild(nongamingHeading)

            

            //sublist for Non Gaming section
            const subList = document.createElement("ul");
            subList.className = "sub-list";

            if (data["Non Gaming Interests"]["Interests"]) {
                const interestsLi = document.createElement("li");
                interestsLi.className = "sub-heading";
                interestsLi.textContent = "Game Genres:";

                const interestsUl = document.createElement("ul");
                interestsUl.className = "array-list";

                data["Non Gaming Interests"]["Interests"].forEach(interest => {
                    const interestsLi = document.createElement("li");
                    interestsLi.className = "array-item";
                    interestsLi.textContent = interest;
                    interestsUl.appendChild(interestsLi);
                });

                interestsLi.appendChild(interestsUl);
                subList.appendChild(interestsLi);
            }

            if (data["Non Gaming Interests"]["Interest Summary"]) {
                const interestSummary = document.createElement("li");
                interestSummary.className = "sub-heading";
                interestSummary.textContent = "Gaming Summary";

                const summaryUl = document.createElement("ul");
                summaryUl.className = "array-list";
                const summaryLi = document.createElement("li");
                summaryLi.className = "array-item";
                summaryLi.textContent = data["Gaming Summary"]
                summaryUl.appendChild(summaryLi);
                interestSummary.appendChild(summaryUl);
                
                subList.appendChild(interestSummary)
            }

            nongamingContainer.appendChild(subList);
            container.appendChild(nongamingContainer);
        }
        
    } else {
        console.error("Unsupported data type or format:", data);
        container.textContent = "Unsupported data format";
    }

    return container;
}

// Handler for analyzing Reddit username
document.getElementById("username-analyze-button").addEventListener("click", async () => {
    const username = document.getElementById("reddit-username").value.trim();
    const outputElement = document.getElementById("output");
    outputElement.innerHTML = ''; // Clear previous output

    if (!username) {
        alert('Please enter a Reddit username.');
        return;
    }

    var analyzeSubredditButton = document.getElementById("analyze-button");

    //Delete the input box and analyze button
    document.getElementById("username-analyze-button").remove();
    document.getElementById("reddit-username").remove();
    document.getElementById("username-prompt").remove();

    // Create a new text element
    var newText = document.createElement("p");
    newText.textContent = "Click to generate subreddit matches for " + username;

    newText.classList.add("new-text");

    analyzeSubredditButton.insertAdjacentElement("beforebegin", newText);

    // Display loading message
    const loadingMessage = document.createElement("p");
    loadingMessage.textContent = "Loading user analysis...";
    outputElement.append(loadingMessage);

    try {
        // Send a request to the Flask backend
        const response = await fetch(`http://127.0.0.1:5000/user-analysis?username=${username}&stored=True`);
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        loadingMessage.remove(); // Remove loading message

        // Fetch response as text, clean it, and parse it
        let textData = await response.text();
        textData = textData.replace(/```json|```/g, ''); // Remove any markdown artifacts

        // Parse the response as JSON
        const displayData = JSON.parse(textData);

        console.log("Final Parsed Display Data:", displayData); // Confirm the structure
    } catch (error) {
        console.error("Error details:", error);
        outputElement.textContent = "An error occurred while fetching user data: " + error.message;
    }
});
