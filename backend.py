# coding=utf-8

from flask import *
import os
app = Flask(__name__)


def buildlevel2(name, link):
	return "<li class='level2' link=%s>%s</li>" % (link, name)

def buildlevel1(title):
	return "<div class='level1'>%s</div>" % title

def insert(html):
	s = ""
	# 特殊处理新手引导
	dirs = os.listdir("doc")
	path = "doc/%s" % "新人指引"
	if os.path.isdir(path):
		s += buildlevel1("新人指引")
		s += "<ul>"
		for level2 in sorted(os.listdir(path)):
			if level2.endswith(".md"):
				link = "doc/%s/%s" % ("新人指引", level2)
				s += buildlevel2(level2, link)
		s += "</ul>"

	dirs.remove("新人指引")
	for level1 in sorted(dirs):
		path = "doc/%s" % level1
		if os.path.isdir(path):
			s += buildlevel1(level1)
			s += "<ul>"
			for level2 in sorted(os.listdir(path)):
				if level2.endswith(".md"):
					link = "doc/%s/%s" % (level1, level2)
					s += buildlevel2(level2, link)
			s += "</ul>"
	html = html.replace("内容链接锚点", s)
	return html


@app.route("/")
def index():
	f = open("index.html")
	return insert(f.read())

@app.route('/<path:filename>')
def show_user_profile(filename):
	try:
		if filename.endswith(".jpg") or filename.endswith("png"):
			return send_file(filename, mimetype='image/jpeg')
		elif filename.endswith(".css"):
			return send_file(filename, mimetype='text/css')
		elif filename.endswith(".js"):
			return send_file(filename, mimetype='application/x-javascript')
		elif filename.endswith(".md"):
			return send_file(filename)
		elif filename.endswith("htm") or filename.endswith("html"):
			return send_file(filename, mimetype='text/html')
		else:
			return "你好坏啊！"
	except Exception, e:
		return e

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
