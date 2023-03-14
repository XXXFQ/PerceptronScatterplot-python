import random
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
from perceptron import Perceptron as pla
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Perceptron Scatterplot v1.0')
        
        # 通常のフレームを配置
        self.frame = tk.Frame(self.master)
        self.frame.pack(side = tk.RIGHT)
        
        # グラフフレームの作成
        self.createGraphFrame()
        
        # パーセプトロンの種類を選択するラジオボタン作成
        self.createPerceptronTypeRadio()
        
        # バイアス値入力テキストボックス作成
        self.createBiasInputBox()
        
        # データ数入力テキストボックス作成
        self.createDataCountInputBox()
    
    def createGraphFrame(self):
        # matplotlib配置用フレーム
        qraphFrame = ttk.Frame(self.master)
        
        # matplotlibの描画領域の作成
        fig = Figure()
        
        # 座標軸の作成
        self.ax = fig.add_subplot(1, 1, 1)
        
        # matplotlibの描画領域とウィジェット(Frame)の関連付け
        self.fig_canvas = FigureCanvasTkAgg(fig, qraphFrame)
        
        # matplotlibのツールバーを作成
        self.toolbar = NavigationToolbar2Tk(self.fig_canvas, qraphFrame)
        
        # matplotlibのグラフをフレームに配置
        self.fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # フレームをウィンドウに配置
        qraphFrame.pack(side = tk.LEFT)
        
        # ボタンの作成
        self.s_PerceptronButton = ttk.Button(
            self.frame,
            text = "散布図を描写",
            command = self.perceptronButton_click
        )
        
        # 散布図描写ボタンの配置
        self.s_PerceptronButton.pack(side = tk.TOP, pady = 4)
    
    def createPerceptronTypeRadio(self):
        '''
        パーセプトロンの種類を選択するラジオボタン作成
        '''
        # ラベルフレームの作成
        labelFrame = ttk.LabelFrame(self.frame, text="パーセプトロンの種類")
        
        # ラジオボタンの値
        self.pla_TypeRadioVar = tk.IntVar(value = 0)
        
        # ラジオボタン作成
        radioText = ["単純パーセプトロン", "3層パーセプトロン(MLP)"]
        for i in range(len(radioText)):
            self.perceptronRadio = ttk.Radiobutton(
                labelFrame,
                value = i,
                text = radioText[i],
                variable = self.pla_TypeRadioVar
            )
            self.perceptronRadio.pack(side=tk.TOP, anchor=tk.W)
        
        # 配置
        labelFrame.pack(side=tk.RIGHT, padx=30, pady=10, anchor=tk.NE)
    
    def createBiasInputBox(self):
        '''
        バイアス値入力テキストボックス作成
        '''
        # バイアス値入力ボックスのラベル
        Label = ttk.Label(
            self.frame,
            width = 8,
            text = "バイアス",
            justify = tk.CENTER
        )
        
        # バイアス値入力ボックス
        self.biasInputBox = ttk.Entry(
            self.frame,
            width = 10,
            justify = tk.CENTER
        )
        
        # 初期値設定
        self.biasInputBox.insert(tk.END, '-0.5')
        
        # 配置
        Label.pack(anchor = tk.NW)
        self.biasInputBox.pack(anchor = tk.NW)
    
    def createDataCountInputBox(self):
        '''
        データ数入力テキストボックス作成
        '''
        # データ数入力ボックスのラベル
        Label = ttk.Label(
            self.frame,
            width = 10,
            text = "データ個数",
            justify = tk.CENTER
        )
        
        # データ数入力ボックス
        self.dataCountInputBox = ttk.Entry(
            self.frame,
            width = 10,
            justify = tk.CENTER
        )
        
        # 初期値設定
        self.dataCountInputBox.insert(tk.END, '500')
        
        # 配置
        Label.pack(anchor = tk.NW)
        self.dataCountInputBox.pack(anchor = tk.NW)
    
    def perceptronButton_click(self):
        '''
        パーセプトロンの散布図を描写する
        '''
        try:
            # バイアス値を取得
            BIAS = float(self.biasInputBox.get())
            
            # テストデータを生成
            x = np.array([
                [random.random(), random.random()]
                for i in range(int(self.dataCountInputBox.get()))
            ])
            
            # パーセプトロンの散布図を描写
            mode = self.pla_TypeRadioVar.get()
            if mode == 0:
                y = pla.simplePerceptron(x, BIAS)
            elif mode == 1:
                y = pla.threeLayerPerceptron(x, BIAS)
            
            # 散布図を表示
            self.ax.clear()
            self.ax.scatter(
                x[:, 0], x[:, 1],
                color = ["Yellow" if out == 0 else "Magenta" for out in y],
                marker = "o",
                s = 30
            )
            self.fig_canvas.draw()
        except (ValueError):
            messagebox.showerror("エラー!", "数値を入力して下さい。")

if __name__=='__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()