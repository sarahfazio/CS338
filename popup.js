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

function formatSingleUserJson(data) {
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
        // Handle "Gaming" section
        if (data.Gaming) {
            const gamingContainer = document.createElement("div");
            gamingContainer.className = "gaming-section";

            // Games Section
            if (data.Gaming.Games && data.Gaming.Games.length > 0) {
                const gamesHeading = document.createElement("h3");
                gamesHeading.className = "section-heading";
                gamesHeading.textContent = "Games:";
                gamingContainer.appendChild(gamesHeading);

                const gamesList = document.createElement("ul");
                gamesList.className = "array-list";

                data.Gaming.Games.forEach(game => {
                    const gameLi = document.createElement("li");
                    gameLi.className = "array-item";
                    gameLi.textContent = game;
                    gamesList.appendChild(gameLi);
                });

                gamingContainer.appendChild(gamesList);
            }

            // Game Genres Section
            if (data.Gaming["Game Genres"] && data.Gaming["Game Genres"].length > 0) {
                const genresHeading = document.createElement("h3");
                genresHeading.className = "section-heading";
                genresHeading.textContent = "Game Genres:";
                gamingContainer.appendChild(genresHeading);

                const genresList = document.createElement("ul");
                genresList.className = "array-list";

                data.Gaming["Game Genres"].forEach(genre => {
                    const genreLi = document.createElement("li");
                    genreLi.className = "array-item";
                    genreLi.textContent = genre;
                    genresList.appendChild(genreLi);
                });

                gamingContainer.appendChild(genresList);
            }

            container.appendChild(gamingContainer);
        }

        // Handle "Gaming Summary" section
        if (data["Gaming Summary"]) {
            const summarySection = document.createElement("div");
            summarySection.className = "gaming-summary";

            const summaryHeading = document.createElement("h3");
            summaryHeading.textContent = "Gaming Summary:";
            summarySection.appendChild(summaryHeading);

            const summaryText = document.createElement("p");
            summaryText.textContent = data["Gaming Summary"];
            summarySection.appendChild(summaryText);

            container.appendChild(summarySection);
        }

        // Handle "Non Gaming Interests" section
        if (data["Non Gaming Interests"]) {
            const interestsContainer = document.createElement("div");
            interestsContainer.className = "non-gaming-section";

            // Interests Section
            if (data["Non Gaming Interests"].Interests && data["Non Gaming Interests"].Interests.length > 0) {
                const interestsHeading = document.createElement("h3");
                interestsHeading.className = "section-heading";
                interestsHeading.textContent = "Interests:";
                interestsContainer.appendChild(interestsHeading);

                const interestsList = document.createElement("ul");
                interestsList.className = "array-list";

                data["Non Gaming Interests"].Interests.forEach(interest => {
                    const interestLi = document.createElement("li");
                    interestLi.className = "array-item";
                    interestLi.textContent = interest;
                    interestsList.appendChild(interestLi);
                });

                interestsContainer.appendChild(interestsList);
            }

            // Interest Summary
            if (data["Non Gaming Interests"]["Interest summary"]) {
                const interestSummarySection = document.createElement("div");
                interestSummarySection.className = "interest-summary";

                const interestSummaryHeading = document.createElement("h3");
                interestSummaryHeading.textContent = "Interest Summary:";
                interestSummarySection.appendChild(interestSummaryHeading);

                const interestSummaryText = document.createElement("p");
                interestSummaryText.textContent = data["Non Gaming Interests"]["Interest summary"];
                interestSummarySection.appendChild(interestSummaryText);

                interestsContainer.appendChild(interestSummarySection);
            }

            container.appendChild(interestsContainer);
        }
        
    } else {
        console.error("Unsupported data type or format:", data);
        container.textContent = "Unsupported data format";
    }

    return container;
}
