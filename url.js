function getRedditInfo(url) {
    // Use URL constructor for easy parsing
    const parsedUrl = new URL(url);
    
    // Check the pathname for subreddit or user
    const pathSegments = parsedUrl.pathname.split('/').filter(segment => segment);
    console.log(pathSegments)
    
    if (pathSegments.length === 2) {
        
        const type = pathSegments[0]; // This should be either 'r' or 'u'
        const name = pathSegments[1]; // The actual subreddit or username
        
        if (type === 'r') {
            return {
                type: 'subreddit',
                name: name
            };
        } else if (type === 'user') {
            return {
                type: 'user',
                name: name
            };
        }
    }
    
    return null; // Return null if not a valid subreddit/user URL
}

// Get the current active tab
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const currentTab = tabs[0]; // Get the first tab from the result
    if (currentTab) {
        const urlElement = document.getElementById("url");
        urlElement.textContent = currentTab.url; // Display the URL
        
        // if this is subreddit
        
        result = getRedditInfo(currentTab.url)
        console.log(result)

        const subredditElement = document.createElement("p");
        if (result.type == "subreddit") {
            subredditElement.textContent = "You're on the " + result.name + " subreddit.";
            fetch("http://127.0.0.1:5000/subreddit-analysis")
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.error("Error: ", error);
                })
        } else if (result.type == "user") {
            subredditElement.textContent = "You're on the profile of " + result.name + ".";
        }
        document.body.append(subredditElement);
    }
  });