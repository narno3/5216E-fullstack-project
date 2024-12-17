# Exemple de création de classe en python
class Question():
	def init(self, title: str, text: str, position: int, image: str, possibleAnswers: dict):
		self.title = title
		self.text = text
		self.position = position
		self.image = image
		self.possibleAnswers = possibleAnswers

	def to_json(self) -> dict:
		"""creates json from question object"""
		json = {}
		json['title'] = self.title
		json['text'] = self.text
		json['position'] = self.position
		json['image'] = self.image
		json['possibleAnswers'] = self.possibleAnswers
		return json

	@classmethod
	def from_json(cls, json: dict) -> "Question":
		"""creates python object from json"""
		return cls(
			title=json['title'],
			position=json['position'],
			text=json['text'],
			image = json['image'],
			answers = json['answers']
		)
