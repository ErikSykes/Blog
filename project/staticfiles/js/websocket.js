
// Construct WebSocket URI dynamically
const topicId = document.getElementById('comment-list').getAttribute('data-topic-id');

// Create WebSocket connection
const websocket = new WebSocket(wsUri);

// Event handler for incoming WebSocket messages
websocket.onmessage = function (event) {
    // Handle incoming WebSocket messages (new comments)
    var newComment = JSON.parse(event.data)['comment'];
    var commentList = document.getElementById('comment-list');

    // Append the new comment to the comment list
    var newCommentElement = document.createElement('div');
    newCommentElement.className = 'list-group-item';
    newCommentElement.innerHTML = `
        <div class="d-flex w-100 justify-content-between">
            <h5 class="mb-1">${newComment.body}</h5>
            <small>${newComment.user.username}</small>
        </div>`;
    commentList.appendChild(newCommentElement);

    // Show the "New Messages" button
    var newMessagesBtn = document.getElementById('new-messages-btn');
    newMessagesBtn.style.display = 'block';
}

document.addEventListener("DOMContentLoaded", function () {
    const addCommentBtn = document.getElementById('add-comment-btn');

    addCommentBtn.addEventListener('click', function () {
        // Get the comment text from the textarea
        const commentText = document.getElementById('comment-text').value.trim();

        // Check if the comment text is not empty
        if (commentText) {
            // Submit the form
            document.getElementById('comment-form').submit();

            // Clear the textarea after submission
            document.getElementById('comment-text').value = '';
        } else {
            // If the comment text is empty, display an alert or handle it as needed
            alert('Please write a comment before adding.');
        }
    });
});
