import math

import numpy as np

def simple_perceptron(x, bias=-0.5):
    '''
    単層パーセプトロン
    
    Parameters
    ----------
    x : list
        論理演算の入力値の組合せ
    bias : float
        ノードのバイアスの値
    
    Returns
    -------
    list
        論理演算の出力値(演算結果)
    '''
    # アークがもつ重み
    weights = np.array([0.5, 0.5]) if bias < 0 else np.array([-0.5, -0.5])
    
    # アークがもつ重みとバイアスを使って計算し、論理演算の出力値を返す
    y = np.array([1 if math.fsum(out * weights) + bias > 0 else 0 for out in x])
    
    return y

def three_layer_perceptron(x, bias=-0.6):
    '''
    3層パーセプトロン
    
    Parameters
    ----------
    x : list
        論理演算の入力値の組合せ
    bias : float
        ノードのバイアスの値
    
    Returns
    -------
    list
        論理演算の出力値(演算結果)
    '''
    # 中間ノードのアークが持つ重みの値
    weights_middle = np.array([[0.5, 0.5], [-0.5, -0.5]])
    
    # 中間ノードのバイアスの値
    bias_middle = np.array([-0.2, 0.7])
    
    # 中間ノードのアークが持つ重みとバイアスを使って計算し、論理演算の出力値を求める
    m = np.array([
        [1 if math.fsum(out * weights_middle[mid]) + bias_middle[mid] > 0 else 0 for mid in range(len(x[0]))]
        for out in x])
    
    # 中間層の結果を利用し、出力層の論理演算の値を求めて返す
    return simple_perceptron(m, bias)