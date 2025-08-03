# beginner-dl-dify-llamafactory
面向小白的深度学习实践入门教程：本地环境部署指南、Dify应用搭建详解、LLaMA Factory模型微调实战。提供开箱即用的配置脚本和中文图文教程，帮助零基础用户快速构建AI应用。

基于自己实操的一些有关大模型的一些基础知识以及简单的实战,因为在网上很多教程都比较分裂,没有一个很好的实际案例,也是我自己的一些总结

## 1. 环境搭建
### python相关
因为很多地方都需要用到python,比如llamafactory的启动

推荐使用 [Anaconda](https://www.anaconda.com/download)如果你电脑上已经下载好了python等环境,没事,直接卸载就好了,因为你可以使用Anaconda创建一个一模一样的虚拟环境,也就是说你可以通过Anaconda创建不同的python环境以适应不同的工作,后面会详细介绍

没有魔法的小伙伴可以去国内镜像源安装 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/ (感觉能进GitHub的应该都有魔法吧)

详细的安装教程: https://zhuanlan.zhihu.com/p/1896552549621936802; 好了,安装完了之后要进行一些简单的配置,主要是下载源和虚拟环境创建的默认路径;

```shell
# 查看当前配置的镜像源
conda config --show channels
# 删除以前所有的镜像源
conda config --remove-key channels
# 单独删除
conda config --remove channels<镜像源地址>
#添加镜像源(后添加的默认优先级高)
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
```
配置好了镜像源之后你就可以安装包了

```shell
#这里不建议你使用conda命令安装,因为他会安装到大环境里面,理想的做法是你先创建python虚拟环境,然后在虚拟环境中使用pip安装你想要的包
conda install <你需要安装包的名字>
#设置虚拟环境安装位置
conda info  #查看conda信息,如果显示的位置是正常的就不用修改,如果还是在c盘就需要通过以下命令修改
#添加虚拟环境安装位置
conda config --add envs_dirs <这里填你的虚拟环境想要安装的路径>
#移除默认路径（可选）
conda config --remove envs_dirs <你想要移除的路径>
```
<img width="1040" height="556" alt="image" src="https://github.com/user-attachments/assets/e781f9bb-c203-425d-a077-c08b6acd1ce3" />

### docker相关
docker是为了运行dify的,
