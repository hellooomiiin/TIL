const chatBox = document.getElementById('chat-box');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

function appendMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${sender}`;
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = text;
    msgDiv.appendChild(bubble);
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function botReply(userText) {
    // 심플한 챗봇 응답 (예시)
    if (userText.includes('안녕')) {
        return '안녕하세요! 무엇을 도와드릴까요?';
    } else if (userText.includes('이름')) {
        return '저는 심플 챗봇입니다.';
    } else {
        return '죄송해요, 이해하지 못했어요.';
    }
}

chatForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const text = userInput.value.trim();
    if (text) {
        appendMessage(text, 'user');
        setTimeout(() => {
            appendMessage(botReply(text), 'bot');
        }, 500);
        userInput.value = '';
    }
});
