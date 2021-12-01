import random
import numpy as np
np.set_printoptions(threshold=np.inf)#npによる大型行列を全て表示
from math import sqrt#平方根
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import networkx as nx
import statistics as sta
import os
pi=math.pi
color_list=['#6e69ee', '#367e21', '#9bd8f6', '#f10274', '#25c03f', '#d32898', '#e006ce', '#fcf6b2', '#b2a79c', '#06cc6f', '#e6573d', '#63cfea', '#1cae9b', '#95c001', '#d18308', '#7686f1', '#9bfe01', '#bbbc2f', '#02c9b7', '#d51293', '#8a2426', '#64a282', '#a3bd0a', '#0d0981', '#99352d', '#592913', '#81eb65', '#ca94af', '#07a4d1', '#59bfb0', '#55affc', '#907308', '#93b836', '#23a28e', '#dc248e', '#2dc68b', '#42c8d0', '#e464aa', '#445738', '#a92b78', '#f2b2a1', '#81209d', '#adaa0b', '#3d675b', '#6964f3', '#72f55d', '#85c215', '#398137', '#52009f', '#8f5f73', '#038e21', '#b11a5f', '#ce1477', '#07767b', '#93bdf2', '#91a221', '#39e768', '#5ebcad', '#9c84c4', '#68e23f', '#7b0e84', '#deced1', '#f98bed', '#0e7f79', '#f567fe', '#9d1f63', '#a7662a', '#72d38f', '#b692eb', '#c874a9', '#122913', '#fa331b', '#3ae2c3', '#3a9787', '#bbeca5', '#ec0297', '#dbb435', '#7540d4', '#0cea12', '#ef45e1', '#4cfe6a', '#b9ec1f', '#3603c3', '#8326a2', '#eb3871', '#36a4b2', '#04dcd9', '#b3e5ef', '#86c928', '#ca6f31', '#05ea7b', '#338056', '#389f4d', '#fe8856', '#30f295', '#5e8336', '#1f0344', '#e98ccc', '#90f0da', '#ec9290', '#dbc602', '#924af2', '#066597', '#78fed2', '#6692e4', '#0176ed', '#dc070c', '#6beb76', '#b1caf0', '#7755c2', '#2fc26e', '#53a9a0', '#266b54', '#76c4ce', '#505d21', '#f243df', '#d842ed', '#a79283', '#ba71b9', '#ccb7b0', '#3a6071', '#b2231f', '#482725', '#633d1b', '#bc192a', '#36315e', '#ccf213', '#3fc63c', '#73ebca', '#b1ac89', '#64be9a', '#9cf98a', '#e88353', '#7e9f24', '#8b16c2', '#3669ca', '#4af74c', '#7e249f', '#2522c8', '#a545c0', '#5e00b8', '#187cf5', '#c47f27', '#c9c70e', '#9e9071', '#45421a', '#04517d', '#fe4d5d', '#1319a6', '#df43e3', '#fefed0', '#f581d8', '#bdce7d', '#e2e6de', '#6d3017', '#d77e82', '#31988e', '#cd1e0e', '#fc7524', '#80360f', '#a623f4', '#82cd1c', '#4b71a2', '#bf3384', '#7fd628', '#e35d4e', '#6e6dfa', '#d014ae', '#39d97a', '#bd9562', '#e130ea', '#477ff6', '#07923a', '#3c82e1', '#dbf8e9', '#0ccd3d', '#177d59', '#ede3fe', '#b6d935', '#1ddd5a', '#774f5c', '#b9e46a', '#1d22ac', '#2718a0', '#a87fd9', '#043a51', '#e3e8d3', '#79e1e4', '#424128', '#d1d41e', '#ab6124', '#3f5fe7', '#1e6d85', '#fbd717', '#07bafc', '#73a614', '#3fa1b1', '#37513e', '#dd3cfb', '#6feb75', '#e1869e', '#e28589', '#42f7b5', '#479117', '#18d7af', '#df4eb6', '#228239', '#3f4b9b', '#a285a0', '#e38fa9', '#f26658', '#bab8a4', '#1c5922', '#e6ea82', '#636a9c', '#a0e25f', '#ac15f9', '#84d21f', '#30d51c', '#3043e7', '#707c62', '#4ca8c1', '#c13889', '#9c362a', '#8ac13e', '#b45815', '#4bdfc0', '#09c374', '#1b6195', '#b5f12d', '#2a4019', '#c937a2', '#5a4432', '#e63c10', '#655e16', '#fecc17', '#132a2b', '#7a59cc', '#bd2b16', '#61aa7d', '#0dcd94', '#05d4e9', '#db4bcc', '#68d3ff', '#c40a15', '#90fcfb', '#069877', '#3a6ff9', '#764118', '#d4270a', '#32b4b5', '#aa9dbf', '#18dc4b', '#a3f499', '#b2b4d0', '#126ef7', '#e2a39e', '#54dc20', '#8b1984', '#45c283', '#190895', '#267a43', '#9e4797', '#e15836', '#b38137', '#3fb1e7', '#2203e7', '#e1797b', '#ca8172', '#c2c26c', '#fb3625', '#29e829', '#35c940', '#23bfc4', '#f53db0', '#0340c9', '#b4b989', '#875a50', '#232aa9', '#302755', '#c88fab', '#937d52', '#667758', '#297684', '#c330f9', '#dd3fbf', '#cfbf4e', '#1b0176', '#83eec3', '#8e325a', '#7bbf44', '#8cd083', '#f182f4', '#4ccc10', '#a55a22', '#cd024b', '#a67928', '#c7cd05', '#2de6b9', '#183c93', '#1f7d79', '#8f4264', '#d20e64', '#5c297a', '#ff4c7f', '#a90909', '#e385b4', '#bb0f5a', '#509904', '#05f860', '#05e333', '#adc74c', '#28f311', '#ab035d', '#0bbf59', '#e77331', '#0f18a7', '#703c8e', '#296bc7', '#6a98bd', '#214096', '#7b95a3', '#6a11d5', '#7019d4', '#3dd1b4', '#cf0b06', '#f703a7', '#ec9750', '#fae540', '#8b4a35', '#7bf860', '#670096', '#f15e7b', '#aad1bc', '#95f3ef', '#9d3ff0', '#a19a80', '#d770b3', '#aa0646', '#878b8e', '#bff057', '#08317a', '#62b97c', '#8a105e', '#06fc09', '#2b060c', '#4b42c9', '#2c50ce', '#25a7f0', '#3ebd4d', '#b2f0a4', '#fb554a', '#9ab555', '#aba480', '#8a02c5', '#f14323', '#03c64f', '#a2b861', '#38f96c', '#c12641', '#0bf095', '#eebb67', '#482f47', '#6d28f5', '#1ab118', '#6cedec', '#553575', '#5846a0', '#2ef21d', '#a3af8a', '#3bb787', '#a3cc03', '#dc7d46', '#ea0338', '#61f99f', '#af304b', '#f4f750', '#31cf41', '#6870ca', '#ec7bb3', '#48531e', '#7520d7', '#4633fb', '#4067c3', '#f03d0a', '#993704', '#70a81b', '#02fca3', '#fca9e0', '#56b79a', '#a4404c', '#67f599', '#93ef80', '#35508a', '#05b5b2', '#9c35b3', '#7152c3', '#fedd77', '#5ff0fd', '#dbac4a', '#587fc4', '#f89037', '#0ba952', '#1d6648', '#dccfec', '#f0d3a1', '#9fcabd', '#97ce1c', '#a23ae0', '#52d122', '#0ab087', '#fcd05f', '#2edaa0', '#591d53', '#5af906', '#9b6988', '#1b9217', '#40718e', '#867da2', '#7069e9', '#197306', '#4b431c', '#5e7e37', '#3c0a39', '#ca946e', '#445a53', '#7cd04e', '#721d80', '#dba01a', '#6ce796', '#789cfd', '#84d548', '#f8b5a1', '#90e904', '#39e2e1', '#5fc94a', '#2792b1', '#a2ab4c', '#59489c', '#841e83', '#3b0e18', '#609567', '#329367', '#569fbb', '#b8e7e8', '#40dc31', '#8a58c3', '#f33128', '#3e9ec2', '#deed51', '#21de7a', '#2a61c3', '#014cdf', '#8e5ab9', '#61be8f', '#d53653', '#74f5e9', '#512fe2', '#62b5ae', '#c774f8', '#cfcc7d', '#b85479', '#5d6348', '#50a9fc', '#225e3d', '#6a3b64', '#9f60dc', '#5b684c', '#0df3dc', '#4ffa42', '#7189e4', '#675317', '#975caa', '#c574ec', '#24be7c', '#578906', '#4c6f9f', '#86e1e6', '#fcb139', '#14b47e', '#b34a0e', '#cb7025', '#3795ae', '#37f012', '#14416f', '#cbc589', '#448432', '#ed8787', '#196753', '#416f04', '#1f37c9', '#fbda25', '#7b6bcc', '#1ea2b8', '#c7b4b1', '#6f6719', '#b1befb', '#a7c960', '#f7a85c', '#a34f17','#6e69ee', '#367e21', '#9bd8f6', '#f10274', '#25c03f', '#d32898', '#e006ce', '#fcf6b2', '#b2a79c', '#06cc6f', '#e6573d', '#63cfea', '#1cae9b', '#95c001', '#d18308', '#7686f1', '#9bfe01', '#bbbc2f', '#02c9b7', '#d51293', '#8a2426', '#64a282', '#a3bd0a', '#0d0981', '#99352d', '#592913', '#81eb65', '#ca94af', '#07a4d1', '#59bfb0', '#55affc', '#907308', '#93b836', '#23a28e', '#dc248e', '#2dc68b', '#42c8d0', '#e464aa', '#445738', '#a92b78', '#f2b2a1', '#81209d', '#adaa0b', '#3d675b', '#6964f3', '#72f55d', '#85c215', '#398137', '#52009f', '#8f5f73', '#038e21', '#b11a5f', '#ce1477', '#07767b', '#93bdf2', '#91a221', '#39e768', '#5ebcad', '#9c84c4', '#68e23f', '#7b0e84', '#deced1', '#f98bed', '#0e7f79', '#f567fe', '#9d1f63', '#a7662a', '#72d38f', '#b692eb', '#c874a9', '#122913', '#fa331b', '#3ae2c3', '#3a9787', '#bbeca5', '#ec0297', '#dbb435', '#7540d4', '#0cea12', '#ef45e1', '#4cfe6a', '#b9ec1f', '#3603c3', '#8326a2', '#eb3871', '#36a4b2', '#04dcd9', '#b3e5ef', '#86c928', '#ca6f31', '#05ea7b', '#338056', '#389f4d', '#fe8856', '#30f295', '#5e8336', '#1f0344', '#e98ccc', '#90f0da', '#ec9290', '#dbc602', '#924af2', '#066597', '#78fed2', '#6692e4', '#0176ed', '#dc070c', '#6beb76', '#b1caf0', '#7755c2', '#2fc26e', '#53a9a0', '#266b54', '#76c4ce', '#505d21', '#f243df', '#d842ed', '#a79283', '#ba71b9', '#ccb7b0', '#3a6071', '#b2231f', '#482725', '#633d1b', '#bc192a', '#36315e', '#ccf213', '#3fc63c', '#73ebca', '#b1ac89', '#64be9a', '#9cf98a', '#e88353', '#7e9f24', '#8b16c2', '#3669ca', '#4af74c', '#7e249f', '#2522c8', '#a545c0', '#5e00b8', '#187cf5', '#c47f27', '#c9c70e', '#9e9071', '#45421a', '#04517d', '#fe4d5d', '#1319a6', '#df43e3', '#fefed0', '#f581d8', '#bdce7d', '#e2e6de', '#6d3017', '#d77e82', '#31988e', '#cd1e0e', '#fc7524', '#80360f', '#a623f4', '#82cd1c', '#4b71a2', '#bf3384', '#7fd628', '#e35d4e', '#6e6dfa', '#d014ae', '#39d97a', '#bd9562', '#e130ea', '#477ff6', '#07923a', '#3c82e1', '#dbf8e9', '#0ccd3d', '#177d59', '#ede3fe', '#b6d935', '#1ddd5a', '#774f5c', '#b9e46a', '#1d22ac', '#2718a0', '#a87fd9', '#043a51', '#e3e8d3', '#79e1e4', '#424128', '#d1d41e', '#ab6124', '#3f5fe7', '#1e6d85', '#fbd717', '#07bafc', '#73a614', '#3fa1b1', '#37513e', '#dd3cfb', '#6feb75', '#e1869e', '#e28589', '#42f7b5', '#479117', '#18d7af', '#df4eb6', '#228239', '#3f4b9b', '#a285a0', '#e38fa9', '#f26658', '#bab8a4', '#1c5922', '#e6ea82', '#636a9c', '#a0e25f', '#ac15f9', '#84d21f', '#30d51c', '#3043e7', '#707c62', '#4ca8c1', '#c13889', '#9c362a', '#8ac13e', '#b45815', '#4bdfc0', '#09c374', '#1b6195', '#b5f12d', '#2a4019', '#c937a2', '#5a4432', '#e63c10', '#655e16', '#fecc17', '#132a2b', '#7a59cc', '#bd2b16', '#61aa7d', '#0dcd94', '#05d4e9', '#db4bcc', '#68d3ff', '#c40a15', '#90fcfb', '#069877', '#3a6ff9', '#764118', '#d4270a', '#32b4b5', '#aa9dbf', '#18dc4b', '#a3f499', '#b2b4d0', '#126ef7', '#e2a39e', '#54dc20', '#8b1984', '#45c283', '#190895', '#267a43', '#9e4797', '#e15836', '#b38137', '#3fb1e7', '#2203e7', '#e1797b', '#ca8172', '#c2c26c', '#fb3625', '#29e829', '#35c940', '#23bfc4', '#f53db0', '#0340c9', '#b4b989', '#875a50', '#232aa9', '#302755', '#c88fab', '#937d52', '#667758', '#297684', '#c330f9', '#dd3fbf', '#cfbf4e', '#1b0176', '#83eec3', '#8e325a', '#7bbf44', '#8cd083', '#f182f4', '#4ccc10', '#a55a22', '#cd024b', '#a67928', '#c7cd05', '#2de6b9', '#183c93', '#1f7d79', '#8f4264', '#d20e64', '#5c297a', '#ff4c7f', '#a90909', '#e385b4', '#bb0f5a', '#509904', '#05f860', '#05e333', '#adc74c', '#28f311', '#ab035d', '#0bbf59', '#e77331', '#0f18a7', '#703c8e', '#296bc7', '#6a98bd', '#214096', '#7b95a3', '#6a11d5', '#7019d4', '#3dd1b4', '#cf0b06', '#f703a7', '#ec9750', '#fae540', '#8b4a35', '#7bf860', '#670096', '#f15e7b', '#aad1bc', '#95f3ef', '#9d3ff0', '#a19a80', '#d770b3', '#aa0646', '#878b8e', '#bff057', '#08317a', '#62b97c', '#8a105e', '#06fc09', '#2b060c', '#4b42c9', '#2c50ce', '#25a7f0', '#3ebd4d', '#b2f0a4', '#fb554a', '#9ab555', '#aba480', '#8a02c5', '#f14323', '#03c64f', '#a2b861', '#38f96c', '#c12641', '#0bf095', '#eebb67', '#482f47', '#6d28f5', '#1ab118', '#6cedec', '#553575', '#5846a0', '#2ef21d', '#a3af8a', '#3bb787', '#a3cc03', '#dc7d46', '#ea0338', '#61f99f', '#af304b', '#f4f750', '#31cf41', '#6870ca', '#ec7bb3', '#48531e', '#7520d7', '#4633fb', '#4067c3', '#f03d0a', '#993704', '#70a81b', '#02fca3', '#fca9e0', '#56b79a', '#a4404c', '#67f599', '#93ef80', '#35508a', '#05b5b2', '#9c35b3', '#7152c3', '#fedd77', '#5ff0fd', '#dbac4a', '#587fc4', '#f89037', '#0ba952', '#1d6648', '#dccfec', '#f0d3a1', '#9fcabd', '#97ce1c', '#a23ae0', '#52d122', '#0ab087', '#fcd05f', '#2edaa0', '#591d53', '#5af906', '#9b6988', '#1b9217', '#40718e', '#867da2', '#7069e9', '#197306', '#4b431c', '#5e7e37', '#3c0a39', '#ca946e', '#445a53', '#7cd04e', '#721d80', '#dba01a', '#6ce796', '#789cfd', '#84d548', '#f8b5a1', '#90e904', '#39e2e1', '#5fc94a', '#2792b1', '#a2ab4c', '#59489c', '#841e83', '#3b0e18', '#609567', '#329367', '#569fbb', '#b8e7e8', '#40dc31', '#8a58c3', '#f33128', '#3e9ec2', '#deed51', '#21de7a', '#2a61c3', '#014cdf', '#8e5ab9', '#61be8f', '#d53653', '#74f5e9', '#512fe2', '#62b5ae', '#c774f8', '#cfcc7d', '#b85479', '#5d6348', '#50a9fc', '#225e3d', '#6a3b64', '#9f60dc', '#5b684c', '#0df3dc', '#4ffa42', '#7189e4', '#675317', '#975caa', '#c574ec', '#24be7c', '#578906', '#4c6f9f', '#86e1e6', '#fcb139', '#14b47e', '#b34a0e', '#cb7025', '#3795ae', '#37f012', '#14416f', '#cbc589', '#448432', '#ed8787', '#196753', '#416f04', '#1f37c9', '#fbda25', '#7b6bcc', '#1ea2b8', '#c7b4b1', '#6f6719', '#b1befb', '#a7c960', '#f7a85c', '#a34f17']

#-----------------------------変数定義---------------------------------------

t=100 #時間
n=500 #ノード数
l=0.07 #通信可能距離
c=5 #cに近い固有値に属する固有ベクトルに収束させる正の定数
dmax=7 #最大同時接続可能数
b=2/(2*dmax-c)**2 #状態量の受け渡しの量を決める正の定数
v_min=0.002 #歩行速度最小値
v_max=0.014 #歩行速度最大値
sd=4 #乱数の種



#初期状態量分布
q=np.random.seed(sd-3)
q=np.random.rand(n)
q=list(q)



#-----------------------------関数定義-------------------------------------

def initial_position (sd): #初期ノード配置
    x=np.random.seed(sd*31)
    x=np.random.rand(n)#0から1の乱数をノード数だけ発生．
    y=np.random.seed(sd*37)
    y=np.random.rand(n)
    x=list(x)
    y=list(y)
    return x,y

def randomwalk_model (time,sd): #ランダムウォークモデル (時間，乱数) 隣接行列を出力

    #初期化
    gap=[0 for i in range(n)]
    radians=[0 for i in range(n)]
    next_x=[0 for i in range(n)]
    next_y=[0 for i in range(n)]
    link=[[0 for i in range(n)]for j in range(n)] #リンクの有無
    degree=[0 for i in range(n)] #次数
    

    for i in range(n):

        np.random.seed(i*i*7+time*time*11+sd*sd*13) #各ノードの方向が一致しないよう，タネを複雑に．
        radians[i]=2*np.pi*np.random.random() #移動角度の決定
        gap[i]=np.random.uniform(v_min,v_max) #移動距離の決定
        next_x[i]=x[i]+gap[i]*math.cos(radians[i]) #x座標計算
        next_y[i]=y[i]+gap[i]*math.sin(radians[i]) #y座標計算

        #境界での跳ね返りを考慮してx座標を更新
        if(0<=next_x[i]<=1):
            x[i]=next_x[i]
        elif(next_x[i]<0):
            x[i]=-next_x[i]
        elif(1<next_x[i]):
            x[i]=1-(next_x[i]-1)
        
        #境界での跳ね返りを考慮してy座標を更新
        if(0<=next_y[i]<=1):
            y[i]=next_y[i]
        elif(next_y[i]<0):
            y[i]=-next_y[i]
        elif(1<next_y[i]):
            y[i]=1-(next_y[i]-1)

    #リンク生成   
    for i in range(n):
        for j in range(n):
            if i>j and degree[i]<dmax and degree[j]<dmax :
                dis=(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])
                if sqrt(dis)<l :#unit disk graph 最大次数を超えない処理
                    link[i][j]=1
                    link[j][i]=1
                    degree[i]+=1
                    degree[j]+=1

    return link #隣接行列

def static_environment_model(sd): #静的環境下のネットワークモデル

    link=[[0 for i in range(n)]for j in range(n)] #リンクの有無
    degree=[0 for i in range(n)] #次数
    for i in range(n):
        for j in range(n):
            if i>j and degree[i]<dmax and degree[j]<dmax :
                dis=(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])
                if sqrt(dis)<l :#unit disk graph 最大次数を超えない処理
                    link[i][j]=1
                    link[j][i]=1
                    degree[i]+=1
                    degree[j]+=1

    return link #隣接行列

def laplacian(link): #ラプラシアン行列 (隣接行列) NW構造の描写も可能   

    #グラフ作成
    graph=nx.Graph()
    for i in range(n):
        graph.add_node(i)
        for j in range(n):
            if i>j and link[i][j]==1:
                graph.add_edge(i,j)

    A = nx.to_numpy_array(graph) #隣接行列
    D = np.diag(np.sum(A,axis=1))  #次数行列
    L = D-A  #ラプラシアン行列

    w_L, v_L =np.linalg.eig(L) 
    idx = np.argsort(w_L)
    val_L = w_L[idx]  #固有値
    vec_L = v_L[:,idx].T  #固有ベクトル転置

    '''
    #グラフの概形出力
    nx.draw_networkx(graph)
    plt.show()
    '''

    return L

def adsc(link,q): #自律分散スペクトルクラスタリングに基づく状態ベクトル更新 (隣接行列，状態ベクトル)

    #初期化
    q_odd=[0 for i in range(n)]
    q_even=[0 for i in range(n)]

    #奇数ステップ
    for i in range(n):
        sigma1=0
        for j in range(n):
            if link[i][j]!=0:
                sigma1+=q[i]-q[j]
        q_odd[i]=q[i]+sigma1  

    #偶数ステップ
    for i in range (n):
        sigma1=0
        sigma2=0
        for j in range(n):
            if link[i][j]!=0:
                sigma1+=q[i]-q[j]
                sigma2+=q_odd[i]-q_odd[j]
        q_even[i]=(1-b*c**2)*q[i]-b*sigma2+b*(1+2*c)*sigma1 
    q=q_even

    return q

def clustering(link,q): #クラスタ判定(隣接行列，状態ベクトル)　ノードの所属するクラスタ番号を1次元ベクトルで出力(クラスタナンバー)

    cluster_number=[0 for i in range(n)]
    max_grade=[-1 for i in range(n)]#自分と一番差があるノード番号 #自分の場合は-1のまま
    for i in range(n):
        MAX=0.0
        for j in range(n):
            if link[i][j]==1:
                if q[j]-q[i]>=MAX:#相手ー自分の値をより大きいものに更新し続ける．→自分が最も大きい場合，負の値となり、MAXは更新されない。
                    MAX=q[j]-q[i]#あるiにおける，最終的なMAXの値を下のfor文で適用している．
        for j in range(n):
            if link[i][j]==1:
                if q[j]-q[i]==MAX:#jと最も差があるのはi
                    max_grade[i]=j#ノードiともっとも差があるノードはノードj#ここまでで，隣接ノードとの状態量の差を把握している．

    for i in range(n):
        grade1=0
        for j in range(50):#grade1=grade2の時の処理のために,jで回す必要がある．N=500は大きすぎる
            if j==0:#自分がCHの時の処理#j=0なのは，j=0が回し終わった時点で，自分自身がCHと判別でき，それ以降のjで回す必要がないから
                grade1=max_grade[i]#max_grade[i]は，ノードiと一番差があるノード番号
                if grade1==-1:#自分がCHの時の処理　#自分と一番差があるノード番号が-1→自分がクラスタヘッドということが分かる．
                    cluster_number[i]=i#ノードiが所属するクラスタのCH
                    break
            grade2=max_grade[grade1]#grade2は，あるiにとって一番差があるノードgrade1,にとってさらに一番差があるノード(iから2ホップ先)．この行の一番最後のgrade1=grade2が適用される
            if grade2==-1:       #自分（ノードi）の隣がCH←隣から探し始めたら、自分がCH←grade2==-1より
                cluster_number[i]=grade1#grade1=max_grade[i]#max_grade[i]は，ノードiと一番差があるノード番号(1ホップ先)
                break
            if max_grade[grade2]==-1:#自分の２個となりcH
                cluster_number[i]=grade2
                break
            if grade2==max_grade[max_grade[grade2]]: #grade2と同じ値のCHの時#2ホップ先と3ホップ先の状態量が同じ場合の処理
                if grade2>max_grade[grade2]:#ノード番号が大きい方をクラスタヘッドに
                    cluster_number[i]=grade2
                    break
                if max_grade[grade2]>grade2:
                    cluster_number[i]=max_grade[grade2]
                    break
            grade1=grade2#どのif分にも引っかからない場合は，grade1をgrade2変換→jで回すことによりNホップ先まで判定可能に．
            #クラスタ数をカウント

    return cluster_number
    
def cluster_counter(cluster_number): #クラスタ数出力（時刻，クラスタナンバー）
    cluster_counter=0
    
    for i in range(n):
        if cluster_number[i]==i:
            cluster_counter+=1

    return cluster_counter
    
def cluster_plot(cluster_number): #クラスタリングをプロット(クラスタナンバー) 
    for i in range(n):
        if cluster_number[i]!=i:#CH以外
            plt.plot(x[i],y[i],color=color_list[cluster_number[i]],marker='o')
        if cluster_number[i]==i:#CH
            plt.plot(x[i],y[i],color=color_list[cluster_number[i]],marker='*',markersize=20)     

    plt.xlabel('x-coordinate',fontsize=16)
    plt.ylabel('y-coordinate',fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    
    return plt.plot()
    
    #plt.show()
    #fig.savefig('d16clu.pdf')

def evaluation(horizon,xlabel,vertex,ylabel): #評価実験プロット（横軸，ラベル，縦軸，ラベル）
    
    plt.xlabel(xlabel,fontsize=16)
    plt.ylabel(ylabel,fontsize=16)
    plt.plot(horizon, vertex)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show() 
    

#-----------------------------シミュレーション--------------------------------

time_list=[]
fig,ax=plt.subplots()

#初期ノード位置
x,y=initial_position(sd)
#初期状態量分布
q=np.random.seed(sd*41)
q=np.random.rand(n)

link=static_environment_model(sd)


for k in range (100):
    time_list.append(k)
    q=adsc(link,q)
    cluster_number=clustering(link,q)

cluster_plot(cluster_number)
    
plt.show()





         
   
