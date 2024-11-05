function getRedditInfo(url) {
    // Use URL constructor for easy parsing
    const parsedUrl = new URL(url);
    
    // Check the pathname for subreddit or user
    const pathSegments = parsedUrl.pathname.split('/').filter(segment => segment);
    console.log(pathSegments)
    
    if (pathSegments.length >= 2) {
        
        const type = pathSegments[0]; // This should be either 'r' or 'u'
        const name = pathSegments[1]; // The actual subreddit or username
        var sort = ""
        var time = ""

        if (pathSegments.length >= 3) {
            sort = pathSegments[2];
            if (pathSegments.length >= 4) {
                time = pathSegments[3];
            }
        }
        
        
        if (type === 'r') {
            return {
                type: 'subreddit',
                name: name,
                sort: sort
            };
        } else if (type === 'user') {
            return {
                type: 'user',
                name: name,
                sort: sort
            };
        }
    }
    
    return null; // Return null if not a valid subreddit/user URL
}


document.getElementById("analyze-button").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
        const currentTab = tabs[0]; // Get the first tab from the result
        if (currentTab) {
            const urlElement = document.getElementById("url");
            urlElement.textContent = currentTab.url; // Display the URL
            
            result = getRedditInfo(currentTab.url)
            console.log(result)
    
            // If this is a subreddit
            if (result.type == "subreddit") {
                const subredditElement = document.createElement("p");
                subredditElement.textContent = "You're on the " + result.name + " subreddit.";
                document.body.append(subredditElement);
    
                // Add a loading indicator
                const loadingMessage = document.createElement("p");
                loadingMessage.textContent = "Loading subreddit analysis...";
                document.body.append(loadingMessage);
    
                try {
                    const response = await fetch(`http://127.0.0.1:5000/subreddit-analysis?subreddit=${result.name}&sort=${result.sort}`)
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    //Remove loading message
                    loadingMessage.remove();
    
                    const data = await response.json(); 
                    document.body.append(data.message);
                    console.log(data);
    
                } catch (error) {
                    console.error("Error: ", error)
    
                }
                
            } else if (result.type == "user") {
                subredditElement.textContent = "You're on the profile of " + result.name + ".";
                document.body.append(subredditElement);
            }
            
        }
      });
    });
