# Master-art-punk
##### Make your master artistic punk avatar through machine learning world famous paintings.
##### 通过机器学习世界名画制作属于你的大师级艺术朋克头像
##### Nowadays, NFT is becoming popular in the world, and various trading platforms like opensea have developed rapidly, and cryptopunks have even sold tens of millions of dollars.
##### 如今，NFT在世界上正流行起来，各种交易平台像opensea等，快速发展了起来，像cryptopunks甚至卖出了上千万美金。
##### This project will help you to know in general how these NFT pictures are made, and try to make your own NFT.
![punk1](https://cdn.jsdelivr.net/gh/philipjhc/Master-art-punk@main/Master-art-punk/cover_photo/example.png)
![punk2](https://cdn.jsdelivr.net/gh/philipjhc/Master-art-punk@main/Master-art-punk/cover_photo/example.png)
##### 这个项目将有助于你大体知道这些NFT的图片是如何制作的，并尝试制作自己的NFT。
##### This project uses the K-Means algorithm to acquire and learn the color matching of world famous paintings in the data set, and imitate its color style to color the model.
##### 本项目运用了K-Means算法对数据集中世界名画的色彩搭配进行获取和学习，并模仿其色彩风格给模型上色,展示如下：
![NFT1](https://cdn.jsdelivr.net/gh/philipjhc/Master-art-punk@main/Master-art-punk/cover_photo/NFT1.png)
![NFT4](https://cdn.jsdelivr.net/gh/philipjhc/Master-art-punk@main/Master-art-punk/cover_photo/NFT4.png)
## 使用说明：
### 1.安装要求：
#### 1.更改settings.py参数路径
#### 2.安装numpy和pypng:pip install numpy / pip install pypng
### 2.训练：
#### 1.将setting.py改为train = True
#### 2.python app.py
#### 3.运行后，会输出对应模型路径./output/csv/XXXXXXXXXX.csv
### 3.生成
#### 1.将setting.py改为train = False
#### 2.将setting.py中color_model_path修改为对应路径
#### 3.python app.py
#### 4../output/中查看生成图像
