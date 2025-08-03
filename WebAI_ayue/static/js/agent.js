document.addEventListener('DOMContentLoaded', () => {
    const inputField = document.getElementById('user-input');
    const sendButton = document.getElementById('send-btn');
    const responseDisplay = document.getElementById('agent-response');
    
    // 移除欢迎信息
    function clearWelcome() {
        const welcome = document.querySelector('.welcome-message');
        if (welcome) welcome.remove();
    }
    
    // 格式化代码块为HTML
    function formatCodeBlocks(text) {
        // 支持多语言代码块
        return text.replace(/```(\w+)?\n([\s\S]*?)```/g, function(match, lang, code) {
            return `<pre><code class="language-${lang||'plaintext'}">${escapeHtml(code)}</code></pre>`;
        });
    }
    
    // HTML转义
    function escapeHtml(str) {
        return str.replace(/[<>&"]/g, function(c) {
            return {'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}[c];
        });
    }
    
    // 添加消息到对话框
    function addMessage(message, isUser = false) {
        clearWelcome();
        const messageEl = document.createElement('div');
        messageEl.className = `message ${isUser ? 'user' : 'agent'}`;
        messageEl.innerHTML = `
            <div class="bubble">${formatCodeBlocks(message)}</div>
        `;
        responseDisplay.appendChild(messageEl);
        responseDisplay.scrollTop = responseDisplay.scrollHeight;
        // 代码高亮
        if (window.hljs) {
            messageEl.querySelectorAll('pre code').forEach(block => hljs.highlightElement(block));
        }
    }
    
    // 处理用户输入
    async function handleSubmit() {
        const userInput = inputField.value.trim();
        if (!userInput) return;
        
        // 显示用户消息
        addMessage(userInput, true);
        inputField.value = '';
        
        try {
            // 调用后端智能体API
            const response = await fetch('/agent', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userInput })
            });
            
            const data = await response.json();
            // 模拟思考延迟
            setTimeout(() => {
                addMessage(data.response);
            }, 800);
            
        } catch (error) {
            addMessage('系统连接异常，请稍后再试');
        }
    }
    
    // 事件监听
    sendButton.addEventListener('click', handleSubmit);
    inputField.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSubmit();
    });
});