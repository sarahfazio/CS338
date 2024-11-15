function isRedditURL(url) {
    try {
        console.log("trying to get reddit url")
        const parsedUrl = new URL(url);
        const hostname = parsedUrl.hostname;
        // Check for both www.reddit.com and reddit.com
        return hostname.endsWith('reddit.com');
    } catch (error) {
        // If URL parsing fails, we know it's not a valid URL
        return false;
    }
}
  

function getRedditInfo(url) {
    const parsedUrl = new URL(url);
    const pathSegments = parsedUrl.pathname.split('/').filter(segment => segment);
    console.log(pathSegments);
    
    if (pathSegments.length >= 2) {
        const type = pathSegments[0];
        const name = pathSegments[1];
        let sort = "";
        let time = "";

        if (pathSegments.length >= 3) {
            sort = pathSegments[2];
            if (pathSegments.length >= 4) {
                time = pathSegments[3];
            }
        }
        
        if (type === 'r') {
            return { type: 'subreddit', name, sort };
        } else if (type === 'user') {
            return { type: 'user', name, sort };
        }
    }
    
    return null;
}

document.getElementById("analyze-button").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
        const currentTab = tabs[0];
        if (currentTab) {
            const outputElement = document.getElementById("output");
            outputElement.innerHTML = ''; // Clear previous output
            if (isRedditURL(currentTab.url)) {
                const result = getRedditInfo(currentTab.url);
    
                if (result && result.type === "subreddit") {
                    // Display loading message
                    const loadingMessage = document.createElement("p");
                    loadingMessage.textContent = "Loading subreddit analysis...";
                    outputElement.append(loadingMessage);
    
                    try {
                        const response = await fetch(`http://127.0.0.1:5000/subreddit-analysis?subreddit=${result.name}&sort=${result.sort}`);
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
    
                        loadingMessage.remove(); // Remove loading message
                        
                        // Fetch response as text, clean it, and parse it
                        let textData = await response.text();
                        textData = textData.replace(/```json|```/g, ''); // Remove any markdown artifacts
    
                        // Parse finalData as JSON if it's still a string
                        let displayData = JSON.parse(textData);
                        
                        console.log("Final Parsed Display Data:", displayData); // Confirm the structure
    
                        // Pass the correctly parsed data to formatJson
                        outputElement.appendChild(formatJson(displayData));
                        
                    } catch (error) {
                        console.error("Error details:", error);
                        outputElement.textContent = "An error occurred while fetching data: " + error.message;
                    }
                    
                } else if (result && result.type == "user") {
                    // Display loading message
                    const loadingMessage = document.createElement("p");
                    loadingMessage.textContent = "Loading user analysis...";
                    outputElement.append(loadingMessage);
    
                    try {
                        const response = await fetch(`http://127.0.0.1:5000/user-analysis?username=${result.name}&sort=${result.sort}`);
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
    
                        loadingMessage.remove(); // Remove loading message
                        
                        // Fetch response as text, clean it, and parse it
                        let textData = await response.text();
                        textData = textData.replace(/```json|```/g, ''); // Remove any markdown artifacts
    
                        // Parse finalData as JSON if it's still a string
                        let displayData = JSON.parse(textData);
                        
                        console.log("Final Parsed Display Data:", displayData); // Confirm the structure
    
                        // Pass the correctly parsed data to formatJson
                        outputElement.appendChild(formatSingleUserJson(displayData));
                        
                    } catch (error) {
                        console.error("Error details:", error);
                        outputElement.textContent = "An error occurred while fetching data: " + error.message;
                    }
                } else {
                    outputElement.textContent = "This feature is for subreddits or user profiles only.";
                }
            }
            else {
                outputElement.innerHTML = "You are not on Reddit. Please navigate to a subreddit or user profile.";
            }   
        }
    });
});