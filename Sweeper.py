import pyautogui
from PIL import Image
import random

source="C:\\Users\\muhri\\OneDrive\\Desktop\\Sweeper\\images\\"

#Find the board
def board_generator():
    global board_im
    board_im=Image.open(source+"board.png")
    board=pyautogui.locateAllOnScreen(board_im)

    board=list(board)

    x0=board[0][0]
    y0=board[0][1]

    global edges
    edges=[x0,x0+600,y0,y0+320]

    #Create the tiles list
    gen_board=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(0,16):
        for j in range(0,30):
            temp=[x0+j*20,y0+i*20, ""]
            gen_board[i].append(temp)
    return(gen_board)

#Check if on edge
#Left, Right, Up, Down
def edge_check(tile):
    x=[0,0,0,0]
    if tile[0]>edges[0]:
        x[0]=1
    if tile[0]<edges[1]-20:
        x[1]=1
    if tile[1]>edges[2]:
        x[2]=1
    if tile[1]<edges[3]-20:
        x[3]=1
    y=[[-x[0]*x[2],-x[0]*x[2]],   [0,-x[2]],   [x[1]*x[2], -x[1]*x[2]],
       [-x[0],0],                              [x[1],0],
       [-x[0]*x[3],x[0]*x[3]],    [0,x[3]],    [x[1]*x[3],x[1]*x[3]]]
    return(y)


def click(x,y):
    pyautogui.doubleClick(gen_board[y][x][0],gen_board[y][x][1])
    check(x,y)


def check(x,y):
    to_check = [(x,y)]
    for k in to_check:
        check_nums = []
        print(len(to_check))
        for i in range(0, len(nums)):
            check_num=list(pyautogui.locateAllOnScreen(nums[i], region=(gen_board[k[1]][k[0]][0], gen_board[k[1]][k[0]][1], 20, 20)))
            if check_num!=[]:
                gen_board[k[1]][k[0]][2] = i
                num_list.append((k[0],k[1]))
        if gen_board[k[1]][k[0]][2] == "":
            gen_board[k[1]][k[0]][2] = 8
        if gen_board[k[1]][k[0]][2] == 0:
            edge_truth = edge_check(gen_board[k[1]][k[0]])
            for l in edge_truth:
                if (k[0] + l[0],k[1] + l[1]) not in to_check and gen_board[k[1] + l[1]][k[0] + l[0]][2]=="":
                    to_check.append((k[0] + l[0],k[1] + l[1]))


def image_gen():
    _1_im = Image.open(source+"1.png")
    _2_im = Image.open(source+"2.png")
    _3_im = Image.open(source+"3.png")
    _4_im = Image.open(source+"4.png")
    _5_im = Image.open(source+"5.png")
    _6_im = Image.open(source+"6.png")
    _7_im = Image.open(source+"7.png")
    #_8_im = Image.open(source+"8.png")
    _0_im = Image.open(source+"0.png")

    global nums
    nums=[_0_im,_1_im,_2_im,_3_im,_4_im,_5_im,_6_im,_7_im]

    global win_im
    win_im=Image.open(source+"Win.png")

    global lose_im
    lose_im=Image.open(source+"frown.png")

    global smile_im
    smile_im=Image.open(source+"smile.png")



#If bombs are around, check the other tiles
def sat_check(x,y):
    bombs=0
    edge_truth = edge_check(gen_board[y][x])
    temp=list()
    for i in edge_truth:
        if gen_board[y+i[1]][x+i[0]][2]==-1:
            bombs+=1
        else:
            temp.append((x+i[0],y+i[1]))
    if gen_board[y][x][2]==bombs:
        for p in range(len(temp)):
            if gen_board[temp[p][1]][temp[p][0]][2]=="":
                click(temp[p][0],temp[p][1])


#Find bombs around a tile
def bomb_check(x,y):
    edge_truth = edge_check(gen_board[y][x])
    nms=0
    temp=list()
    for i in edge_truth:
        if sint(gen_board[y+i[1]][x+i[0]][2])>=0:
            nms+=1
        else:
            temp.append((x+i[0],y+i[1]))
    if gen_board[y][x][2]==8-nms:
        for z in range(len(temp)):
            gen_board[temp[z][1]][temp[z][0]][2]=-1

#How to group unknown spaces together
def pair_check(x,y):
    edge_truth = edge_check(gen_board[y][x])
    bombs = 0
    nms=0
    temp = list()
    edge_xy=[]
    for i in edge_truth:
        if gen_board[y+i[1]][x+i[0]][2]==-1:
            bombs+=1
        elif gen_board[y+i[1]][x+i[0]][2]!="":
            edge_xy.append((x + i[0], y + i[1]))
            nms+=1
        elif gen_board[y+i[1]][x+i[0]][2]=="":
            temp.append((x + i[0], y + i[1]))
    if gen_board[y][x][2]==7-nms and len(temp)==2:
        for j in edge_xy:
            edge_truth2 = edge_check(gen_board[j[1]][j[0]])
            bmbs=0
            temp2=[]
            for k in edge_truth2:
                if gen_board[j[1] + k[1]][j[0] + k[0]][2] == -1:
                    bmbs += 1
                if gen_board[j[1] + k[1]][j[0] + k[0]][2] =="":
                    if (j[0] + k[0],j[1] + k[1]) in temp:
                        bmbs+=0.5
                    else:
                        temp2.append((j[0] + k[0], j[1] + k[1]))
                if gen_board[j[1]][j[0]][2]==bmbs:
                    for l in temp2:
                        if gen_board[l[1]][l[0]][2]=="":
                            click(l[0],l[1])
                elif gen_board[j[1]][j[0]][2]==bmbs-len(temp2):
                    for a in temp2:
                        gen_board[a[1]][a[0]][2]=-1



#define sint
def sint(x):
    if x=="":
        return(-1)
    else:
        return(x)


#How to guess
def guess():
    gs=True
    while gs==True:
        randy = random.randint(0, 15)
        randx=random.randint(0,29)
        if gen_board[randy][randx][2]=="":
            click(randx,randy)
            gs=False


global gen_board
gen_board=board_generator()
image_gen()

global num_list
num_list=[]

smile_find=pyautogui.locateOnScreen(smile_im)
guess()
fin=False
while fin==False:
    same=False
    while same==False:
        chek_total=len(num_list)
        for zzz in num_list:
            bomb_check(zzz[0], zzz[1])
        for zzz in num_list:
            sat_check(zzz[0], zzz[1])
        for zzz in num_list:
            pair_check(zzz[0], zzz[1])
        print(chek_total, len(num_list))
        if chek_total==len(num_list):
            same=True
    print("guess")
    guess()
    if pyautogui.locateOnScreen(win_im, region=smile_find) != None:
        fin = True
        print("You Win!")
    if pyautogui.locateOnScreen(lose_im, region=smile_find) != None:
        fin = True
        print("You Lose!")