#graph.py is the interface of metrics.py

import plotly.graph_objects as go

#read data from txt
data = []
f = open("data.txt", "r")
if f.mode == "r":
    #sort data for visualization
    for line in f:
        clLine = line.strip()
        line = clLine.split("        Followers: ")
        line[1] = line[1].split(",")[0] + line[1].split(",")[1]
        line[1] = int(line[1])
        data.append(line)
        print(line)
          
    print(data)

    xTime = []
    yFollowers = []

    for p in data:
        xTime.append(p[0])
        yFollowers.append(p[1])

print(xTime , "\n" , yFollowers)

#draw Followers Graph
fig = go.Figure(
    data=[go.Line(x=xTime, y=yFollowers)],
    layout_title_text="Followers"
)
fig.show()
