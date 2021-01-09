import requests
import lxml.html as html
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import logging
import json

baseUrl = "https://www.animalgame.com"
targetUrl = "https://www.animalgame.com/play/"
QUESTION_XPATH = "//tbody/tr/td/font[@size='+3']/text()"
# $x("//tbody/tr/td/font[@size='+3']")[0].innerText
# $x("//tbody/tr/td/form") //  confirmation  question - last question 
listNodes = []
fatherNodeSaved = {}


def getNodes2(urlNode):
  try:
    digitsFromNode= re.findall(r'\d+', urlNode)
    idNode = "root"
    if len(digitsFromNode) > 0 :
        idNode = digitsFromNode[0]

    response = requests.get(urlNode)
    s = BeautifulSoup(response.text, 'lxml')
    question = s.find('font', attrs={'size':'+3'}).get_text()
    questionClean = question.replace("\n", "")
    questionClean = " ".join(questionClean.split())
    question = s.find_all('form')
    questionY = question[0].get('action')
    questionN = question[1].get('action')

    digitsFromN= re.findall(r'\d+', questionN)
    idN = digitsFromN[0]
    digitsFromY = re.findall(r'\d+', questionY)
    idY = digitsFromY[0]
    # print(questionY)
    urlY = baseUrl + questionY
    urlN = baseUrl + questionN
    # /play/index.php?id=1206'
    # /play/index.php?id=62224&action=right'
    
    node = {
        "question":questionClean,
        "id":idNode,
        "urlY":urlY,
        "urlN":urlN,
        "animal":"",
        "pattern":[]
    }
    if "action=wrong" in urlN:
       node["animal"] = "Y"
    # print(node)
    return node
  except:
    print("Something went wrong")

    


def getNodesLvlOrder():
    result = []
    Q = []  
    if True != False :
        Q.append(getNodes2(targetUrl))
        while len(Q) > 0 :
            #   let node = Q.shift()
              node = Q.pop(0)
              result.append(node)
              # print(node)
       
              if node["urlN"] and "action=wrong" not in node["urlN"]:
                  nodeN = getNodes2(node["urlN"])
                  if nodeN:
                    addFromFatherNodeN = node["pattern"].copy()
                    addFromFatherNodeN.append(0)
                    nodeN["pattern"] = addFromFatherNodeN
                    # print(nodeN,"nodeN")
                    Q.append(nodeN)
                  else:
                    print("None is not True...:nodeN")
              if node["urlY"] and "action=right" not in node["urlY"]:
                  nodeY = getNodes2(node["urlY"])
                  if nodeY:
                    addFromFatherNodeY = node["pattern"].copy()
                    addFromFatherNodeY.append(1)
                    nodeY["pattern"] = addFromFatherNodeY
                    # print(nodeY,"nodeY")
                    Q.append(nodeY)
                  else:
                    print("None is not True...:nodeY")

              if len(result) in [10 , 100 ,500, 1000 ,2000,3000,4000,5000,6000,7000,8000,9000, 10000,20000,30000,40000,50000 , 100000]:
                print("10 , 100 ,500, 1000 ,2000,3000,4000,5000,6000,7000,8000,9000, 10000 ,20000,30000,40000,50000 , 100000")
              with open(f'scraperData.json', 'w', encoding='utf-8') as outFile:
                outFile.write(json.dumps(result))  

        print("Proceso terminado...")
        return result

getNodesLvlOrder()