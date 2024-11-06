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