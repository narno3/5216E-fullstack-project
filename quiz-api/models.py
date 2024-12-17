# Exemple de création de classe en python
class Question():
	def init(self, title: str, text: str, position: int, image: str, possibleAnswers: dict):
		self.title = title
		self.text = text
		self.position = position
		self.image = image
		self.possibleAnswers = possibleAnswers

	def questionJsonToPython(json):
		title = json['title']
		position = json['position']
		text = json['text']
		image = json['image']
		answers = json['possibleAnswers']
		return new Question()

	def questionJsonToPython(question):
		title = json['title']
		position = json['position']
		text = json['text']
		image = json['image']
		answers = json['possibleAnswers']
		return new Question()
     