import math
import numpy as np

class Perceptron:
    def simple_perceptron(x, bias=-0.5):
        '''
        単純パーセプトロン
        :param 論理演算の入力値の組合せ
        :param ノードのバイアスの値
        :return 論理演算の出力値(演算結果)
        '''
        # アークがもつ重み
        w = np.array([0.5, 0.5]) if bias < 0 else np.array([-0.5, -0.5])
        
        # アークがもつ重みとバイアスを使って計算し、論理演算の出力値を返す
        y = np.array([
            1 if math.fsum(x[out] * w) + bias > 0 else 0
            for out in range(x.shape[0])
        ])
        return y
    
    def three_layer_perceptron(x, bias=-0.6):
        '''
        3層パーセプトロン
        :param 論理演算の入力値の組合せ
        :param ノードのバイアスの値
        :return 論理演算の出力値(演算結果)
        '''
        # 中間ノードのアークが持つ重みの値
        wm = np.array([[0.5, 0.5], [-0.5, -0.5]])
        
        # 中間ノードのバイアスの値
        bm = np.array([-0.2, 0.7])
        
        # 中間ノードのアークが持つ重みとバイアスを使って計算し、論理演算の出力値を求める
        m = np.array([
            [
                1 if math.fsum(x[out] * wm[mid]) + bm[mid] > 0 else 0
                for mid in range(x.shape[1])
            ]
            for out in range(x.shape[0])
        ])
        
        # 中間層の結果を利用し、出力層の論理演算の値を求めて返す
        return Perceptron.simple_perceptron(m, bias)
