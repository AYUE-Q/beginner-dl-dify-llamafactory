# beginner-dl-dify-llamafactory
面向小白的深度学习实践入门教程：本地环境部署指南、Dify应用搭建详解、LLaMA Factory模型微调实战。提供开箱即用的配置脚本和中文图文教程，帮助零基础用户快速构建AI应用。

基于自己实操的一些有关大模型的一些基础知识以及简单的实战,因为在网上很多教程都比较分裂,没有一个很好的实际案例,也是我自己的一些总结

## 1. 环境搭建
### python相关
因为很多地方都需要用到python,比如llamafactory的启动

推荐使用 [Anaconda](https://www.anaconda.com/download)如果你电脑上已经下载好了python等环境,没事,直接卸载就好了,因为你可以使用Anaconda创建一个一模一样的虚拟环境,也就是说你可以通过Anaconda创建不同的python环境以适应不同的工作,后面会详细介绍

没有魔法的小伙伴可以去国内镜像源安装 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/ (感觉能进GitHub的应该都有魔法吧)

详细的安装教程: https://zhuanlan.zhihu.com/p/1896552549621936802; 好了,安装完了之后要进行一些简单的配置,主要是下载源和虚拟环境创建的默认路径;

这里不建议你使用conda命令安装,因为他会安装到大环境里面,理想的做法是你先创建python虚拟环境,然后在虚拟环境中使用pip安装你想要的包

所以主要讲讲如何创建python虚拟环境, 并配置该环境的下载镜像源, 首先你需要检查你的conda安装虚拟环境的路径对不对(cmd或者powershell中运行)

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
conda activate myenv   # 激活环境
conda deactivate       # 退出环境
conda remove --name myenv --all  # 删除环境
```
### docker相关
docker是为了运行dify的,
