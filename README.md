# beginner-dl-dify-llamafactory
面向小白的生成式AI实践入门教程：本地环境部署指南、Dify应用搭建详解、LLaMA Factory模型微调实战。提供开箱即用的配置脚本和中文图文教程，帮助零基础用户快速构建AI应用。

基于自己实操的一些有关大模型的一些基础知识以及简单的实战,因为在网上很多教程都比较分裂,没有一个很好的实际案例,也是我自己的一些总结

## 一、环境搭建
### python
因为很多地方都需要用到python,比如llamafactory的启动

推荐使用 [Anaconda](https://www.anaconda.com/download)如果你电脑上已经下载好了python等环境,没事,直接卸载就好了,因为你可以使用Anaconda创建一个一模一样的虚拟环境,也就是说你可以通过Anaconda创建不同的python环境以适应不同的工作,后面会详细介绍

没有魔法的小伙伴可以去国内镜像源安装 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/ (感觉能进GitHub的应该都有魔法吧)

详细的安装教程: https://zhuanlan.zhihu.com/p/1896552549621936802; 好了,安装完了之后要进行一些简单的配置,主要是下载源和虚拟环境创建的默认路径;

这里不建议你使用conda命令安装包,因为他会安装到大环境里面,理想的做法是你先创建python虚拟环境,然后在虚拟环境中使用pip安装你想要的包

所以主要讲讲如何创建python虚拟环境, 并配置该环境的下载镜像源, 首先你需要检查你的conda安装虚拟环境的路径对不对

在命令行中运行(cmd powershell)

```shell
#查看conda信息,如果显示的位置是正常的就不用修改,如果还是在c盘就需要通过以下命令修改
conda info  
#添加虚拟环境安装位置
conda config --add envs_dirs <这里填你的虚拟环境想要安装的路径>
#移除默认路径（可选）
conda config --remove envs_dirs <你想要移除的路径>
```
正常你应该显示如下图所示:

<img width="1151" height="180" alt="image" src="https://github.com/user-attachments/assets/86769d35-c0a3-4d6c-98d2-c54f1e8df093" />

然后就是使用conda创建虚拟环境:

```shell
conda create -n py39 python=3.9 numpy pandas
# 上面的命令表示我创建了一个名为py39的python版本为3.9的环境,附加了numpy和pandas包
conda env list         # 查看所有环境
conda activate py39   # 激活环境
conda deactivate       # 退出环境
conda remove -n py39 --all  # 删除环境
```
使用conda activate激活了环境之后你会看到你的命令行左边的括号就显示了你的环境名称, 然后设置当前python环境的镜像源(想在哪个环境就conda activate <环境名>)

```shell
# 设置主镜像源（清华源）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 设置附加镜像源（官方源）
pip config set global.extra-index-url https://pypi.org/simple
# 验证一下
pip config list
```

显示下图代表已经配置好了

<img width="840" height="90" alt="image" src="https://github.com/user-attachments/assets/3fb5d7c8-242d-409f-a752-1f111a1adaae" />

接下来你就可以在当前环境使用

```shell
pip install <包名> 下载包了
```
!!! 注意一定要先激活环境

## 二、大模型本地部署

### 1. Ollama 安装与模型路径设置

#### 安装步骤

下载安装包： 官网(https://ollama.com/)   无法自定义下载路径

默认路径为：Windows：C:\Users\用户名\AppData\Local\Programs\Ollama

验证安装： 命令行输入 ollama --version，显示版本号即成功 

<img width="1203" height="597" alt="image" src="https://github.com/user-attachments/assets/5c19baae-4601-476a-8437-aa8439f52a60" />

红框里可以调用你下载好的模型

#### 自定义模型安装位置

操作步骤：在目标盘（如D盘）新建文件夹 Ollama，内部创建子文件夹 models

移动默认文件：将 C:\Users\用户名\AppData\Local\Programs\Ollama 内容剪切到 D:\Ollama

将 C:\Users\用户名\.ollama\models 内容剪切到 D:\Ollama\models

设置环境变量：直接搜索编辑系统环境变量  

编辑 Path,新增值 D:\Ollama\

新建变量名 OLLAMA_MODELS，值 D:\Ollama\models

#### 模型下载

在命令行使用如下命令

```shell
# 模型下载
ollama pull <模型名字> 
# 注意要带上完整名称,比如deepseek-r1:1.5b,后面的b是模型的大小,非常吃电脑的配置

# 模型运行
ollama run <模型名字>

# 查看已下载的模型
ollama list

# 卸载模型
ollama rm <模型名字>
```

###  2. LMstudio安装与模型路径设置

#### 安装步骤

下载安装包： 官网(https://lmstudio.ai)  可以自定义下载路径 

#### 自定义模型安装位置

下载完成之后打开客户端

<img width="1494" height="999" alt="image" src="https://github.com/user-attachments/assets/6afa1940-5b43-4fa8-a4cd-ebfb39890657" />

如图所示可以自定义路径

#### 模型下载

LMstudio 模型的下载是从Hugging Face进行下载的, 可以直接在UI界面里面搜索可以下载的模型

后面使用Llama Factory微调时也需要Hugging Face源下载的模型

#### Hugging Face模型下载

在python环境中: 

```shell
# 下载对应的包
pip install huggingface_hub

# 如果你要下载 私有模型 或使用高权限 API 访问，需要登录 Hugging Face 账户。
huggingface-cli login

#下载模型(安装到指定路径)
huggingface-cli download deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --local-dir D:\LLM\Huggingface_model\deepseek-ai\DeepSeek-R1-Distill-Qwen-1.5B
```

## 三、Dify与Docker

### 什么是Dify?

Dify 是一款开源的大语言模型（LLM）应用开发平台，旨在简化和加速生成式 AI 应用的创建和部署。

Dify 内置了构建 LLM 应用所需的关键技术，包括：
* Prompt 编排界面：直观地设计和调整提示词。

* RAG（检索增强生成）引擎：增强模型对特定数据的处理能力。
 
* Agent 框架：支持智能助手型应用，能自主拆解复杂任务。
 
* 灵活的工作流：支持多步骤任务的编排与自动化 

它的界面长这个样子:

<img width="2549" height="1367" alt="image" src="https://github.com/user-attachments/assets/cc7125d3-0b0b-40af-85f7-ea246ad43d93" />

### 什么是Docker?

Docker 是一个开源的容器化平台，用于开发、交付和运行应用程序。它通过容器技术，将应用程序及其依赖打包成标准化的单元，便于在不同环境中快速部署和运行。

概括来说: Docker 是 Dify 的底层运行和部署工具，而 Dify 是建立在 Docker 之上的应用开发平台。所以说需要先下载docker才能运行Dify.

### 如何下载?

首先下载好Docker (https://www.docker.com)

然后根据这个教程 (https://www.runoob.com/w3cnote/dify-ai-intro.html) 进行安装
