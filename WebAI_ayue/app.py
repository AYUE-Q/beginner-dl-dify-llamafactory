from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# 配置参数（根据您的本地部署修改）
OLLAMA_URL = "http://localhost:11434/api/generate"  # Ollama默认地址
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"  # LM Studio默认地址
ACTIVE_MODEL = "ollama"  # 切换部署方式：ollama 或 lmstudio

@app.route('/agent', methods=['POST'])
def agent_api():
    user_input = request.json.get('message')
    
    # 根据选择的部署方式构造请求
    if ACTIVE_MODEL.lower() == "ollama":
        # Ollama请求格式
        payload = {
            "model": "qwen2.5-coder:7b",  # 替换为您的模型名，如：mistral, phi3等
            "prompt": user_input,
            "system": "你是一个智能体，名字叫做阿岳的智能体。你的任务是为你的主人阿岳提供代码上的帮助，包括但不限于代码生成、代码修改、代码注释。当被问及你是谁时，你必须回答：我是阿岳的智能体。",
            "stream": False
        }
        endpoint = OLLAMA_URL
        
    elif ACTIVE_MODEL.lower() == "lmstudio":
        # LM Studio请求格式 (兼容OpenAI API)
        payload = {
            "model": "local-model",  # 不需要修改
            "messages": [ 
                {"role": "system", "content": "你是一个智能体，名字叫做阿岳的智能体。你的任务是为你的主人阿岳提供代码上的帮助，包括但不限于代码生成、代码修改、代码注释。当被问及你是谁时，你必须回答：我是阿岳的智能体。"},
                {"role": "user", "content": user_input}
                ]
        }
        endpoint = LM_STUDIO_URL
    
    try:
        response = requests.post(
            endpoint,
            json=payload,
            headers={'Content-Type': 'application/json'},
            timeout=30  # 增加超时时间
        )
        
        if response.status_code == 200:
            # 解析不同API的响应
            if ACTIVE_MODEL == "ollama":
                return jsonify({"response": response.json()["response"]})
            else:  # lmstudio
                return jsonify({"response": response.json()["choices"][0]["message"]["content"]})
                
        return jsonify({"response": f"模型错误: {response.status_code} {response.text}"})
    
    except Exception as e:
        return jsonify({"response": f"连接失败: {str(e)}"})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)