import random
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from .perceptron import Perceptron

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Perceptron Scatterplot v1.0')
        
        # 通常のフレームを配置
        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.RIGHT)
        
        # グラフフレームの作成
        self.create_graph_frame()
        
        # パーセプトロンの種類を選択するラジオボタン作成
        self.create_perceptron_type_radio()
        
        # バイアス値入力テキストボックス作成
        self.create_bias_input_box()
        
        # データ数入力テキストボックス作成
        self.create_datacount_input_box()
    
    def create_graph_frame(self):
        # matplotlib配置用フレーム
        qraph_frame = ttk.Frame(self.master)
        
        # matplotlibの描画領域の作成
        fig = Figure()
        
        # 座標軸の作成
        self.ax = fig.add_subplot(1, 1, 1)
        
        # matplotlibの描画領域とウィジェット(Frame)の関連付け
        self.fig_canvas = FigureCanvasTkAgg(fig, qraph_frame)
        
        # matplotlibのツールバーを作成
        self.toolbar = NavigationToolbar2Tk(self.fig_canvas, qraph_frame)
        
        # matplotlibのグラフをフレームに配置
        self.fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # フレームをウィンドウに配置
        qraph_frame.pack(side=tk.LEFT)
        
        # ボタンの作成
        self.s_perceptron_button = ttk.Button(
            self.frame,
            text="散布図を描写",
            command=self.perceptronButton_click
        )
        
        # 散布図描写ボタンの配置
        self.s_perceptron_button.pack(side=tk.TOP, pady=4)
    
    def create_perceptron_type_radio(self):
        '''
        パーセプトロンの種類を選択するラジオボタン作成
        '''
        # ラベルフレームの作成
        label_frame = ttk.LabelFrame(self.frame, text="パーセプトロンの種類")
        
        # ラジオボタンの値
        self.pla_type_radio_var = tk.IntVar(value=0)
        
        # ラジオボタン作成
        radio_texts = ["単純パーセプトロン", "3層パーセプトロン(MLP)"]
        for i, radio_text in enumerate(radio_texts):
            self.perceptron_radio = ttk.Radiobutton(
                label_frame,
                value=i,
                text=radio_text,
                variable=self.pla_type_radio_var)
            self.perceptron_radio.pack(side=tk.TOP, anchor=tk.W)
        
        # 配置
        label_frame.pack(side=tk.RIGHT, padx=30, pady=10, anchor=tk.NE)
    
    def create_bias_input_box(self):
        '''
        バイアス値入力テキストボックス作成
        '''
        # バイアス値入力ボックスのラベル
        label = ttk.Label(
            self.frame,
            width=8,
            text="バイアス",
            justify=tk.CENTER
        )
        
        # バイアス値入力ボックス
        self.bias_input_box = ttk.Entry(
            self.frame,
            width=10,
            justify=tk.CENTER
        )
        
        # 初期値設定
        self.bias_input_box.insert(tk.END, '-0.5')
        
        # 配置
        label.pack(anchor=tk.NW)
        self.bias_input_box.pack(anchor=tk.NW)
    
    def create_datacount_input_box(self):
        '''
        データ数入力テキストボックス作成
        '''
        # データ数入力ボックスのラベル
        label = ttk.Label(
            self.frame,
            width=10,
            text="データ個数",
            justify=tk.CENTER
        )
        
        # データ数入力ボックス
        self.datacount_input_box = ttk.Entry(
            self.frame,
            width=10,
            justify=tk.CENTER
        )
        
        # 初期値設定
        self.datacount_input_box.insert(tk.END, '500')
        
        # 配置
        label.pack(anchor=tk.NW)
        self.datacount_input_box.pack(anchor=tk.NW)
    
    def perceptronButton_click(self):
        '''
        パーセプトロンの散布図を描写する
        '''
        try:
            # バイアス値を取得
            BIAS = float(self.bias_input_box.get())
            
            # テストデータを生成
            x = np.array([
                [random.random(), random.random()]
                for _ in range(int(self.datacount_input_box.get()))
            ])
            
            # パーセプトロンの散布図を描写
            if (mode := self.pla_type_radio_var.get()) == 0:
                y = Perceptron.simple_perceptron(x, BIAS)
            elif mode == 1:
                y = Perceptron.three_layer_perceptron(x, BIAS)
            
            # 散布図を表示
            self.ax.clear()
            self.ax.scatter(
                x[:, 0], x[:, 1],
                color=["Yellow" if out == 0 else "Magenta" for out in y],
                marker="o",
                s=30
            )
            self.fig_canvas.draw()
        except (ValueError):
            messagebox.showerror("エラー!", "数値を入力して下さい。")