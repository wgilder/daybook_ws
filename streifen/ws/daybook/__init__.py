
def get_about():
    return "{ message:'hello' }", 200

def get_version():
    return """"{
	"author": "Walter Gildersleeve",
	"contact": "wmg@puppet.com",
	"daybook.ws.version": "0.0.1"
}""", 200