from typing import TypedDict

class UserData(TypedDict) : 
	name : str
	age : int
	items :  list[dict[str, str]]
	active : bool
	affiliation : None

data : UserData = {
	"name" : "Rick",
	"age" : 42,
	"items" : [{"name": "Portal Gun"}, {"name": "Plumbus"}],
	"active" : True,
	"affiliation" : None
}