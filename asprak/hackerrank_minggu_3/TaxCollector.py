def TaxCollector(G:float,J:int)->float:
    if G >= 0 and J >= 0:
        if G < 50:
            return (G * J) * 0.85
        elif G <= 150 and G >= 50:
            return (G * J) * 0.9
        elif G <= 500 and G > 150:
            return (G * J) * 0.95
        else:
            return G * J

#JANGAN DIUBAH!
print(eval(input()))