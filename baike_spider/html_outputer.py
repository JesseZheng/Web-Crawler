# -*- coding: utf-8 -*-

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
        fout.write("<html>")
        fout.write("<body>")


        for data in self.datas:
            fout.write("<table border='1'>")
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td ><a href=%s>点我哦哦</a></td></tr>" % data['url'])
            fout.write("<tr><td colspan='2'>%s</td>" % data['summary'])
            fout.write("</tr>")
            fout.write("</table>")
            fout.write("<br>")

        fout.write("</body>")
        fout.write("</html>")
