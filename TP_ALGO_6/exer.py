martrice_adj=[
	[0, 1, 1], # 1 relié à 2,3
	[1, 0, 1], # 2 relié à 3,1
	[1, 1, 0]  # 3 relié à 1,2
]
class Graphe:
	def __init__(self, matrAdj):
		self.matrAdj = matrAdj
	def isMatNotOriented(self):
		tailleMat = range(len(self.matrAdj))
		test = True
		for x in tailleMat:
			for y in tailleMat:
				if self.matrAdj[x][y]!=self.matrAdj[y][x]:
					test = False
		return test
	def isListeNotOriented(self):
		pass
		
	def createListAdj(self):
		tailleMat = range(len(self.matrAdj))
		listAdj = {}
		for i in tailleMat:
			listAdj[i]=[]
			for j in tailleMat:
				if self.matrAdj[i][j]==1:
					listAdj[i].append(j)
		return listAdj

				
g = Graphe(martrice_adj)
print(g.isMatNotOriented())
print(g.createListAdj())

