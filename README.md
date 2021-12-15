# これはなにか

シャーレ上のカビの面積比を測るツールを作りました

# どうやって使うか

1. まず写真のサンプルを集めます
2. カビのある面積に縁をぬりえして、画像を加工します(二値化するために)
3. このツールを使って面積比を計算しましょう

# インストール方法

まずPythonがPCに入っているのが前提です。私の環境では`Python3.7`以降を使っています。

## Pythonの環境構築方法

Pragateの記事が初心者でもわかりやすいと思います。

- [WindowsでPythonをインストールする方法](https://prog-8.com/docs/python-env-win)
- [MacでPythonをインストールする方法](https://prog-8.com/docs/python-env)

## ツールを使うのに必要なライブラリをインストール

Pythonをインストールしただけだとまだこのツールを使うことはできません。

ネットから他の人が作ったプログラムを借りて動作させます。そのためにライブラリをインストールする必要がありますので、以下のコマンドをターミナルに打ち込みましょう。

1. [NumPyのインストール](https://pypi.org/project/numpy/)
    
    ```bash
    pip install numpy
    ```
    
2. [OpenCVのインストール](https://pypi.org/project/opencv-python/)
    
    ```bash
    pip install opencv-python
    ```
    
3. [matplotlibのインストール](https://pypi.org/project/matplotlib/)
    
    ```bash
    pip install matplotlib
    ```
    

### ツールの起動

Pythonスクリプトの起動をします。

Progateの"Pythonのコードを実行する"のページがどのようにしてPythonを起動させるのかわかりやすいので、初めてPythonを動かす人は一通りやってみることをお勧めします。

[Progate : **Pythonの開発環境を用意しよう！**](https://prog-8.com/docs/python-env)

起動**コマンド**

```bash
python kabirunrun.py
```

## 注意

```bash
img = cv2.imread('/Users/tomixrm/Desktop/カビ　画像/iPad1.png')
```

この行のコードがカビの画像を参照するコードになります。

`/Users/tomixrm/Desktop/カビ　画像/iPad1.png`が画像のディレクトリになりますので、ここを編集してください。

# 乾燥

初めてOpenCVとPythonを使ってなんかするってことをしました。難しかったです。

[https://twitter.com/TomiXRM/status/1309869709920141313](https://twitter.com/TomiXRM/status/1309869709920141313)
