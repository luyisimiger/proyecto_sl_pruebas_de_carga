from flaskapp.logic.ab import runab

args = ["ab", "-c", "5", "-n", "20", "http://www.github.com/"]
result = runab(args)
print(result)
