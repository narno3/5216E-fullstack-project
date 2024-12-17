# Exemple de création de classe en python
class Question():
	def init(self, title: str, text: str, position: int, image: str, possibleAnswers: dict):
		self.title = title
		self.text = text
		self.position = position
		self.image = image
		self.possibleAnswers = possibleAnswers

	def toJson(self):
		json = {}
		json['title'] = self.title
		json['text'] = self.text
		json['position'] = self.position
		json['image'] = self.image
		json['possibleAnswers'] = self.possibleAnswers
		return json
     